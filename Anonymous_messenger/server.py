import socket
import threading
import time

clients = []

def client_handler(conn,addr):
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break

            print(f"{addr}: {msg}")

            for c in clients:
                if c != conn:
                    c.send(msg.encode())

        except:
            break

    print("client disconnected:", addr)    
    clients.remove(conn)
    conn.close()

server = socket.socket()
server.bind(("localhost",99))
server.listen(5)
print("server running....")

while True:
    conn,addr = server.accept()    
    print("connected:",addr)
    clients.append(conn)

    threading.Thread(target=client_handler,args=(conn,addr), daemon=True).start()








    
