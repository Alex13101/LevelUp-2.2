from lxml import html, etree

xml = """
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book category="cooking">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="children">
    <title lang="en">Harry Potter</title>
    <author>J.K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  </bookstore>
"""

tree = etree.fromstring(xml)

books = tree.xpath('//book')
for book in books:
    print(etree.tostring(book, encoding='unicode'))

categories = tree.xpath('//book/@category')
for category in categories:
    print(category)

new_book = etree.Element('book')
new_book.set('category', 'fiction')
