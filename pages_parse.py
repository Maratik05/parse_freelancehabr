import requests
from bs4 import BeautifulSoup
import sqlite3


con = sqlite3.connect('orders.db')
cursor = con.cursor()

cursor.execute("""CREATE TABLE orders(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               zakaz VARCHAR(300),
               price INTEGER)""")


for count in range(1,52):
    url = f'https://freelance.habr.com/tasks?page={count}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('article', class_= 'task task_list')
    for i in data:
        job = i.find('div', class_='task__title').text.replace("\n", "")
        price = i.find('div', class_='task__price').text.replace("\n", "")
        # print(f'Задание:{job} \n Цена: {price}')
        cursor.execute("""
            INSERT INTO orders (zakaz, price) VALUES (?, ?)
            """, (job, price))
        
        con.commit()
con.close()


        

            
            

