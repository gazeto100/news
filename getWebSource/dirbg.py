#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import mysql.connector
from bs4 import BeautifulSoup

page = requests.get('https://dir.bg/latest-news')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(class_='main-section')
item = week.find_all(class_='img-wrapper')

#print(item)
from datetime import datetime
now = datetime.now() # current date and time
time = now.strftime("%H:%M:%S / %d.%m.%y")
print("date and time:",time)

infoImg = []
infoTitle = []
infoSubTitle = []
infoLink = []

for x in range(12):
    infoLink.append(item[x].get('href'))

for x in range(12):
    infoImg.append(item[x].find('img').get('src'))

for x in range(12):
    infoTitle.append(item[x].find('img').get('alt'))


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="newsbg",
  use_unicode=True,
  charset="utf8"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT title FROM dnesbg WHERE site = 'dir.bg' ORDER BY id DESC LIMIT 1000")

myresult = mycursor.fetchall()

getRealNews = []
getRealNewsLink = []
getRealNewsImg = []

dbrec  = 0
for j in range(len(infoTitle)):
    dbrec = 0
    for x in myresult:
        if x[0] == infoTitle[j]:
            #print(infoTitle[j])
            dbrec = 1

    if ((dbrec != 1) and len(myresult) != 0):
        getRealNews.append(infoTitle[j])
        getRealNewsLink.append(infoLink[j])
        getRealNewsImg.append(infoImg[j])
    dbrec = 0

if (len(myresult) == 0):
    for x in range(len(infoTitle)):
        getRealNews.append(infoTitle[x])
        getRealNewsLink.append(infoLink[x])
        getRealNewsImg.append(infoImg[x])

print("==============================")
for x in range(len(getRealNews)):
    print(getRealNews[x])
#    print(getRealNewsLink[x])
#    print(getRealNewsImg[x])



print(len(getRealNews))
for x in range(len(getRealNews)):
    sql = "INSERT INTO dnesbg (title, subtitle, link, img, site, data) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (getRealNews[x], " ", getRealNewsLink[x], getRealNewsImg[x], "dir.bg", time)
    mycursor.execute(sql, val)

    mydb.commit()

print(mycursor.rowcount, "record inserted.")
