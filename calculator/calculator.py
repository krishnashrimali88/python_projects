import customtkinter as ctk


class calculator:
    def __init__(self):
      
        
        self.root = ctk.CTk()
        self.root.title('Calculator')
        self.root.geometry('320x550')
        self.root.resizable(False,False)
        self.enter = ctk.CTkEntry(self.root,width=350,height=200,state='normal',font=ctk.CTkFont('Arial',50,'bold'))
        self.enter.pack(pady = 10)


        def result():
            try:
                new = self.enter.get()
                op = eval(new)

            except ZeroDivisionError as e:
                self.enter.delete(0,'end')
                self.enter.insert('end','ERROR')


            except ValueError as e:
                self.enter.delete(0,'end')
                self.enter.insert('end','ERROR')     

            except Exception as e:
                self.enter.delete(0,'end')
                self.enter.insert('end','ERROR')

            else:
                self.enter.delete(0,'end')
                self.enter.insert('end',str(op))


        def button(n):
            print(f'button no{n} is clicked')
            self.enter.insert('end',n)

        def clear():
            self.enter.delete(0,'end')    
        
    


        self.one = ctk.CTkButton(self.root,text=1,width=50,command=lambda:button(1))
        self.one.place(x = 10,y = 220)

        self.two = ctk.CTkButton(self.root,text=2,width=50,command=lambda:button(2))
        self.two.place(x = 80 ,y = 220)

        self.three = ctk.CTkButton(self.root,text=3,width=50,command=lambda:button(3))
        self.three.place(x = 160 ,y = 220)

        self.four = ctk.CTkButton(self.root,text=4,width=50,command=lambda:button(4))
        self.four.place(x = 240 ,y = 220)

        self.five = ctk.CTkButton(self.root,text=5,width=50,command=lambda:button(5))
        self.five.place(x = 10 ,y = 260)
        
        self.six = ctk.CTkButton(self.root,text=6,width=50,command=lambda:button(6))
        self.six.place(x = 80 ,y = 260)
        
        self.seven = ctk.CTkButton(self.root,text=7,width=50,command=lambda:button(7))
        self.seven.place(x = 160 ,y = 260)
        
        self.eight = ctk.CTkButton(self.root,text=8,width=50,command=lambda:button(8))
        self.eight.place(x = 240 ,y = 260)

        self.nine = ctk.CTkButton(self.root,text=9,width=50,command=lambda:button(9))
        self.nine.place(x = 10 ,y = 300)
        
        self.zero = ctk.CTkButton(self.root,text=0,width=50,command=lambda:button(0))
        self.zero.place(x = 80 ,y = 300)
    
        self.add = ctk.CTkButton(self.root,text="+",width = 50, command=lambda:button('+'))
        self.add.place(x = 160,y = 300)
        
        self.sub = ctk.CTkButton(self.root,text="-",width = 50, command=lambda:button('-'))
        self.sub.place(x = 240,y = 300)

        self.mul = ctk.CTkButton(self.root,text="*",width = 50, command=lambda:button('*'))
        self.mul.place(x = 10,y = 340)

        self.div = ctk.CTkButton(self.root,text="/",width = 50, command=lambda:button('/'))
        self.div.place(x = 80,y = 340)
                       

    
        self.result = ctk.CTkButton(self.root,text="=",width = 50, command=result)
        self.result.place(x = 160,y = 340)
        

        self.clear = ctk.CTkButton(self.root,text='CLR',width=50,command=clear)
        self.clear.place(x = 240,y = 340)

        self.root.mainloop()







if __name__ == '__main__':
    calculator()
