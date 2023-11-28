
import grequests
import time

urls = [
    f'https://search.wb.ru/exactmatch/ru/male/v4/search?appType=1&curr=rub&dest=-1281648&page={i}&query=шуба&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&resultset=catalog&sort=popular&spp=22&suppressSpellcheck=false'
    for i in range(1, 61)
]

start = time.time()
rs = (grequests.get(u) for u in urls)
lst = grequests.map(rs)
products = [product for r in lst for product in r.json()['data']['products']]

print(len(products))
print(time.time() - start)
