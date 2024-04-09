import Spyware_Manager.HashManager as HashManager
import os

def getHash():
    hashes = []
    for i in os.listdir("malware"):
        hashes.append(HashManager.getHashFile(os.path.abspath(os.path.join("malware",i))))
    return hashes
    
    
if __name__ == "__main__":
    print(getHash())