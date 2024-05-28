from . import HashManager ,YaraManager ,HybridManager ,VirusTotal
import os
import threading


class Analysis():
    def __init__(self, path) -> None:
        self.path = path
        self.results = [None for i in range(4)]
        self.lock = threading.Lock()

    def __scan_hash(self, path):
        res = HashManager.hash_scan_dir(path) if os.path.isdir(path) else HashManager.hash_scan_file(path)
        with self.lock:
            self.results[0] = res
        return res
        


    def __scan_yara(self, path):
        res = YaraManager.scan_yara(path)
        with self.lock:
            self.results[1] = res
        return res

    def __scan_hybrid(self, path):
        res = HybridManager.scan_dir(path)
        with self.lock:
            self.results[3] = res
        return res


    def __virus_total(self, path):
        res = VirusTotal.scan_dir(path)
        with self.lock:
            self.results[3] = res
        return res

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

        # print the results
        print("all threads finished.")
        return self.results



if __name__ == "__main__":
    pass
