#!/usr/bin/python

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

#print(link)
#print(link1)

#print(img)
#print(img1)

infoImg = []
infoTitle = []
infoSubTitle = []
infoLink = []

dnesitem = week.find_all(class_='news-item')
#print(dnesitem)

for x in range(10):
    infoTitle.append(dnesitem[x].find('span').get_text())
    infoImg.append(dnesitem[x].find('img').get('src'))
    infoLink.append(dnesitem[x].find('a').get('href'))
    infoSubTitle.append(dnesitem[x].find(class_='news-subtitle').get_text())



for x in range(len(infoTitle)):
    print(infoTitle[x])

for x in range(len(infoLink)):
    print("https://dnes.bg/"+infoLink[x])

for x in range(len(infoImg)):
    print(infoImg[x])


#import mysql.connector

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  passwd="",
#  database="newsbg"
#)

#mycursor = mydb.cursor()
#for x in range(len(title)):
#    sql = "INSERT INTO dnesbg (title, subtitle, "https://dnes.bg/"+link, img, site) VALUES (%s, %s, %s, %s, %s)"
#    val = (title[x], subtitle[x], link[x], img[x], "dnes")
#    mycursor.execute(sql, val)

#    mydb.commit()

#print(mycursor.rowcount, "record inserted.")

