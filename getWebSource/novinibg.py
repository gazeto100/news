import requests

from bs4 import BeautifulSoup

page = requests.get('https://novini.bg/bylgariya')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(class_='content')
item = week.find_all('li')

#print(item)

infoImg = []
infoTitle = []
infoLink = []

for x in range(6):
    infoLink.append(item[x].find('a').get('href'))

for x in range(6):
    infoImg.append(item[x].find('img').get('src'))

for x in range(6):
    infoTitle.append(item[x].find('h3').get_text())


for x in range(len(infoLink)):
    print(infoLink[x])

for x in range(len(infoImg)):
    print(infoImg[x])

for x in range(len(infoTitle)):
    print(infoTitle[x])