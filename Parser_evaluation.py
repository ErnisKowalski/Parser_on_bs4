import requests
from bs4 import BeautifulSoup as bs
# Импорт данных для входа в личный кабинет в формате словаря
from Get_data import data, url2
import os


def get_html():
    url = 'https://elschool.ru/Logon/Index'
    session = requests.Session()
    response = session.post(url, data=data)
    response_table = session.get(url2)
    if response_table.status_code == 200:
        return response_table.text
    else:
        print('Not found')
        print('404')


soup = bs(get_html(), 'html.parser')


def get_table():
    table = [i.text for i in soup.find_all('td', class_='grades-lesson')]
    return table


for i in get_table():
    print(i)

Lesson = input()


def get_nums(lesson):
    span = soup.find_all('tbody', attrs={'period': str(get_table().index(lesson) + 1)})
    soup1 = bs(str(span), 'html.parser')
    num = soup1.find_all('span')
    mas_num = list(map(int, [i.text for i in num]))
    return mas_num


average = sum(get_nums(Lesson)) / len(get_nums(Lesson))
get_nums(Lesson)
os.system('cls')
print(f'Предмет: {Lesson}\n'
      f'Оценки: {get_nums(Lesson)}\n'
      f'Средний балл: {average}')
