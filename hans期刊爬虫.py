from bs4 import *
import requests

a=input("输入网址：")
url=f'{a}'
headers= {'User-Agent':
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
              '/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}
response =requests.get(url=url,headers=headers)
soup = BeautifulSoup(response.text,"html.parser")

# print(soup)
title=soup.find("b",style="font-size:19px;").text
print("\033[1m"+f"标题：{title}"+"\033[0m"+"\n")

abstract=soup.find("div",id="ctl00_ContentPlaceHolder1_div_abs_zw").text
print("\033[3m"+abstract+"\033[0m"+"\n")

content=soup.find("div",id="htmlContent")
con=content.find("p","")
while con:
    print(con.get_text())
    con = con.find_next_sibling("p")

