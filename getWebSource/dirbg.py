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


for x in range(len(infoLink)):
    print(infoLink[x])
    print(infoImg[x])
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
#    sql = "INSERT INTO dirbg (title, subtitle, "https://24chasa.bg/"+link, img, site) VALUES (%s, %s, %s, %s, %s)"
#    val = (title[x], subtitle[x], link[x], img[x], "dirbg")
#    mycursor.execute(sql, val)

#    mydb.commit()

#print(mycursor.rowcount, "record inserted.")