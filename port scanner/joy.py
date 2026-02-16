import socket


def portscan(target,port,timeout=0.5):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        conn = s.connect((target,port))
        s.settimeout(timeout)
        s.close()
        return True
    except:
        return False
    

