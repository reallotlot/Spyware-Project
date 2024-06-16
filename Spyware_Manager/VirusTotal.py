import time
import requests
import hashlib
import os

from cryptography import fernet

   
    
def scan_file(path):
    api_key = '390d84de22c52785ecabaa956966b4aedba5a793c41e65c53543baea26c2c1b3'

    #trusted vendors
    trusted_vendors = ['google', 'avast', 'avg', 'kaspersky', 'malwarebytes', 'microsoft', 'bitdefender']

    #set the endpoint to files and apply the api key as the header
    endpoint = 'https://www.virustotal.com/api/v3/files'
    headers = {
        "accept": "application/json",
        'x-apikey': api_key
    }   

    #upload file data to virus total
    with open(path, 'rb') as file:
        sha256 = hashlib.sha256(file.read()).hexdigest()
        files = {'file': file}
        upload_response = requests.post(endpoint, headers=headers, files=files)

    if upload_response.status_code == 200:
        # get the analysis id
        upload_result = upload_response.json()
        analysis_id = upload_result.get('data').get('id')
        #print(f"File uploaded successfully. Analysis ID: {analysis_id}")

        # Check the analysis status
        analysis_url = f'https://www.virustotal.com/api/v3/analyses/{analysis_id}'

        # wait for completion
        while True:
            analysis_response = requests.get(analysis_url, headers=headers)
            analysis_result = analysis_response.json()
            if analysis_response.status_code == 200:
                if analysis_result.get('data').get('attributes').get('status') == 'completed':
                    #print("Analysis completed!")
                    break
                else:
                    time.sleep(5)
            else:
                #print(f"Error: {analysis_response.status_code}")
                #print(analysis_response.text)
                return None
            
        #get the results
        result_endpoint = f'https://www.virustotal.com/api/v3/files/{sha256}'
        result_response = requests.get(result_endpoint, headers=headers)

        if result_response.status_code == 200:
            results = result_response.json()
            res = results.get('data').get('attributes').get('last_analysis_results')
            for vendor in res:
                if vendor.lower() in trusted_vendors:
                    if res[vendor]['category'].lower() in ['malicious', 'suspicious']:
                        info = {
                            'path' : os.path.abspath(path),
                            'name' : os.path.basename(path),
                            'info' : vendor
                        }
                        return info
        else:
            return None


    else:
        return None
            
            
def scan_dir(path):
    results = []
    res = ''
    if not os.path.isdir(path):
        res = scan_file(path)
        if res is not None:
            results.append(res)
    else:
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if not os.path.isdir(file_path):
                res = scan_file(file_path)
                if res is not None:
                    results.append(res)
            else:
                res = scan_dir(file_path)
                results = results + res
        
    return  results
    
    
if __name__ == "__main__":
    print(scan_dir(r'C:\Users\lotan\project\Spyware-Project\malware\Flasher.exe'))