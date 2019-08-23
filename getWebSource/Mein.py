import requests

from bs4 import BeautifulSoup

page = requests.get('http://dnes.bg')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(class_='homepage')
item = week.find_all(class_='first')
#print(item)

link = item[0].find('a').get('href')
link1 = item[1].find('a').get('href')

title = item[0].get_text()
title1 = item[1].get_text()

img = item[0].find('img').get('src')
img1 = item[1].find('img').get('src')

#print(title.strip())
#print(title1.strip())

#print('https://dnes.bg'+link)
#print('https://dnes.bg'+link1)

#print(img)
#print(img1)

img_title_1 = []

dnesitem = week.find_all(class_='news-item')
#print(dnesitem)

for x in range(10):
    img_title_1.append(dnesitem[x].find('span').get_text())
    img_title_1.append(dnesitem[x].find('img').get('src'))
    img_title_1.append(dnesitem[x].find('a').get('href'))
    img_title_1.append(dnesitem[x].find(class_='news-subtitle').get_text())

for x in range(len(img_title_1)):
    print(img_title_1[x])
