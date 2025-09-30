# to store hyperlink and used them


link:list = []

def add_link() -> None:
    try:
        y = str(input("Enter the input"))
        link.append(y)
    except TypeError as e:
        print(e)

def show_All_links() -> None:
    length:int = len(link)
    length:int = length - 1
    i:int = 0
    try:
        while length != -1:
            url:str = link[i]
            link_text = f"Click here to visit {url}"
            print(f"\033]8;;{url}\033\\{link_text}\033]8;;\033\\")
            length -= 1
            i += 1
    except:
        print("error is")




