import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
# Импорт данных для входа в личный кабинет в формате словаря
from Get_data import data

Day = input('Введите день недели c большой буквы, домашнее которого хотите узнать: ')
Week = input("Введите 'Next', если этот день на следующей неделе: ")
Day_a_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
url = 'https://elschool.ru/Logon/Index'


def get_html(wk):
    session = requests.Session()
    response = session.post(url, data=data)
    soup_for_this_page = bs(response.text, 'html.parser')
    BS_for_this_page = soup_for_this_page.find_all('div', class_='d-flex justify-content-center')
    url_this_page = 'https://elschool.ru' + [i.find('a').get('href') for i in BS_for_this_page][0]
    if wk == 'Next':
        response2 = session.get(url_this_page).text
        url_next_week = 'https://elschool.ru' + [j.find('a').get('href') for j in
                                                 bs(response2, 'html.parser').find_all('div',
                                                                                       class_='navigation__nextweek')][
            0]
        html_dnevnik = session.get(url_next_week)
    else:
        html_dnevnik = session.get(url_this_page)
    if html_dnevnik.status_code == 200:
        return html_dnevnik.text
    else:
        print('Нет соединения')


def get_html_day():
    soup = bs(get_html(Week), 'html.parser')
    soup1 = soup.find_all('div', class_='diaries_mobile__day__lessons')[Day_a_week.index(Day)]
    lessons = bs(str(soup1), 'html.parser')
    return lessons


def get_lesson():
    lesson = [i.text for i in get_html_day().find_all('div', class_='diaries_mobile__lesson__discipline')]
    return lesson


def get_lesson_time():
    lesson_time = [i.text.replace("\r\n", '')[48:61] for i in
                   get_html_day().find_all('span', class_='diaries_mobile__lesson__time')]
    return lesson_time


def get_homework():
    homework = [i.text for i in get_html_day().find_all('div', class_='diaries-mobile__homework-text')]
    return homework


mas_data_day = list(zip(get_lesson_time(), get_lesson(), get_homework()))
# df = pd.DataFrame({
#    'Time': get_lesson_time(),
#    'Name_lesson': get_lesson(),
#    'Homework': get_homework()
# })
# df.to_excel(f'Homework_from_{Day}.xlsx')


for i in mas_data_day:
    print(i)
