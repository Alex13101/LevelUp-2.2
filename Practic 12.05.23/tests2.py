import requests
import time

def get_products(url):
    products = requests.get(url).json()['data']['products']
    return products

urls = [f'https://search.wb.ru/exactmatch/ru/male/v4/search?appType=1&curr=rub&dest=-1281648&page={i}&query=%D0%BA%D1%80%D0%BE%D1%81%D0%BE%D0%B2%D0%BA%D0%B8&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&resultset=catalog&sort=popular&spp=22&suppressSpellcheck=false'
        for i in range(1,61)
]
all_products =[]
start = time.time()
for url in urls:
    all_products += get_products(url)

print(time.time() - start)
print(len(all_products))
