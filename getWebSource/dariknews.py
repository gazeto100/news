#!/usr/bin/python

import requests

from bs4 import BeautifulSoup

page = requests.get('https://dariknews.bg/')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(class_='col-xs-24 visible-xs')
item = week.find_all('h2')

#print(item)

from datetime import datetime
now = datetime.now() # current date and time
time = now.strftime("%H:%M:%S / %d.%m.%y")
print("date and time:",time)

infoImg = []
infoTitle = []
infoSubTitle = []
infoLink = []

for x in range(11):
    infoLink.append(item[x].find('a').get('href'))

for x in range(11):
    infoTitle.append(item[x].find('a').get_text().strip())

for x in range(11):
    infoImg.append(item[x].find('img').get('src'))

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
    sql = "INSERT INTO dnesbg (title, subtitle, link, img, site, data) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (infoTitle[x].strip(), " ", "http:"+infoLink[x], "http:"+infoImg[x], "dariknews.bg", time)
    mycursor.execute(sql, val)

    mydb.commit()

print(mycursor.rowcount, "record inserted.")