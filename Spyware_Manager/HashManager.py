import hashlib

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
    with open("Spyware_Manager\hashfiles\md5.txt", 'r') as file:
        text = list(file.read().split("\n"))
        if md5 in text:
            print(md5)
            return True
    return False


def check_sha256(sha256):
    hashes = list(open("Spyware_Manager\hashfiles\sha256hashes.txt", 'r').read().split("\n"))
    info = list(open("Spyware_Manager\hashfiles\sha256info.txt", 'r').read().split("\n"))
    for i in range(len(hashes)):
        if sha256 in hashes[i]:
            print(sha256 + " " + info[i])
            return True
    return False


def hash_scan(path):
    md5 = get_md5(path)
    sha256 = get_sha256(path)
    return check_md5(md5) or check_sha256(sha256)
    
        
if __name__ == "__main__":
    print(hash_scan(r"malware\delete_windows_malware.exe"))