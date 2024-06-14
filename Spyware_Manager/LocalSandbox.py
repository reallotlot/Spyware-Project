import os
import subprocess
import time
import shutil

from sandbox import Volatility  

# Important variables
VBOXMANAGE = r'C:\Program Files\Oracle\VirtualBox\VBOXMANAGE.exe'
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
    try:
        subprocess.run([VBOXMANAGE, "startvm", VBOXNAME, "--type", "headless"], check=True)
        print(f"Virtual machine sandbox started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting VM {VBOXNAME}: {e}")

def execute_malware(file_name):
    guest_path = f'\\\\VBoxSvr\\shared\\{file_name}'
    print("Executing malware")

    try:
        subprocess.run([
            VBOXMANAGE, "guestcontrol", VBOXNAME, "run",
            "--username", "sandbox", "--password", "1234",
            "--exe", f"{guest_path}",
            "--verbose"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(f"Malware executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing file {guest_path} on VM {VBOXNAME}: {e}")

def make_memory_dump():
    dump_file = r'C:\Users\lotan\project\Spyware-Project\Spyware_Manager\sandbox\dump.raw'
    if os.path.exists(dump_file):
        os.remove(dump_file)
    
    try:
        subprocess.run([VBOXMANAGE, "debugvm", VBOXNAME, "dumpvmcore", "--filename", dump_file], check=True)
        print(f"Memory dumped to {dump_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error making memory dump: {e}")

def stop_running():
    try:
        subprocess.run([VBOXMANAGE, "controlvm", VBOXNAME, "poweroff"], check=True)
        print(f"VM {VBOXNAME} powered off.")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping VM {VBOXNAME}: {e}")

def restore_snapshot():
    try:
        subprocess.run([VBOXMANAGE, "snapshot", VBOXNAME, "restore", 'ready'], check=True)
        print(f"VM {VBOXNAME} restored to snapshot")
    except subprocess.CalledProcessError as e:
        print(f"Error restoring snapshot on VM {VBOXNAME}: {e}")

def scan_file(path):
    # Confirm the file is executable
    executable_file_types = [
        ".exe", ".bat", ".cmd", ".com", ".msi", ".vbs", ".ps1", ".jar", ".msc", ".scr", ".py",
    ]
    for type in executable_file_types:
        if type in path:
            break
    else:
        print("File is not executable")
        return None

    file_name = os.path.basename(path)
    print(f"Scanning file: {file_name}")

    # Start the sandbox and give it some time to load up
    try:
        copy_malware(path)
        start_vm()
        time.sleep(30)  # Adjust this delay as needed

        # Wait for malware execution
        execute_malware(file_name)
        # Make memory dump after execution
        make_memory_dump()
    finally:
        try:
            stop_running()
            restore_snapshot()
        except Exception as e:
            print(f"Error during cleanup: {e}")

        delete_malware(file_name)

    # Analyze with volatility after all operations are complete
    Volatility.run_all_plugins(file_name)


def scan_dir(path):
    if os.path.isfile(path):
        scan_file(path)
    else:
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                scan_file(file_path)

if __name__ == "__main__":
    scan_dir(r'C:\Users\lotan\project\Spyware-Project\malware')