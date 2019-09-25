# coding:utf8
'''
Created on 2018年5月21日

@author: Ma.jian
'''
from bs4 import BeautifulSoup
import re

html_doc = '''
    <html>
  <head>
   <title>
    The Dormouse's story
   </title>
  </head>
  <body>
   <p class="title">
    <b>
     The Dormouse's story
    </b>
   </p>
   <p class="story">
    Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie" id="link1">
     Elsie
    </a>
    ,
    <a class="sister" href="http://example.com/lacie" id="link2">
     Lacie
    </a>
    and
    <a class="sister" href="http://example.com/tillie" id="link2">
     Tillie
    </a>
    ; and they lived at the bottom of a well.
   </p>
   <p class="story">
    ...
   </p>
  </body>
 </html>
'''
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf8')
print 'links'
links = soup.find_all('a')
for link in links:
    print link.name, link['href'], link.get_text()

print 'get locie links'
link_node = soup.find('a', href='http://example.com/tillie')
print link_node.name, link_node['href'], link_node.get_text()

print 'zengzepipei'
link_node = soup.find('a', href=re.compile(r"ill"))
print link_node.name, link_node['href'], link_node.get_text()

print 'focus class'
p_node = soup.find('p', class_="title")
print p_node.name, p_node.get_text()

