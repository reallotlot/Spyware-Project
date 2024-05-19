import os
import shutil
from ctypes import cdll, WinDLL

import psutil

class disinfect():
    def __init__(self, file_path, file_name) -> None:
        self.file_path = file_path
        self.file_name = file_name
        self.quarantine_dir = f'Spyware_Manager\quarantined_files\{os.path.splitext(self.file_name)[0]}'
        self.quarantine_file = f'Spyware_Manager\quarantined_files\{os.path.splitext(self.file_name)[0]}\{self.file_name}'
    
    
    def isolate(self):
        if not os.path.exists(self.quarantine_dir) and os.path.exists(self.file_path) :
            os.makedirs(self.quarantine_dir)
            shutil.move(self.file_path, self.quarantine_dir)
        
    
    def is_open(self):
        _sopen = cdll.msvcrt._sopen
        _close = cdll.msvcrt._close
        _SH_DENYRW = 0x10

        if not os.access(self.quarantine_file, os.F_OK):
            return None # file doesn't exist
        h = _sopen(self.quarantine_file, 0, _SH_DENYRW, 0)
        if h == 3:
            _close(h)
            return False # file is not opened by anyone else
        return True # file is already open
            
    
    def delete_file(self):
        print("deleting")
        try:
            shutil.rmtree(self.quarantine_dir)
            print("finished")
        except Exception as e:
            print(e)
            
            
    def run_disinfection(self):
        self.isolate()
        print(self.is_open())
        self.delete_file()
            
            
            
            
            
            
if __name__ == "__main__":
    sus_file = disinfect(r'malware\AutoClicker.exe', 'AutoClicker.exe')
    sus_file.run_disinfection()