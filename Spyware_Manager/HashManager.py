import hashlib

def get_hash(path):
    sha256 = hashlib.sha256(path)
    md5 = hashlib.md5(path)
    
