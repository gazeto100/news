#!/usr/bin/python

import requests

from bs4 import BeautifulSoup

page = requests.get('https://btvnovinite.bg/')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(class_='list-wrapper')
item = week.find_all(class_='item')

print(item)

infoImg = []
infoTitle = []
infoSubTitle = []
infoLink = []

for x in range(18):
    infoLink.append(item[x].find('a').get('href'))

for x in range(18):
    infoTitle.append(item[x].find(class_='title').get_text())

for x in range(18):
    infoImg.append(item[x].find('img').get('src'))


for x in range(len(infoLink)):
    print("https://btvnovinite.bg/"+infoLink[x])
    print(infoTitle[x])
    print("http:" + infoImg[x])

#import mysql.connector

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  passwd="",
#  database="newsbg"
#)

#mycursor = mydb.cursor()
#for x in range(len(title)):
#    sql = "INSERT INTO novabg (title, subtitle, "https://24chasa.bg/"+link, img) VALUES (%s, %s, %s, %s)"
#    val = (title[x], subtitle[x], link[x], img[x])
#    mycursor.execute(sql, val)

#    mydb.commit()

#print(mycursor.rowcount, "record inserted.")