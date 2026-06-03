from customtkinter import CTk,CTkFrame,CTkLabel,CTkEntry,CTkTextbox,CTkButton,CTkFont
from link_search import search,image_search

root = CTk()
root.title('links search')

root.geometry('820x450')
root.resizable(False,False)

side = CTkFrame(root,height=800,width=200)
side.place(relx = 0.0,rely = 0.0,anchor = 'nw')

main = CTkFrame(root,height=450,width=550)
main.place(relx = 0.26,rely = 0.50,anchor = 'w')

l1 = CTkLabel(side,text='v1.0',text_color='white')
l1.place(relx= 0.05,rely=0.00,anchor = 'nw')

#code for searching links

l2 = CTkLabel(main,text="links search",font=CTkFont('arial',20,'bold'),text_color='white')
l2.place(relx= 0.5,rely = 0.01,anchor = 'n')

ent = CTkEntry(main,width=250,placeholder_text='enter the topic here')
ent.place(relx = 0.5,rely= 0.10,anchor = 'n')

link_btn = CTkButton(main,text='search',width=80,command=lambda:search(ent.get(),t1))
link_btn.place(relx = 0.75,rely = 0.10)

t1 = CTkTextbox(main,width = 450)
t1.place(relx = 0.10,rely  = 0.3)


def demolish():
    for widget in main.winfo_children():
        widget.destroy()


def button1():
    demolish()
    l2 = CTkLabel(main,text="links search",font=CTkFont('arial',20,'bold'),text_color='white')
    ent = CTkEntry(main,width=250,placeholder_text='enter the topic here')
    t1 = CTkTextbox(main,width = 450)
    link_btn = CTkButton(main,text='search',width=80,command=lambda:search(ent.get(),t1))
   




    l2.place(relx= 0.5,rely = 0.01,anchor = 'n')
    ent.place(relx = 0.5,rely= 0.10,anchor = 'n')
    link_btn.place(relx = 0.75,rely = 0.10)
    t1.place(relx = 0.10,rely  = 0.3)
   


def button2():
    demolish()
    l6 = CTkLabel(main,text="images search",font=CTkFont('arial',20,'bold'),text_color='white')
    ent1 = CTkEntry(main,width=250,placeholder_text='enter the topic here')
    t2 = CTkTextbox(main,width = 450)
    link_btn2 = CTkButton(main,text='search',width=80,command=lambda:image_search(ent1.get(),t2))
   




    l6.place(relx= 0.5,rely = 0.01,anchor = 'n')
    ent1.place(relx = 0.5,rely= 0.10,anchor = 'n')
    link_btn2.place(relx = 0.75,rely = 0.10)
    t2.place(relx = 0.10,rely  = 0.3)

b1 = CTkButton(side,text='Topic search',command=button1)
b1.place(relx= 0.05,rely=0.05,anchor = 'nw')

b2 = CTkButton(side,text='image search',command=button2)
b2.place(relx= 0.05,rely=0.10,anchor = 'nw')






root.mainloop()
