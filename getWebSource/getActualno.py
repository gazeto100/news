import requests

from bs4 import BeautifulSoup

page = requests.get('http://actualno.bg')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(class_='wrap')
item = week.find_all(class_='right')

print (item)

infoItem = []

#for x in range(7):
infoItem.append(item[0].find('a').get('data-image'))
infoItem.append(item[0].find('a').get('href'))
infoItem.append(item[0].find('a').get('title'))

print(infoItem[0])
print(infoItem[1])
print(infoItem[2])
