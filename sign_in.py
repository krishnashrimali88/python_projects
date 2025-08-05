from tkinter import *
from tkinter import messagebox
import database


def validation():
    username = input1.get()
    password  = input2.get()

    if not username or not password:
        print("you havn't added input")

    elif database.watcher(username,password):
        messagebox.showinfo('Success','login sucessful')

    else:
        messagebox.showerror('Error','Entry denied')       

        



root = Tk()


root.title('Emplyoee login')
root.resizable(False,False)

root.geometry('500x500')

label = Label(root,text='Login',font=("calibri",20,"bold"))
label2 = Label(root,text='username:',font=("calibri",15))
label3 = Label(root,text='password:',font=("calibri",15))

input1 = Entry(root,width=50)
input2 = Entry(root,width=50)


b1 = Button(root,text="sign in",font=('calibri',12),command=validation)
label.place(x = 220,y =10) 
label2.place(x = 20,y =50)
label3.place(x = 20,y =90)
b1.place(x = 160,y = 140)
input1.place(x = 120,y=60)
input2.place(x = 120,y=100)


root.mainloop()