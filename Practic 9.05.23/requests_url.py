

import requests

def get(url):
    resp = requests.get(url)


    if resp.status_code == 200:
        return resp
    return None

if __name__ == '__main__':
    resp = get('https://fdn2.gsmarena.com/vv/bigpic/xiaomi-poco-m5.jpg')
    print(resp.status_code)
    with open("picture.png", "wb") as f:
        f.write(resp.content)



