import tkinter as tk
global v,num,num1
num = []
num1 = []



def adder():
    global num,num1
    a1 = ''.join(num)
    a2 = ''.join(num1) 
    ans = int(a1) + int(a2)
    num1.clear()
    result.config(text=str(ans))
   
   

def subber():
    global num,num1
    a1 = ''.join(num)
    a2 = ''.join(num1) 
    ans = int(a1) - int(a2)
    num1.clear()
    result.config(text=str(ans))

def multiplier():
    global num,num1
    a1 = ''.join(num)
    a2 = ''.join(num1) 
    ans = int(a1) * int(a2)
    num1.clear()
    result.config(text=str(ans))   

def divisor():
    global num,num1
    a1 = ''.join(num)
    a2 = ''.join(num1) 
    ans = int(a1) / int(a2)
    num1.clear()
    result.config(text=str(ans))   


root  = tk.Tk()
root.resizable(False,False)
root.geometry("300x550")
root.title("calculator")

v = tk.IntVar(value=0)
k = tk.IntVar(value=0)

def radio1():
    if v.get() == 1:
        b1.config(state="disabled")
       
    elif v.get() == 0 :
        b1.config(state="active")
        
    
def radio2():
    if k.get() == 1 :
        bb.config(state="disabled")
    elif k.get() == 0 :
        bb.config(state="active")

def zero():
    if v.get() == 1:
        num.append("0")
        result.config(text=''.join(num))
    elif k.get() == 1:
        num1.append("0")
        result.config(text=''.join(num1))
  

def one():
    if v.get() == 1:
        num.append("1")
        result.config(text=''.join(num))
    elif k.get() == 1:
        num1.append("1")
        result.config(text=''.join(num1))
   

def two():
    if v.get() == 1:
        num.append("2")
        result.config(text=''.join(num))
    elif k.get() == 1:
        num1.append("2")
        result.config(text=''.join(num1))
    

def three():
    if v.get() == 1:
        num.append("3")
        result.config(text=''.join(num))
    elif k.get() == 1:
        num1.append("3")
        result.config(text=''.join(num1))
     

def four():
    if v.get() == 1:
        num.append("4")
        result.config(text=''.join(num))
    elif k.get() == 1:
        num1.append("4")
        result.config(text=''.join(num1))
    

def five():
    if v.get() == 1:
        num.append("5")
        result.config(text=''.join(num))
    elif k.get() == 1:
        num1.append("5")
        result.config(text=''.join(num1))
 

def six():
    if v.get() == 1:
        num.append("6")
        result.config(text=''.join(num))
    elif k.get() == 1:
        num1.append("6")
        result.config(text=''.join(num1))
          

def seven():
    if v.get() == 1:
        num.append("7")
        result.config(text=''.join(num))
    elif k.get() == 1:
        num1.append("7")
        result.config(text=''.join(num1))
    

def seven():
    if v.get() == 1:
        num.append("7")
        result.config(text=''.join(num))
    elif k.get() == 1:
        num1.append("7")
 

def seven():
    if v.get() == 1:
        num.append("7")
        result.config(text=''.join(num))
    elif k.get() == 1:
        num1.append("7")
        result.config(text=''.join(num1))
 

def eight():
    if v.get() == 1:
        num.append("8")
        result.config(text=''.join(num))
    elif k.get() == 1:
        num1.append("8")
        result.config(text=''.join(num1))


def nine():
    if v.get() == 1:
        num.append("9")
        result.config(text=''.join(num))
    elif k.get() == 1:
        num1.append("9")
        result.config(text=''.join(num1))
 

def clear():
    num.clear()
    num1.clear()
    result.config(text="0.0")




label1 = tk.Label(text="calculator",font=("calibri",20))
result = tk.Label(text="0.0",font=("calibri",18),justify="left",borderwidth=2,relief="solid")

bb = tk.Checkbutton(text="first number",font=("calibri",8),variable=v,onvalue=1,offvalue=0,command=radio1)
b1 = tk.Checkbutton(text="second number",font=("calibri",8),variable=k,onvalue=1,offvalue=0,command=radio2)

button0 = tk.Button(text="0",font=("calibri",30),cursor="hand2",command=zero)
button1 = tk.Button(text="1",font=("calibri",30),cursor="hand2",command=one)
button2 = tk.Button(text="2",font=("calibri",30),cursor="hand2",command=two)
button3 = tk.Button(text="3",font=("calibri",30),cursor="hand2",command=three)
button4 = tk.Button(text="4",font=("calibri",30),cursor="hand2",command=four)
button5 = tk.Button(text="5",font=("calibri",30),cursor="hand2",command=five)
button6 = tk.Button(text="6",font=("calibri",30),cursor="hand2",command=six)
button7 = tk.Button(text="7",font=("calibri",30),cursor="hand2",command=seven)
button8 = tk.Button(text="8",font=("calibri",30),cursor="hand2",command=eight)
button9 = tk.Button(text="9",font=("calibri",30),cursor="hand2",command=nine)

cls = tk.Button(text="clr",font=("calibri",18),cursor="hand2",command=clear)
ad = tk.Button(text="add",font=("calibri",18),cursor="hand2",command=adder)
sub = tk.Button(text="sub",font=("calibri",18),cursor="hand2",command=subber)
mul = tk.Button(text="mul",font=("calibri",18),cursor="hand2",command=multiplier)
div = tk.Button(text="div",font=("calibri",18),cursor="hand2",command=divisor)






bb.place(x = 10,y = 10)
b1.place(x = 10,y = 30)
label1.place(x = 110,y  = 5)
result.place(x=50,y=60)
button1.place(x = 50,y=100)
button2.place(x= 110,y = 100)
button3.place(x = 170,y= 100)
button4.place(x = 50,y= 190)
button5.place(x = 110, y = 190)
button6.place(x = 170, y = 190)
button7.place(x= 50,y=280)
button8.place(x= 110,y=280)
button9.place(x= 170,y=280)
button0.place(x = 240,y = 190)
cls.place(x = 50,y = 370)
ad.place(x = 110,y = 370)
sub.place(x = 170,y = 370)
mul.place(x = 50,y = 460)
div.place(x = 110,y = 460)


root.mainloop()
