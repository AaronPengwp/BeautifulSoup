#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
# __Author__ Aaron


from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 创建 Beautiful Soup 对象
# 使用lxml来进行解析
soup = BeautifulSoup(html,"lxml")
# print(soup.prettify())
# print(soup.title)
# print(soup.head)
# print(soup.a)
# print(soup.p)
# print(type(soup.p))

# print(soup.name)
# print(soup.head.name)
# print(soup.p.attrs)
# print(soup.p['class'])
# print(soup.p.get('class'))
# soup.p['class'] = "newClass"
# print(soup.p)

# print(soup.p.string)
# print(type(soup.p.string))

head_tag = soup.head
# print(head_tag.contents)
# for child in head_tag.children:
    # print(child)

# for string in soup.strings:
    # print(repr(string))
#
# for string in soup.stripped_strings:
#     print(repr(string))
#     print('='*40)
#     print('>>>>'+string)


# print(soup.find_all("a",attrs={"id":"link2"}))
# print(soup.find_all("a",id='link2'))

# print(soup.select('a'))
# print(soup.select('.sister'))
# print(soup.select('#link1'))
# print(soup.select("p #link1"))
# print(soup.select("head>title"))
# print(soup.select('a[href="http://example.com/elsie"]'))

# print(type(soup.select('title')))
# print(soup.select('title')[0].get_text())

for title in soup.select('title'):
    print(title.get_text())