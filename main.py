import requests
from bs4 import BeautifulSoup


url = 'https://freelance.habr.com/tasks?q=%D0%BB%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF&categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other'


response = requests.get(url)



# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
data = soup.find_all('article', class_= 'task task_list')

# print(data)

for i in data:
    job = i.find('div', class_='task__title').text.replace("\n", "")
    price = i.find('div', class_='task__price').text.replace("\n", "")
    print(f'Задание:{job} \n Цена: {price}')



