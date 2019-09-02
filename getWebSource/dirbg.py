#!/usr/bin/python

import requests

from bs4 import BeautifulSoup

page = requests.get('https://dir.bg/latest-news')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find_all(class_='text-news list-article')
#item = week.find_all('li')

#print(week)

infoImg = []
infoTitle = []
infoSubTitle = []
infoLink = []

for x in range(14):
    infoLink.append(week[x].find('a').get('href'))

for x in range(14):
    infoImg.append(week[x].find('img').get('src'))

for x in range(14):
    infoTitle.append(week[x].find('a').get('title'))


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="newsbg"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT title FROM dnesbg ORDER BY id DESC LIMIT 1000")

myresult = mycursor.fetchall()

getRealNews = []
dbrec  = 0
for j in range(len(infoTitle)):
    for x in myresult:
        if x[0] == infoTitle[j]:
            print(infoTitle[j])
            dbrec = 1

    if ((dbrec != 1) and len(myresult) != 0):
        getRealNews.append(infoTitle[j])
        dbrec = 0

if (len(myresult) == 0):
    for x in range(len(infoTitle)):
        getRealNews.append(infoTitle[x])

for x in range(len(getRealNews)):
    print(getRealNews[x])

for x in range(len(getRealNews)):
    sql = "INSERT INTO dnesbg (title, subtitle, link, img, site) VALUES (%s, %s, %s, %s, %s)"
    val = (infoTitle[x], " ", infoLink[x], infoImg[x], "dir.bg")
    mycursor.execute(sql, val)

    mydb.commit()

print(mycursor.rowcount, "record inserted.")