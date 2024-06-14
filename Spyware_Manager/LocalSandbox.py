import os
import subprocess
import time
import shutil

from .sandbox.Volatility import run_analysis

# Important variables
VBOXMANAGE = r'C:\Program Files\Oracle\VirtualBox\VBOXMANAGE'
VBOXNAME = "sandbox"
SHARED = r'C:\Users\lotan\project\Spyware-Project\Spyware_Manager\sandbox\shared'

def copy_malware(path):
    if not os.path.exists(os.path.join(SHARED, os.path.basename(path))):
        shutil.copy(path, SHARED)
    
def delete_malware(file_name):
    path = os.path.join(SHARED, file_name)
    if os.path.exists(path):
        os.remove(path)



def start_vm():
    subprocess.run([VBOXMANAGE, "startvm", VBOXNAME, "--type", "headless"], check=True)
    print(f"Virtual machine sandbox started successfully.")
    
    
def execute_malware(file_name):
    guest_path = f'\\\\VBoxSvr\\sandbox\\shared\\{file_name}'
    print("executing malware")
    
    session_info = subprocess.Popen([VBOXMANAGE, "guestcontrol", VBOXNAME, "run", "--username", "Administrator", "--password", "1234", "--exe", guest_path, "--verbose"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Executed file {guest_path} on VM {VBOXNAME}.")
    print(session_info)


def make_memory_dump():
    dump_file = r'C:\Users\lotan\project\Spyware-Project\Spyware_Manager\sandbox\dump.raw'
    if os.path.exists(dump_file):
        os.remove(dump_file)
    
    subprocess.run(["VBoxManage", "debugvm", VBOXNAME, "dumpvmcore", "--filename", dump_file], check=True)
    print(f"Memory dumped to {dump_file}")
    
def stop_running():
    subprocess.run([VBOXMANAGE, "controlvm", VBOXNAME, "poweroff"], check=True)
    print(f"VM {VBOXNAME} powered off.")


def restore_snapshot():
    subprocess.run([VBOXMANAGE, "snapshot", VBOXNAME, "restore", 'default'])
    print(f"VM {VBOXNAME} restored to snapshot")


def scan_file(path):
    
    # Confirm the file is executable
    executable_file_types = [
        ".exe",".bat",".cmd",".com",".msi",".vbs",".ps1",".jar",".msc",".scr",".py",   
    ]
    for type in executable_file_types:
        if type in path:
            break
    else:
        print("File is not executable")
        return None
    
    file_name = os.path.basename(path)
    print(file_name)
    # Start the sandbox and give it some time to load up
    try:
        copy_malware(path)
        start_vm()
        time.sleep(30)
    
        # Wait for 30 seconds before taking the memory dump
        execute_malware(file_name)
        time.sleep(30)
        make_memory_dump()
    
    finally:
        try:
            delete_malware(file_name)
            stop_running()
            restore_snapshot()
        except Exception as e:
            print(e)
            
    
    # Analyze with volatility
    malicious, info = run_analysis()
    
    results = {
        'name': file_name,
        'path': path,
        'info': f'{info}'
    }
    if malicious:
        return results


def scan_dir(path):
    results = []
    if not os.path.isdir(path):
        res = scan_file(path)
        if res != []:
            results.append(res)
    else:
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                results.extend(scan_dir(file_path))
            else:
                res = scan_file(file_path)
                if res != []:
                    results.append(res)
    
    return results

if __name__ == "__main__":
    pass