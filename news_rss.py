import requests
from bs4 import BeautifulSoup

#must end with xml 
url = ""

response = requests.get(url)

soup = BeautifulSoup(response.content,features="xml")

items = soup.find_all("item")

for i,item in enumerate(items,start=1):
    print(f"{i}.{item.title.text}")

