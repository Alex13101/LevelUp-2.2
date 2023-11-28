import requests
import json


def get(url, headers=None, params=None):
    resp = requests.get(url, headers=headers, params=params)

    if resp.status_code == 200:
        return resp
    return None


if __name__ == '__main__':
    url = 'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%BA%D1%80%D0%BE%D1%81%D1%8B'
    params = {
        'appType': '1',
        'curr': 'rub',
        'dest': '-1257786',
        'query': 'кросы',
        'regions': '80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114',
        'resultset': 'catalog',
        'sort': 'popular',
        'spp': '0',
        'suppressSpellcheck': 'true'
                              'page:11'
    }
    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 112.0.0.0Safari / 537.36'
    }

    resp = get(url, headers, params)
    print(resp.text)

    # ?appType=1&curr=rub&dest=-1257786&query=%D0%BA%D1%80%D0%BE%D1%81%D1%8B&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&resultset=catalog&sort=popular&spp=0&suppressSpellcheck=false
