import requests
from bs4 import BeautifulSoup
import re

def htmldelete(string, index):
    string = string.split('>')[1]
    string = string.split('<')[0]
    newstr = ""
    for i in range(len(string) - index):
        newstr += string[i + index]
    return newstr
    
def eurtomkd(string):

    string = string.replace(".", "")
    if "МКД" not in string:
        string = string.replace(" ЕУР", "")
        string = string.replace(" ", "")
        try:
            string = str(int(string) * 60) + " МКД"
        except:
            string = "No Price"
        return string
    else:
        return string

def gethref(string):
    try:
        return re.findall(r'"(.*?)"', string)[1]
    except:
        return ""

def getcity(string):
    try:
        return string.split("/")[4]
    except:
        return ""

URL = "https://www.pazar3.mk/oglasi/elektronika/delovi-za-kompjuteri-dodatoci/se-prodava"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

items = soup.find_all(class_="Link_vis")
prices = soup.find_all(class_="list-price")
links = soup.find_all("a", class_="Link_vis", href=True)

for i in range(len(prices)):
    string = str(items[i])
    string = htmldelete(string, 0)
    print(string)

    string = str(prices[i])
    string = htmldelete(string, 1)
    string = eurtomkd(string)
    string = string.replace('\n', '')
    print(string)

    string = str(links[i])
    string = gethref(string)
    print("pazar3.mk" + string)

    string = getcity(string)
    string = string.capitalize()
    print(string + '\n')
