
import requests
import bs4
from bs4 import BeautifulSoup
from lxml import html, etree
from time import *

all_url = []
def get(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp
    return None

for page in range(1, 10):
    url = f"https://www.gsmarena.com/xiaomi-phones-f-80-0-p{page}.php"
    resp = get(url)
    if resp:
        soup = bs4.BeautifulSoup(resp.text, "lxml")
        makers = soup.find("div", class_="makers")
        a_all = makers.find_all("a")
        print(len(a_all))
        all_url += [f'https://www.gsmarena.com/{a["href"]}' for a in a_all]
        #time.sleep(5)

with open("all_url.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(all_url))