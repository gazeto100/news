import requests

from bs4 import BeautifulSoup

page = requests.get('https://24chasa.bg/')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(class_='new-slider-container')
item = week.find_all('li')

print(item)

infoImg = []
infoTitle = []
infoSubTitle = []
infoLink = []

for x in range(12):
    infoLink.append(item[x].find('a').get('href'))

for x in range(12):
    if x < 4:
        infoImg.append(item[x].find('img').get('src'))
    else:
        infoImg.append(item[x].find('img').get('data-img'))



for x in range(len(infoLink)):
    print(infoLink[x])

for x in range(len(infoImg)):
    print(infoImg[x])
