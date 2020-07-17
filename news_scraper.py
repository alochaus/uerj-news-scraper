#!/bin/python3

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup as bs
from os import system, name

CONTENT_TEMPLATE = '%s%-25s%s'
TITLE_TEMPLATE = '%-28s%s'

def GET(url):
    try:
        with closing(get(url, stream=True)) as response:
            if HTTP_200(response):
                return response.content
            else:
                return None
    except RequestException as err:
        print('Error during requests to {0} : {1}'.format(url, str(e)))

def HTTP_200(response):
    content_type = response.headers['Content-Type'].lower()
    return (response.status_code == 200 and content_type != None and content_type.find('html') > -1)

def del_n_t(string):
    return ' '.join(string.split())

def print_title(title, website):
    print(TITLE_TEMPLATE % (title, website))

if name == 'nt':    # nt = windows
    system('cls')
else:
    system('clear')

title = 'Notícias do IME UERJ'
website = 'https://www.ime.uerj.br/'
print_title(title, website)
html = GET('https://www.ime.uerj.br/')
soup = bs(html, 'html.parser')
title = soup.find_all('div', class_='box-name')
date = soup.find_all('span', class_='entry-date')

print(' │ ')
for index in range(0, 5):
    root = ' ├ '
    if index == 4:
        root = ' └ '
    print(CONTENT_TEMPLATE % (root, date[index].string, title[index].string))
print('\n')

title = 'Notícias do BCC UERJ'
website = 'http://www.bcc.ime.uerj.br/noticias'
print_title(title, website)
html = GET('http://www.bcc.ime.uerj.br/noticias')
soup = bs(html, 'html.parser')
title = soup.select('header h2.title')
date = soup.find_all('div', class_='published')

print(' │ ')
for index in range(0, 5):
    root = ' ├ '
    if index == 4:
        root = ' └ '
    date[index].i.extract()
    print(CONTENT_TEMPLATE % (root, del_n_t(date[index].contents[1].split('Publicado: ')[1]), del_n_t(title[index].a.string)))

print('\n')
title = 'Notícias da UERJ'
website = 'https://www.uerj.br/todas-as-noticias/'
print_title(title, website)
html = GET('https://www.uerj.br/todas-as-noticias/')
soup = bs(html, 'html.parser')
title = soup.select('section.textos h1.titulo')
date = soup.select('section.textos div.entry-data')

print(' │ ')
for index in range(0, 5):
    root = ' ├ '
    if index == 4:
        root = ' └ '
    date[index].span.extract()
    date[index].span.extract()
    print(CONTENT_TEMPLATE % (root, del_n_t(date[index].contents[1]), title[index].string))

print('\n\n')
