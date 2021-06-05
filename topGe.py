import requests
from bs4 import BeautifulSoup
import sqlite3

connection  = sqlite3.connect('topGe.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS topGe(
    Rating INTEGER,
    website VARCHAR)
""")


rating = 1
for page in range(1, 6):
    request = requests.get("https://top.ge/page/" + str(page)).text
    soap = BeautifulSoup(request, 'html.parser')
    websites = soap.find_all("a", {"class":"stie_title"})
    for i in range(20):
        w = websites[i].text.strip()
        cursor.execute("""INSERT INTO topGe VALUES (?, ?)""", (rating, w))
        connection.commit()
        rating += 1

        
cursor.close()
connection.close()