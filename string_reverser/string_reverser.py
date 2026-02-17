import customtkinter

root = customtkinter.CTk()

root.title("string reverser")

root.geometry("750x500")

root.resizable(False,False)

root._windows_set_titlebar_color("red")


#my function
def reverser():
    text = textbox1.get("1.0",customtkinter.END)
    text = text[::-1]

    textbox1.delete("1.0",customtkinter.END)
    textbox1.insert("1.0",text)



label = customtkinter.CTkLabel(master=root,text="string reverser")
label.configure(font = customtkinter.CTkFont(family="Courier",size=30,weight="bold"))
label.place(x= 250,y = 20)


textbox1 = customtkinter.CTkTextbox(master=root,width= 600)
textbox1.configure()
textbox1.place(x = 80,y = 100)

button = customtkinter.CTkButton(master=root,text="reverse",command=reverser)
button.place(x = 300,y =350)

root.mainloop()
