#!/usr/bin/python

import requests

from bs4 import BeautifulSoup

page = requests.get('http://dnes.bg')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(class_='homepage')
dnesitem = week.find_all(class_='news-item')

#print(dnesitem)

from datetime import datetime
now = datetime.now() # current date and time
time = now.strftime("%H:%M:%S / %d.%m.%y")
print("date and time:",time)

infoImg = []
infoTitle = []
infoSubTitle = []
infoLink = []


for x in range(10):
    infoTitle.append(dnesitem[x].find('span').get_text())
    infoImg.append(dnesitem[x].find('img').get('src'))
    infoLink.append(dnesitem[x].find('a').get('href'))
    infoSubTitle.append(dnesitem[x].find(class_='news-subtitle').get_text())



#for x in range(len(infoTitle)):
#    print(infoTitle[x])

#for x in range(len(infoLink)):
#    print("https://dnes.bg/"+infoLink[x])

#for x in range(len(infoImg)):
#    print(infoImg[x])


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="newsbg"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT title FROM dnesbg WHERE site = 'dnes.bg' ORDER BY id DESC LIMIT 1000")

myresult = mycursor.fetchall()

getRealNews = []
dbrec  = 0
for j in range(len(infoTitle)):
    for x in myresult:
        if x[0] == infoTitle[j]:
            #print(infoTitle[j])
            dbrec = 1
            break

    if ((dbrec != 1) and len(myresult) != 0):
        getRealNews.append(infoTitle[j])
        #print(infoTitle[j])
    dbrec = 0

if (len(myresult) == 0):
    for x in range(len(infoTitle)):
        getRealNews.append(infoTitle[x])

for x in range(len(getRealNews)):
    print(getRealNews[x])

for x in range(len(getRealNews)):
    sql = "INSERT INTO dnesbg (title, subtitle, link, img, site, data) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (infoTitle[x], " ", 'https://dnes.bg'+infoLink[x], infoImg[x], "dnes.bg", time)
    mycursor.execute(sql, val)

    mydb.commit()

print(mycursor.rowcount, "record inserted.")

