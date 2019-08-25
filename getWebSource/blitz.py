import requests

from bs4 import BeautifulSoup

page = requests.get('http://blitz.bg')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='homeImportantScroll')
item = week.find_all('article')

print (item)

infoImg = []
infoTitle = []
infoLink = []

for x in range(15):
    infoLink.append(item[x].find('a').get('href'))

for x in range(15):
    infoTitle.append(item[x].find('h3').get_text())


for x in range(15):
    infoImg.append(item[x].find('img').get('src'))


for x in range(len(infoLink)):
    print(infoLink[x])

for x in range(len(infoImg)):
    print(infoImg[x])

for x in range(len(infoTitle)):
    print(infoTitle[x])

#for x in range(len(infoImg)):
#    print(infoImg[x])

#import mysql.connector

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  passwd="",
#  database="newsbg"
#)

#mycursor = mydb.cursor()
#for x in range(len(infoTitle)):
#    sql = "INSERT INTO actualnobg (title, subtitle, link, img) VALUES (%s, %s, %s, %s)"
#    val = (infoTitle[x], " ", infoLink[x], infoImg[x])
#    mycursor.execute(sql, val)

#    mydb.commit()

#print(mycursor.rowcount, "record inserted.")