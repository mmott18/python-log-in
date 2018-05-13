import hashlib


def hash_data(data):
    hashed = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return hashed
