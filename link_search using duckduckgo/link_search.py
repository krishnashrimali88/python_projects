from ddgs import DDGS
import threading
import webbrowser

def search(something,t1):
    def main():
        t1.delete('1.0','end')
        var = something
        if var is None:
            print('add something')
            return
        
        with DDGS() as d:
            result = d.text(var,max_results = 5)

            for index,res in enumerate(result,1):
                ans = res.get('href')
                wow = f'\n[{index}] {ans}'
                tag = f'{ans}'
                t1.insert('end',wow,tag)
                t1.tag_config(tag,foreground = "#ffffff",underline = True)
                t1.tag_bind(tag,'<Button-1>',lambda event,url=ans:webbrowser.open(url))
    threading.Thread(target=main,daemon=True).start()

def image_search(something,t1):
    def main():
        t1.delete('1.0','end')    
        var = something
        if var is None:
            print('add something')
            return
        
        with DDGS() as d:
            result = d.images(var,max_results = 5)

            for index,res in enumerate(result,1):
                ans = res.get('image')
                wow = f'\n[{index}] {ans}'
                tag = f'{ans}'
                t1.insert('end',wow,tag)
                t1.tag_config(tag,foreground = "#ffffff" ,underline = True)
                t1.tag_bind (tag,'<Button-1>',lambda event,url= ans:webbrowser.open(url))

    threading.Thread(target=main,daemon=True).start()        
