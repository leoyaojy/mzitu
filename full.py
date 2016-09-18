# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import os

directory = 'full'
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
for i in range(1, 2):
    pageUrl = 'http://www.mzitu.com/page/%d' % i  # list每页url
    pageHtml = session.get(pageUrl)  # list每页html内容
    pageSoup = BeautifulSoup(pageHtml.content, 'html.parser')
    for a in pageSoup.find('ul', id='pins').find_all('a'):  # 找到list每页套图的a链接，注意:ul#pins>li里面有两个a元素，产生了重复获取
        ttUrls.append(a.get('href'))  # 获取每页套图入口链接
ttUrls = {}.fromkeys(ttUrls).keys()  # 去除重复链接

for i in ttUrls:
    picHtml = session.get(i)  # 套图入口html内容用于获取套图总页数
    picSoup = BeautifulSoup(picHtml.content, 'html.parser')
    maxPage = int(picSoup.find('div', class_='pagenavi').find_all('a')[-2].text)  # 每套图片的总数量
    picImg = picSoup.find('div', class_='main-image').find('img')  # 获取到第一张套图，用于取得名字第一张图片的链接地址
    name = picImg['alt']                    # 套图名
    picDir = os.path.join(directory, name)  # 保存套图的文件目录
    if os.path.exists(picDir):              # 创建套图保存目录及打印相关信息
        pass
    else:
        os.mkdir(picDir)
        print name.encode('utf-8') + ':下载中……'
    for p in range(1, maxPage + 1):
        detailUrl = i + '/' + str(p)  # 每张套图图片url地址
        detailHtml = session.get(detailUrl)  # 每张套图图片html内容
        detailSoup = BeautifulSoup(detailHtml.content, 'html.parser')
        imgSrc = detailSoup.find('div', class_='main-image').find('img')['src']
        print imgSrc.encode('utf-8') + ' :is downloading……'
        img = session.get(imgSrc).content
        try:
            with open(os.path.join(picDir, str(p)), 'wb') as jpg:
                jpg.write(img)
        except Exception as e:
            print e
        finally:
            jpg.close()
    print '下载完成，共%s张图片' % maxPage
