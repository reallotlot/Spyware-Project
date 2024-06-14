from . import HashManager ,YaraManager ,HybridManager ,VirusTotal, Disinfection, StringsManager, LocalSandbox
import os
import threading
from datetime import datetime
from cryptography.fernet import Fernet
from pymongo import MongoClient



class Analysis():
    def __init__(self) -> None:
        self.results = []
        self.lock = threading.Lock()
        self.SCAN_ID = 0


    def __load_key(self):
        key = os.getenv("DATABASE_KEY")
        if key is None:
            key = Fernet.generate_key().decode()
            os.system(f'setx DATABASE_KEY {key}')
            print(key)
            return None
        return key
            

    def __scan_sandbox(self, path):
        res = LocalSandbox.scan_dir(path)
        with self.lock:
            self.results.append(('SandboxAnalysis', res))
        return res
    

    def __scan_hash(self, path):
        res = HashManager.hash_scan_dir(path)
        with self.lock:
            self.results.append(('HashScan', res))
        return res
        

    def __scan_yara(self, path):
        res = YaraManager.scan_yara(path)
        with self.lock:
            self.results.append(('YARA', res))
        return res

    def __scan_hybrid(self, path):
        res = HybridManager.scan_dir(path)
        with self.lock:
            self.results.append(('HybridAnalysis', res))
        return res


    def __virus_total(self, path):
        res = VirusTotal.scan_dir(path)
        with self.lock:
            self.results.append(('VirusTotal', res))
        return res
    
    
    def __scan_string(self, path):
        res = StringsManager.scan_string(path)
        with self.lock:
            self.results.append(('StringScan', res))
        return res
    
    def __send_gui(self) -> str:
        finalResult = ''
        # turn the analysis results into human readable text
        for res in self.results:
            for file in res[1]:
                curPath = file['path']
                if curPath not in finalResult:
                    finalResult += f'Malicious file detected at {curPath}\n'
                    finalResult += f'Info: \n    {file["info"]}\n    {res[0]}\n\n'
                    print(finalResult)
        if finalResult == '':
            return f"The file is clear!"
        return finalResult
    

    def __save_data(self) -> None:
        #connect to database
        client = MongoClient('localhost')
        db = client['scans']
        collection = db['files']

        #load the encryption key
        enc_key = self.__load_key()
        if enc_key == None:
            return None
        enc = Fernet(enc_key)

        for engine in self.results:
            for res in engine[1]:
                #set up date and a ready data for each analysis
                data = {
                    'scanID': self.SCAN_ID,
                    'date': datetime.now().strftime("%d/%m/%Y"),
                    'hour': datetime.now().strftime("%H:%M:%S"),
                    'engine': enc.encrypt(engine[0].encode()),
                    'name': enc.encrypt(res['name'].encode()),
                    'path': enc.encrypt(res['path'].encode()),
                    'info': enc.encrypt(res['info'].encode()) if res['info'] != None else None
                }
                collection.insert_one(data)

    
    def load_data(self) -> list: # <-- not private and will always return the data in the database
        client = MongoClient('localhost')
        db = client['scans']
        collection = db['files']

        data = collection.find()
        
        #load the encryption key
        enc_key = self.__load_key()
        if enc_key == None:
            return None
        enc = Fernet(enc_key)
        

        #make the string that will be sent to the gui side
        msg = []
        for document in data:
            if bool(document): 
                decrypted_document = {}
                for field in document:
                    if document[field] is not None and field in ['name', 'path', 'info', 'engine']:
                        decrypted_document[field] = enc.decrypt(document[field]).decode()
                    else:
                        decrypted_document[field] = document[field]
                msg.append(decrypted_document)

        return msg


    def __disinfect(self, path, file_name):
        pass

    def run_analysis(self, path) -> str:
        try:
            self.SCAN_ID += 1
            #set up the threads
            hashThread = threading.Thread(target=self.__scan_hash, args=(path,))
            yaraThread = threading.Thread(target=self.__scan_yara, args=(path,))
            hybridThread = threading.Thread(target=self.__scan_hybrid, args=(path,))
            vtThread = threading.Thread(target=self.__virus_total, args=(path,))
            strThread = threading.Thread(target=self.__scan_string, args=(path,))
            sandboxThread = threading.Thread(target=self.__scan_sandbox, args=(path,))
            threads = [
                sandboxThread, hashThread, yaraThread,
                hybridThread, vtThread, strThread
            ]

            #run the threads
            print("starting the threads")
            for thread in threads:
                thread.start()

            print("waiting for the threads to finish")
            #wait for threads to finish
            for thread in threads:
                thread.join()
            print("all threads finished.")
            print(self.results)
            
            #create a new list with only non-empty results
            self.results = [res for res in self.results if res[1] != [] and res[1] is not None]

            #save scan data to database
            self.__save_data()

            # print the results
            return self.__send_gui()
        except Exception as e:
            return e



if __name__ == "__main__":
    pass
