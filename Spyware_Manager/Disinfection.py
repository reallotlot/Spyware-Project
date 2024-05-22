import datetime
import os
import shutil
import subprocess
import pywintypes
import win32file
import win32con



class disinfect():
    def __init__(self, file_path, file_name) -> None:
        self.file_path = file_path
        self.file_name = file_name
        self.quarantine_dir = f'..\Spyware_Manager\quarantined_files\{os.path.splitext(self.file_name)[0]}'
        self.quarantine_file = f'..\Spyware_Manager\quarantined_files\{os.path.splitext(self.file_name)[0]}\{self.file_name}'
    
    
    def isolate(self):
        if not os.path.exists(self.quarantine_dir) and os.path.exists(self.file_path) :
            os.makedirs(os.path.abspath(self.quarantine_dir))
            shutil.move(self.file_path, self.quarantine_dir)
            print("isolated")
        else:
            print("file already isolated or doesnt exist")
                  
    
    def delete_file(self):
        print("deleting")
        try:
            with open(self.quarantine_file, 'wb') as file:
                file.write(b'')
            os.remove(self.quarantine_file)
            shutil.rmtree(self.quarantine_dir)
            print("finished")
        except Exception as e:
            print(e)
            
            
    def run_disinfection(self):
        self.isolate()
        self.delete_file()
            
            
            
            
if __name__ == "__main__":
    sus_file = disinfect(r'..\malware\AutoClicker.exe', 'AutoClicker.exe')
    sus_file.run_disinfection()