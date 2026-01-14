import hashlib

def hash_check(n):

    encoded = n.encode()
    alpha = hashlib.sha256()
    alpha.update(encoded)
    return alpha.hexdigest()


def hash_verify(m,n):
    if m == n:
        return True
    else:
        return False
    
