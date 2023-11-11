import requests
from bs4 import BeautifulSoup as bs
name_company = []
links = []
k = 0
r = 0
url = 'https://www.proff.no/søk-etter-bransje/entreprenører/I:441/?q=Entreprenører'
mas_links = [url]
html = requests.get(url)
soup = bs(html.text,'lxml')
name = soup.find_all('a',class_='addax addax-cs_hl_hit_company_name_click')
name_company = [i.text for i in name]
name_company.pop(0)
links_company = []
print(name_company)
name_company.pop(0)
print(name_company)
while k < 399:
    html = requests.get(url).text
    soup = bs(html, 'lxml')
    href  = soup.find_all('li', class_='next')
    new_url = [i.find('a').get('href') for i in href]
    url = 'https://www.proff.no'+new_url[0]
    mas_links.append(url)
    k += 1

while r < 400:
    html1 = requests.get(mas_links[r]).text
    soup = bs(html1, 'lxml')
    name = soup.find_all('a', class_='addax addax-cs_hl_hit_company_name_click')

    link = [i.get('href') for i in name]
    links.append(i for i in link)
    name_com = [i.text for i in name]
    print(link)
    name_company.append(i for i in name_com)
    r += 1
