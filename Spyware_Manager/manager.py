from . import HashManager ,YaraManager ,HybridManager ,VirusTotal, Disinfection
import os
import threading
from pymongo import MongoClient


class Analysis():
    def __init__(self, path) -> None:
        self.path = path
        self.results = [None for i in range(4)]
        self.lock = threading.Lock()


    def __load_key(self):
        try:
            key = os.getenv("DATABASE_KEY")
            return key
        except:
            pass


    def __scan_hash(self, path):
        res = HashManager.hash_scan_dir(path)
        with self.lock:
            self.results[0] = ('hash', res)
        return res
        


    def __scan_yara(self, path):
        res = YaraManager.scan_yara(path)
        with self.lock:
            self.results[1] = ('yara', res)
        return res

    def __scan_hybrid(self, path):
        res = HybridManager.scan_dir(path)
        with self.lock:
            self.results[2] = ('hybrid', res)
        return res


    def __virus_total(self, path):
        res = VirusTotal.scan_dir(path)
        with self.lock:
            self.results[3] = ('vt', res)
        return res
    
    
    def __send_gui(self):
        finalResult = ''
        # turn the analysis results into human readable text
        for res in self.results:
            print(res)
            curPath = res[1]['path']
            if curPath not in finalResult:
                finalResult += f'Malicious file detected at {curPath}\n'
        if finalResult == '':
            return f"{self.path} is clear!"
        return finalResult
    

    def __save_data(self):
        return ''
        client = MongoClient('localhost')
        key = self.__load_key()
        

    
    def load_data(self) -> str: # <-- not private and wil always return the data in the database
        pass


    def disinfect(self, path, file_name):
        pass

    def run_analysis(self):
        #set up the threads
        hashThread = threading.Thread(target=self.__scan_hash, args=(self.path,))
        yaraThread = threading.Thread(target=self.__scan_yara, args=(self.path,))
        hybridThread = threading.Thread(target=self.__scan_hybrid, args=(self.path,))
        vtThread = threading.Thread(target=self.__virus_total, args=(self.path,))
        threads = [hashThread, yaraThread, hybridThread, vtThread]

        #run the threads
        print("starting the threads")
        for thread in threads:
            thread.start()

        print("waiting for the threads to finish")
        #wait for threads to finish
        for thread in threads:
            thread.join()
        print("all threads finished.")


        # Create a new list with only non-empty results
        filtered_results = [res for res in self.results if res[1] != [] and res[1] is not None]
        print(filtered_results)
        

        #save scan data to database
        self.__save_data()


        

        # print the results
        
        return self.__send_gui()



if __name__ == "__main__":
    pass
