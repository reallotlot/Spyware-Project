import hashlib
import os

#get a file md5 hash
def get_md5(path):
    md5 = None
    with open(path, 'rb') as file:
        text = file.read()
        md5 = hashlib.md5(text).hexdigest()
    return md5


# get a file sha256 hash
def get_sha256(path):
    sha256 = None
    with open(path, 'rb') as file:
        text = file.read()
        sha256 = hashlib.sha256(text).hexdigest()
    return sha256
        

#check for the md5 and sha256 in the malicious hash file (respectively)  
def check_md5(md5):
    path = f'{os.path.dirname(os.path.abspath(__file__))}\hashfiles\md5.txt'
    with open(path, 'r') as file:
        text = list(file.read().split("\n"))
        if md5 in text:
            print(md5)
            return True
    return False


def check_sha256(sha256):
    hash_path = f'{os.path.dirname(os.path.abspath(__file__))}\hashfiles\sha256hashes.txt'
    hashes = list(open(hash_path, 'r').read().split("\n"))
    for i in range(len(hashes)):
        if sha256 in hashes[i]:
            return True
    return False


def hash_scan_file(path):
    md5 = get_md5(path)
    sha256 = get_sha256(path)
    #print(md5 + "\n" + sha256 + "\n")
    return check_md5(md5) or check_sha256(sha256)
    

def hash_scan_dir(path):
    results = {}
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            hash_scan_dir(file_path)
        else:
            result = hash_scan_file(file_path)
            if result:
                results[file] = result
    return results        
        
               
if __name__ == "__main__":
    pass