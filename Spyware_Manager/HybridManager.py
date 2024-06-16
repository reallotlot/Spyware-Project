import os
import re
import subprocess
import time
import requests
import platform

from cryptography import fernet




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
    file_types = '.exe .scr .pif .dll .com .cpl .doc .docx .ppt .pps .pptx .ppsx .xls .xlsx .rtf .pub .sct .hta .py .pl .chm .msi'.split(' ')
    for type in file_types: 
        if type in file_name:
            break 
    else:
        return None #file is not executable
         
    
    api_key = 'mpdfmk1ua7d7a8aevv0az9ahf16bb4d256dkubbq567721e7lx578w28c86e01a0'
    api_endpoint = r'https://www.hybrid-analysis.com/api/v2/submit/file'
         
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
        'api-key': api_key
    }

    # Submit the file for analysis in the sandbox
    response = requests.post(api_endpoint, headers=headers, files=files, data=payload)
    analysis_id = ''
    if response.status_code == 201:
        analysis_result = response.json()
        analysis_id = analysis_result.get('job_id')
    else:
        return None
    
    
    #wait for the result
    status_endpoint = f"https://www.hybrid-analysis.com/api/v2/report/{analysis_id}/state"
    while True:
        status_response = requests.get(status_endpoint, headers=headers)
        status_data = status_response.json()
        
        if status_data.get('state') == 'SUCCESS' or status_data.get('state') == 'PARTIAL_SUCCESS':
            break
        elif status_data.get('state') == 'IN_PROGRESS':
            time.sleep(5)
        else:
            return None
    
    #retrieve the data from the reprot
    report_endpoint = f"https://www.hybrid-analysis.com/api/v2/report/{analysis_id}/summary"
    report_response = requests.get(report_endpoint, headers=headers)
    
    
    if report_response.status_code == 200:
        
        info = report_response.json()
        is_mal = info.get('verdict')
        info_dict = {
            'path': os.path.abspath(path),
            'name': info.get('submit_name'),
            'info': f"Threat Score: {info.get('threat_score')}"
        }
        if is_mal in ['malicious', 'suspicious']:
            return info_dict
        else:
            return None
    else:
        return None
    
    
def scan_dir(path):
    results = []
    if not os.path.isdir(path):
        res = scan_file(path, os.path.basename(path))
        if res is not None: results.append(res) 
    else:
        for file in os.listdir(path):
            file_path = os.path.join(path,file)
            if os.path.isdir(file_path):
                results.extend(scan_dir(file_path))
            else:
                res = scan_file(file_path, file)
                if res is not None:
                    results.append(res)
    return results        
    
    
if __name__ == "__main__":
    print(scan_dir(r'C:\Users\lotan\project\Spyware-Project\malware\Flasher.exe'))