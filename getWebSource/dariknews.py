#!/usr/bin/python

import requests

from bs4 import BeautifulSoup

page = requests.get('https://dariknews.bg/')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(class_='col-xs-24 visible-xs')
item = week.find_all('h2')

print(item)

infoImg = []
infoTitle = []
infoSubTitle = []
infoLink = []

for x in range(14):
    infoLink.append(item[x].find('a').get('href'))

for x in range(14):
    infoTitle.append(item[x].find('a').get_text())

for x in range(14):
    infoImg.append(item[x].find('img').get('src'))


for x in range(len(infoLink)):
    print("http:"+infoLink[x])
    print(infoTitle[x].strip())
    print("http:"+infoImg[x])

#import mysql.connector

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  passwd="",
#  database="newsbg"
#)

#mycursor = mydb.cursor()
#for x in range(len(title)):
#    sql = "INSERT INTO dariknews (title, subtitle, link, img) VALUES (%s, %s, %s, %s)"
#    val = (title[x], subtitle[x], link[x], img[x])
#    mycursor.execute(sql, val)

#    mydb.commit()

#print(mycursor.rowcount, "record inserted.")