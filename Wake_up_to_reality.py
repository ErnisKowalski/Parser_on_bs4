import requests
from bs4 import BeautifulSoup as bs

url = 'https://wallpaperscraft.ru'
response = requests.get(url).text
soup_by_catalog = bs(response, 'html.parser')
filters = [i.find('a').get('href') for i in soup_by_catalog.find_all('li', class_='filter')][0:27]
name_filters_and_num = [i.text.replace('\n', '')[14:] for i in soup_by_catalog.find_all('a', class_='filter__link')][
                       0:27]
name_filters = []
for j in name_filters_and_num:
    result = ''.join([i for i in j if not i.isdigit()])
    name_filters.append(result)


name_filters[0] = '3D'
for h in name_filters:
    print(h)

catalog = input()
page = 1
mas_src = []
while page <= 10:
    URL_catalog = url + filters[name_filters.index(catalog)] + '/1920x1080/page' + str(page)
    response_by_image = requests.get(url=URL_catalog).text
    soup_by_src = bs(response_by_image, 'html.parser')
    src_by_page = [i.find('img').get('src') for i in soup_by_src.find_all('span', class_='wallpapers__canvas')]
    for j in src_by_page:
        h = j.replace('300x168', '1920x1080')
        mas_src.append(h)
    page += 1



for number in range(140):
    response_by_src = requests.get(mas_src[number]).content
    with open(f'Foto/{number}.jpg', 'wb') as file:
        file.write(response_by_src)


