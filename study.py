#encoding=utf-8
from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import urllib
import os

c=[]
local="D:\\Download"
url = "https://www.24tupian.com/"
html = requests.get(url)
f = BeautifulSoup(html.content,"lxml")
for k in f.find_all('img') :
    #print str(k)
    d = str(k).split('\"')
    c.append(d[3])
print c
print "开始下载"
x = 1
for i in c:
    try:
        urllib.urlretrieve(i,'D:\\Download\\%s.jpg'%x)
        print('***** ' + i + ' *****' + '   Downloading...')
        x=x+1
    except Exception as e:
        continue
print "the end"
