# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import os

directory = 'single'
if os.path.exists(directory):
    pass
else:
    os.mkdir(directory)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'
}
session = requests.session()
session.headers.update(headers)
ttUrls = []
# 获取每页的套图入口链接
for i in range(1, 5):
    pageUrl = 'http://www.mzitu.com/page/%d' % i  # list每页url
    pageHtml = session.get(pageUrl)  # list每页html内容
    pageSoup = BeautifulSoup(pageHtml.content, 'html.parser')
    for a in pageSoup.find('ul', id='pins').find_all('a'):  # 找到list每页套图的a链接，注意:ul#pins>li里面有两个a元素，产生了重复获取
        ttUrls.append(a.get('href'))  # 获取每页套图入口链接
ttUrls = {}.fromkeys(ttUrls).keys()  # 去除重复链接

for i in ttUrls:
    picHtml = session.get(i)
    picSoup = BeautifulSoup(picHtml.content, 'html.parser')
    picImg = picSoup.find('div', class_='main-image').find('img')  # 获取到第一张套图，用于取得名字第一张图片的链接地址
    picUrl = picImg['src']                  # 获取图片链接
    print picUrl.encode('utf-8') + ' :is downloading……'
    img = session.get(picUrl).content
    try:
        with open(os.path.join(directory, str(i.split('/')[-1])), 'wb') as jpg:
            jpg.write(img)
    except Exception as e:
        print e
    finally:
        jpg.close()