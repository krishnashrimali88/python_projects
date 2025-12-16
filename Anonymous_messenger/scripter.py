import socket
import threading
from tkinter import *
from tkinter.messagebox import *



def client_receiver():
    while True:
        try:
           x = client.recv(1024).decode()
           f1.insert(END,f'USER:{x}\n')
        except:
            break      


def message_sender():
    y = r1.get()
    f1.insert(END,f'YOU:{y}\n')
    client.send(y.encode())
    r1.delete(0,END)


try:
    client = socket.socket()
    print("socket has been created")
    client.connect(("localhost",99))
except:
    showerror('ERROR',"cannot connect to the server")
    exit(0)



root = Tk()

root.geometry('300x400')

l1 = Label(root,text="Messager:")

f1 = Text(root,width=50,height=20)

r1 = Entry(root,width=50)

b1 = Button(root,text = 'send' ,command=message_sender)

l1.pack(side=TOP)
f1.pack(pady=5)
r1.pack()
b1.pack()

threading.Thread(target=client_receiver,args=(),daemon=True).start()
root.mainloop()