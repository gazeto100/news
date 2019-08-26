import requests

from bs4 import BeautifulSoup

page = requests.get('https://vesti.bg/')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(class_='main-wrapper top home')
item = week.find_all(class_='gradient')

print(item)

infoImg = []
infoTitle = []
infoSubTitle = []
infoLink = []

for x in range(6):
    infoLink.append(item[x].find('a').get('href'))

for x in range(6):
    infoImg.append(item[x].find('img').get('data-original'))

for x in range(6):
    infoTitle.append(item[x].find('img').get('alt'))


for x in range(len(infoLink)):
    print(infoLink[x])

for x in range(len(infoImg)):
    print(infoImg[x])

for x in range(len(infoTitle)):
    print(infoTitle[x])


