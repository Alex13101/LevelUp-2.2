
from bs4 import BeautifulSoup




html = """
<html>
  <head>
    <title>Мой сайт</title>
  </head>
  <body>
    <h1>Добро пожаловать на мой сайт!</h1>
    <p>Это первый абзац.</p>
    <p>Это второй абзац.</p>
    <a href="http://example.com">Ссылка</a>
  </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')


title = soup.title
print(title.text) # Мой сайт


paragraphs = soup.find_all('p')
for p in paragraphs:
  print(p.text)
# Это первый абзац.
# Это второй абзац.


link = soup.find('a')
print(link['href']) # http://example.com

print(link.text) # Ссылка