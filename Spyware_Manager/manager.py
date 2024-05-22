import HashManager 
import YaraManager 
import HybridManager 
import VirusTotal
import os


def scan_hash(file_path):
    return HashManager.hash_scan_dir(file_path) if os.path.isdir(file_path) else HashManager.hash_scan_file(file_path)


def scan_yara(file_path):
    YaraManager.scan_yara()
    
    
if __name__ == "__main__":
    print(scan_hash(r'..\malware'))
    
