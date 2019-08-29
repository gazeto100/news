#!/usr/bin/python

import requests

from bs4 import BeautifulSoup

page = requests.get('http://blitz.bg')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='home-top-news')
item = week.find_all('article')

#print(week)

infoImg = []
infoTitle = []
infoLink = []

for x in range(20):
    infoLink.append(item[x].find('a').get('href'))

for x in range(20):
    infoImg.append(item[x].find('img').get('src'))

for x in range(20):
    infoTitle.append(item[x].find('img').get('alt'))


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
#    sql = "INSERT INTO dnesbg (title, subtitle, link, img, site) VALUES (%s, %s, %s, %s, %s)"
#    val = (title[x], subtitle[x], link[x], img[x], "blitz")
#    mycursor.execute(sql, val)

#    mydb.commit()

#print(mycursor.rowcount, "record inserted.")