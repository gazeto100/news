#!/usr/bin/python

import requests

from bs4 import BeautifulSoup

page = requests.get('https://nova.bg/news')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(class_='row')
item = week.find_all(class_='media-cont')

#print(item)

from datetime import datetime
now = datetime.now() # current date and time
time = now.strftime("%H:%M:%S / %d.%m.%y")
print("date and time:",time)

infoImg = []
infoTitle = []
infoSubTitle = []
infoLink = []

for x in range(8):
    infoLink.append(item[x].find('a').get('href'))

for x in range(8):
    infoTitle.append(item[x].find('img').get('alt'))

for x in range(8):
    infoImg.append(item[x].find('img').get('src'))


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="newsbg",
  use_unicode=True,
  charset="utf8"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT title FROM dnesbg WHERE site = 'nova.bg' ORDER BY id DESC LIMIT 1000")

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
        #print(infoTitle[j])
    dbrec = 0

if (len(myresult) == 0):
    for x in range(len(infoTitle)):
        getRealNews.append(infoTitle[x])
        getRealNewsLink.append(infoLink[x])
        getRealNewsImg.append(infoImg[x])

print("==============================")
for x in range(len(getRealNews)):
    print(getRealNews[x] + " = " + infoTitle[x])
#    print('https://dnes.bg'+getRealNewsLink[x] + " = " + 'https://dnes.bg'+infoLink[x])
#    print(getRealNewsImg[x] + " = " + infoImg[x])




for x in range(len(getRealNews)):
    sql = "INSERT INTO dnesbg (title, subtitle, link, img, site, data) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (getRealNews[x], " ", getRealNewsLink[x], getRealNewsImg[x], "nova.bg", time)

    mycursor.execute(sql, val)

    mydb.commit()

print(mycursor.rowcount, "record inserted.")
