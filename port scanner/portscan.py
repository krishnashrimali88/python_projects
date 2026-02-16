import customtkinter
import joy
import threading
from pynput import keyboard


root = customtkinter.CTk()

root.geometry("500x350")

root.title("Port Scanner")

root.resizable(False,False)

stop_scan = False

def on_key_press(key):
    global stop_scan
    try:
        if key.char == 'q':
            stop_scan = True
            textbox1.insert(customtkinter.END,"\n stopped by user\n")   
    except AttributeError:
        pass


def work():
    global stop_scan
    stop_scan = False

    target = entry.get()

    if not target:
        textbox1.insert(customtkinter.END,"Please enter ip addr")
        return

    textbox1.delete("1.0",customtkinter.END)
    textbox1.insert(customtkinter.END,f"scanning{target}\n")

    button.configure(state="disabled",text="scanning...")

    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()


    def scan():
        global stop_scan
        try:
            for port in range(1,200):
                if stop_scan:
                    break

                result = joy.portscan(target,port)

                if result:
               
                    textbox1.insert(customtkinter.END,f"\nport{port} is opened\n")
                    textbox1.see(customtkinter.END)
                else:
             
                    textbox1.insert(customtkinter.END,f"\nport{port} is closed\n")  
                    textbox1.see(customtkinter.END)


        except:
            print("error")

        finally:
            listener.stop()
            button.configure(state="normal",text="scan")
            textbox1.insert(customtkinter.END,"\nscan complete\n")

    thread = threading.Thread(target=scan,daemon=True)
    thread.start()

label = customtkinter.CTkLabel(master=root,text="Port scanner")
label.configure(width = 30,height = 20,font = customtkinter.CTkFont(weight="bold",size=22))
label.pack(pady=12,padx=10)

label1 = customtkinter.CTkLabel(master=root,text="Target:-")
label1.configure(width = 30,height = 20,font = customtkinter.CTkFont(weight="bold",size=20))
label1.place(x= 24,y = 60)

entry = customtkinter.CTkEntry(master=root,placeholder_text="Target ip address")
entry.configure(width=200)
entry.place(x  = 120,y = 60)

button = customtkinter.CTkButton(master=root,text="Enter",command=work)
button.place(x = 340,y = 60)

textbox1 = customtkinter.CTkTextbox(master=root,width=300)
textbox1.place(x = 110,y = 110)




root.mainloop()
