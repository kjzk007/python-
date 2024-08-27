# 在网站使用：http://www.cisszgty.com/tykj

from bs4 import *
import requests
import urllib.request
import re

def geturl(htmlurl):
    pattern = r'href="([^"]+)"'
    link=re.findall(pattern,str(htmlurl))
    return link

url='http://www.cisszgty.com/tykx/2024/channel/1/'
headers= {'User-Agent':
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
              'AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'}
response=requests.get(url=url,headers=headers)
soup = BeautifulSoup(response.text,"html.parser")
ol=soup.findAll('ol',class_="directory-list")

for i in range(10):
    dir=r'D:\A_pan_download\test'
    url=f'{geturl(ol)[i]}'
    headers= {'User-Agent':
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'}
    response=requests.get(url=url,headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")

    title=soup.find('div',class_="article-title")
    title2=title.find('h2').text
    print(title2+"下载中...")

    position=soup.find_all('strong')

    d_url=geturl(position)[0]
    urllib.request.urlretrieve(d_url, dir+fr"\{title2}.pdf")