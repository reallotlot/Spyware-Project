import os
import re
import subprocess
import time
import requests
import platform

from cryptography import fernet


# load the encrypted api key
def load_key():
    enc_key = os.getenv("API_ENCRYPTION_KEY")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'api_keys.txt')
    with open(path, "rb") as file:
        api_key = file.read().split(b"\n")[1]
        
    return fernet.Fernet(enc_key).decrypt(api_key).decode()

#Global variables
API_KEY = load_key()
API_ENDPOINT = r'https://www.hybrid-analysis.com/api/v2/submit/file'


def get_win_ver():
    command = 'systeminfo | findstr /B /C:"OS Name"'
    result = subprocess.run(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    match = re.search(r'Windows (\d+)', result.stdout.decode())
    if match:
        return match.group(1)
    else:
        return "Unknown version"
    

def get_env_id():
    env_ids = {
        'Linux': 310,
        '11': 140,
        '10': 160
    }
    
    env_id = ''
    syst = platform.system()
    
    if syst == "Windows":
        env_id = env_ids[get_win_ver()]
    else:
        env_id = env_ids[syst]
        
    return(env_id)


def scan_file(path, file_name):
    #check if the file is valid for sandbox dynamic analysis
    file_types = '.exe .dll .scr .sys .pdf .doc .docx .xls .xlsx .ppt .pptx .rtf .js .vbs .ps1 .zip .rar .7z .msi .iso'.split(' ')
    for type in file_types: 
        if type in file_name:
            break 
    else:
        #print('invalid file: ', file_name)
        return None #file is not valid for scanning
         
    #set up the data for the sandbox analysis
    payload = {
        'environment_id': get_env_id(),  
        'submit_name': file_name,  
    }
    files = {
        'file': (file_name, open(path, 'rb'), 'text/plain')
    }
    headers = {
        'accept': 'application/json',
        'api-key': API_KEY
    }

    # Submit the file for analysis in the sandbox
    response = requests.post(API_ENDPOINT, headers=headers, files=files, data=payload)
    analysis_id = ''

    if response.status_code == 201:
        analysis_result = response.json()
        analysis_id = analysis_result.get('job_id')
        #print("submitted file")
        #print("analysis ID:", analysis_id)
    else:
        #print("Failed to submit file.")
        #print("Status Code:", response.status_code)
        #print("Response:", response.text)
        return None
    
    
    #wait for the result
    status_endpoint = f"https://www.hybrid-analysis.com/api/v2/report/{analysis_id}/state"
    while True:
        status_response = requests.get(status_endpoint, headers=headers)
        status_data = status_response.json()
        
        if status_data.get('state') == 'SUCCESS':
            #print("analysis complete.")
            break
        elif status_data.get('state') == 'IN_PROGRESS':
            #print("analysis in progress.")
            time.sleep(5)
        else:
            #print("unexpected status:", status_data)
            return None
    
    
    #retrieve the data from the reprot
    report_endpoint = f"https://www.hybrid-analysis.com/api/v2/report/{analysis_id}/summary"
    report_response = requests.get(report_endpoint, headers=headers)
    
    if report_response.status_code == 200:
        info = report_response.json()
        info_dict = {
            'name': info.get('submit_name'),
            'path': f'{os.path.abspath(path)}',
            'verdict': info.get('verdict')
        }
        if info_dict['verdict'] in ['malicious','suspicious']:
            return info_dict
        else:
            return None
    else:
        #print("failed to fetch response")
        return None
    
    
def scan_dir(path):
    results = []
    if not os.path.isdir(path):
        res = scan_file(path, os.path.basename(path))
        if res is not None: results += res 
    else:
        for file in os.listdir(path):
            file_path = os.path.join(path,file)
            if os.path.isdir(file_path):
                results += scan_dir(file_path)
            else:
                res = scan_file(file_path, file)
                if res is not None:
                    results.append(res)
        return  results        
    
    
if __name__ == "__main__":
    pass