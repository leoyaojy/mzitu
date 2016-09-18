# coding:utf-8
from bs4 import BeautifulSoup
import requests
import os

directory = 'page'
if os.path.exists(directory):
    pass
else:
    os.mkdir(directory)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'
}
session = requests.session()
session.headers.update(headers)
for i in range(1, 5):
    url = 'http://www.mzitu.com/page/%d' % i
    html = session.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    for j in soup.find('ul', id='pins').find_all('img'):
        imgSrc = j.get('data-original')
        name = os.path.basename(imgSrc).split('_')[0]
        print imgSrc+' : is downloading'
        img = session.get(imgSrc)
        try:
            with open(os.path.join(directory,name),'wb') as jpg:
                jpg.write(img.content)
        except Exception as e:
            print e
        finally:
            jpg.close()