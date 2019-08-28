#!/usr/bin/python

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


#import mysql.connector

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  passwd="",
#  database="newsbg"
#)

#mycursor = mydb.cursor()
#for x in range(len(title)):
#    sql = "INSERT INTO dnesbg (title, subtitle, link, img) VALUES (%s, %s, %s, %s)"
#    val = (title[x], subtitle[x], link[x], img[x])
#    mycursor.execute(sql, val)

#    mydb.commit()

#print(mycursor.rowcount, "record inserted.")