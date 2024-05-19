import time
import requests
import hashlib
import os

from cryptography import fernet
from vt import Client



#LOAD ENCRYPTED API KEY
def load_key():
    enc_key = os.getenv("API_ENCRYPTION_KEY")
    api_key = ''
    with open(r'api_keys.txt', "rb") as file:
        api_key = file.read().split(b"\n")[0]
        
    return fernet.Fernet(enc_key).decrypt(api_key).decode()

if True:
    api_key = load_key()
    vt_client = Client(api_key)
    
    
def scan_file(path):
    with open(path, 'rb') as file:
        
        vendors = ['google', 'avast', 'avg', 'kaspersky', 'malwarebytes', 'microsoft', 'bitdefender']
        
        # get sha256 (vt api identifies files by their hash and not by the name)
        text = file.read()
        sha256 = hashlib.sha256(text).hexdigest()
        
        #file an anlyses request for the file
        scan_request = vt_client.scan_file(file, wait_for_completion=True)
        scan_result = vt_client.get_object(f"/analyses/{scan_request.id}")
        print(scan_result.status)
        
        #get the scan anlyses results
        scan_result = vt_client.get_object(f"/files/{sha256}")
        results = scan_result.last_analysis_results
        data = {
            'name': scan_result.names[0],
            'report': False
        }
        
        for vendor in results:
            info = results[vendor]
            if vendor.lower() in vendors and info['category'] in ['malicious', 'suspicious']:
                data['report'] = True
                
        return data
            
 
            
            
def scan_dir(path):
    results = []
    
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            results = results + scan_dir(file_path)
        else:
            result = scan_file(file_path)
            if result['report'] == True:
                results.append(result)
        
    return results
    
    
if __name__ == "__main__":
    path = r'C:\Users\lotan\מסמכים\Spyware-Project\malware'
    
    print(scan_dir(path))
    
    
    #close the client at the end of use to prevent problems on the next run
    vt_client.close()
            