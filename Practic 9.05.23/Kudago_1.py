import requests
import bs4
from bs4 import BeautifulSoup
from lxml import html, etree


def get(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp
    return None

if __name__ == '__main__':

    url = 'https://www.wildberries.ru/catalog/0/search.aspx?page=6&sort=popular&search=%D0%BA%D1%80%D0%BE%D1%81%D1%8B'

    resp = get(url)

    text = resp.text

    print(resp.status_code)
    print(resp.text)

    # with open("kudago.html", "w", encoding="utf-8") as f:
    #
    #      f.write(resp.text)


    # soup = bs4.BeautifulSoup(text, "lxml")
    #
    # feed_child = soup.find("div", class_="feed-child")
    # post_content = feed_child.find_all('a',class_='post-title-link')
    # print(len(post_content))
    #
    # post_title_link = feed_child.find_all("a", class_="post-title-link")
    #
    # urls = [a["href"] for a in post_title_link]
    #
    # print(len(post_title_link))
    #
    # print(*urls, sep="\n")