import customtkinter as ctk

root = ctk.CTk()

ctk.set_appearance_mode("light")

root.title("custom unit convertor")
root.geometry("720x360")
root.resizable(False,False)

def convert():
    formula = entry.get()
    counter = 0

    if not formula:
        result.configure(text="enter the formula!")
        return
    
    for y in formula:
        
        if y.isalpha():
            if y != 'x':
                formula = formula.replace(y,"x")
            counter += 1
            
            if counter >= 2:
                result.configure(text="cannot use more than one variable!")
                return

          
        

    
    value = inp.get().strip()

    try:
        x = float(value)
    except ValueError as e:
        result.configure(text = "Enter the valid input!") 
        return    

    final_result = eval(formula)
    result.configure(text=f"the answer is :{final_result}")


ctk.CTkLabel(root,text="custom unit convertor").pack()

ctk.CTkLabel(root,text="Formula:").pack()

entry = ctk.CTkEntry(root,width=250)
entry.pack(pady = 5)

f1 = ctk.CTkLabel(root,text="value")

inp = ctk.CTkEntry(root,width=200)
f1.pack()


inp.pack(pady = 5)

b1 = ctk.CTkButton(root,text="convert",command=convert)
b1.pack()

result = ctk.CTkLabel(root,text="")
result.pack(pady=5)



root.mainloop()
