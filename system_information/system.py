import customtkinter as ctk
import os
import sys
import platform
import psutil
from PIL import Image

Base_dir = os.path.dirname(__file__)

icon_path = os.path.join(Base_dir,'joker.ico')

  
current_os = sys.platform
#checking if system is windows or not,if it's mac or linux the below line would crash.
#the below line is necessary to make taskbar icon visible in windows.
if current_os == "win32":
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("unique id")

match current_os:
    case 'win32':
        img = Image.open(os.path.join(Base_dir,"win.png"))
    case 'darwin':
        img = Image.open(os.path.join(Base_dir,"mac.png"))
    case 'linux':
        img = Image.open(os.path.join(Base_dir,"linux.png"))    

    case _:
        print("no system is detected")
        sys.exit(1)

root = ctk.CTk()
root.geometry("920x650+10")
root.title("system information")
root.resizable(False,False)
x1 = ctk.CTkFrame(root,fg_color="#333642",width=700,height=400)
x1.pack(pady = 20)

root.iconbitmap(icon_path)

imag1 = ctk.CTkImage(light_image=img,dark_image=img,size=(150,150))
ctk.CTkLabel(x1,image=imag1,text="").pack(side="left")
ctk.CTkLabel(x1,text=f"{platform.version()}",width=500,font=ctk.CTkFont("Arial",20,"bold")).pack(padx = 40,pady = 20)
ctk.CTkLabel(x1,text=f"{platform.system()}",width=500,font=ctk.CTkFont("Arial",20,"bold")).pack(padx = 40,pady = 20)
ctk.CTkLabel(x1,text=f"{platform.node()}",width=500,font=ctk.CTkFont("Arial",20,"bold")).pack(padx = 40,pady = 20)

x2 = ctk.CTkFrame(root,fg_color="#333642",width = 700,height=400)
x2.pack(pady = 20)

memory = psutil.virtual_memory()
RAM = str(memory.total//(1024 ** 3))
freq = psutil.cpu_freq()
freq_text = f"{freq.current:.2f}" if freq else 'NA'
boot_time = psutil.boot_time()

ctk.CTkLabel(x2,text=f"{RAM} GB RAM",width=700).pack(pady=5)
ctk.CTkLabel(x2,text=os.cpu_count(),width=700).pack(pady=5)
ctk.CTkLabel(x2,text=platform.processor(),width=700).pack(pady=5)
ctk.CTkLabel(x2,text=platform.architecture()[0],width=700).pack(pady=5)
ctk.CTkLabel(x2,text=f'{freq_text}MHZ',width=700).pack(pady=5)
cpu_bar = ctk.CTkProgressBar(x2)
cpu_bar.pack(pady= 5)
cpu_stat = ctk.CTkLabel(x2,text="")
cpu_stat.pack(pady = 5)

ram_bar = ctk.CTkProgressBar(x2)
ram_bar.pack(pady = 5)
ram_Stat = ctk.CTkLabel(x2,text="")
ram_Stat.pack(pady=5)

#cpu and RAM progress bar

def updates():
    cpu_percent = psutil.cpu_percent(interval=None)
    cpu_bar.set(cpu_percent/100)
    cpu_stat.configure(text=f"{cpu_percent:.1f}%")  

    Ram_percent = memory.percent
    ram_bar.set(Ram_percent/100)
    ram_Stat.configure(text=f"{Ram_percent:1f}")
    root.after(1000,updates)

updates()

root.mainloop()