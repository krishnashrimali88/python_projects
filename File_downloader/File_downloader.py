import requests
import urllib3
import customtkinter as ctk
import threading
import os


urllib3.disable_warnings()

def download():
    def run():
        link = url.get()
        filename = file_name.get()
    

        if not link:
            root.after(0, lambda: toast(root, "please add link", "error"))
            return

        if not filename:
            root.after(0, lambda: toast(root, "please add filename", "error"))
            return  

    
        downloaded  = 0
        headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        direct = os.path.dirname(os.path.abspath(__file__))
        locate = os.path.join(direct,filename)
        try:
            with requests.get(link,stream=True,headers=headers,verify=False) as response:
                response.raise_for_status()
                total = int(response.headers.get('content-length',0))


                with open(locate,'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            file.write(chunk)    
                            downloaded += len(chunk)
                            if total > 0:
                                percent = (downloaded/total) * 100
                                percent_final = percent / 100
                                bar.set(percent_final)
                                per.configure(text=f'{percent}%')
                                root.after(0,bar.set,percent_final)
                           
            root.after(0, lambda: toast(root, "done", "success"))

        except requests.exceptions.MissingSchema:
            root.after(0, lambda: toast(root, "invalid url", "error"))

        except requests.exceptions.ConnectionError:
            root.after(0, lambda: toast(root, "connection error", "error"))

        except requests.exceptions.HTTPError as e:
            root.after(0, lambda: toast(root, f"HTTP eror{e}", "error"))

        except Exception as e:
            root.after(0, lambda: toast(root, e, "error"))

    threading.Thread(target=run,daemon=True).start()      

def toast(app,message,type="success",duration = 3000):
    colors = {
        "success": ("#2d6a4f", "✓ "),
        "error":   ("#9b2226", "✕ "),
    }

    bg,icon = colors.get(type,colors["success"])
    toast = ctk.CTkFrame(app,fg_color=bg,corner_radius=10)
    ctk.CTkLabel(toast,text= icon + message,text_color="white",font=ctk.CTkFont(size=13)).pack(pady= 14,padx = 10)
    toast.place(relx=1.0,rely=1.0,x= -20 ,y = -20,anchor="se")
    toast.lift()
    root.after(duration,toast.destroy)



root = ctk.CTk()
root.title("File_Downloader")
root.geometry("720x520")

ctk.CTkLabel(root,text="File Downloader").pack()

url = ctk.CTkEntry(root)
url.pack(pady = 10)
file_name = ctk.CTkEntry(root)
file_name.pack(pady = 10)

ctk.CTkButton(root,text="download",command=download).pack(pady = 10)


bar = ctk.CTkProgressBar(root)
bar.pack(pady = 10)
bar.set(0)

per = ctk.CTkLabel(root,text="0%")
per.pack(pady = 10)

root.mainloop()

