import tkinter as tk

global num_var,num_add,show,test

num = []

def one():
        num.append("1")

        
def two():
        num.append("2")
        

def three():
        num.append("3")
        
        

def four():
        num.append("4")
      

def five():
        num.append("5")


def six():
        num.append("6")
      

def seven():
        num.append("7")
         

def eight():
        num.append("8")
       
def nine():
        num.append("9")
        

def equal():
        result.config(text=''.join(num))

def clear():
        num.clear()
        result.config(text=str("0.0"))


root  = tk.Tk()
root.resizable(False,False)
root.geometry("300x500")
root.title("calculator")


label1 = tk.Label(text="calculator",font=("calibri",20))


result = tk.Label(text="0.0",font=("calibri",18),justify="left",borderwidth=2,relief="solid")
button1 = tk.Button(text="1",font=("calibri",30),command=one,cursor="hand2")
button2 = tk.Button(text="2",font=("calibri",30),command=two,cursor="hand2")
button3 = tk.Button(text="3",font=("calibri",30),command=three,cursor="hand2")
button4 = tk.Button(text="4",font=("calibri",30),command=four,cursor="hand2")
button5 = tk.Button(text="5",font=("calibri",30),command=five,cursor="hand2")
button6 = tk.Button(text="6",font=("calibri",30),command=six,cursor="hand2")
button7 = tk.Button(text="7",font=("calibri",30),command=seven,cursor="hand2")
button8 = tk.Button(text="8",font=("calibri",30),command=eight,cursor="hand2")
button9 = tk.Button(text="9",font=("calibri",30),command=nine,cursor="hand2")
eq = tk.Button(text="=",font=("calibri",30),command=equal,cursor="hand2")
cls = tk.Button(text="clr",font=("calibri",30),command=clear,cursor="hand2")





label1.pack(pady=20)
result.place(x=20,y=60)
button1.place(x = 50,y=100)
button2.place(x= 110,y = 100)
button3.place(x = 170,y= 100)
button4.place(x = 50,y= 190)
button5.place(x = 110, y = 190)
button6.place(x = 170, y = 190)
button7.place(x= 50,y=280)
button8.place(x= 110,y=280)
button9.place(x= 170,y=280)
eq.place(x = 50,y = 370)
cls.place(x = 110,y = 370)


root.mainloop()