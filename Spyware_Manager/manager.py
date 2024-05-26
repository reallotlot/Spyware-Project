import HashManager 
import YaraManager 
import HybridManager 
import VirusTotal
import os
import threading


def scan_hash(file_path):
    return HashManager.hash_scan_dir(file_path) if os.path.isdir(file_path) else HashManager.hash_scan_file(file_path)


def scan_yara(file_path):
    return YaraManager.scan_yara(file_path)
    

def scan_hybrid(path):
    return HybridManager.scan_dir(path)
    
    
def virus_total(path):
    if os.path.isdir(path):
        return VirusTotal.scan_dir(path)
    else:
        return VirusTotal.scan_file(path)
    

if __name__ == "__main__":
    print(virus_total(r'..\malware'))
    
