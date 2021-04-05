#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

payload = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.111 YaBrowser/21.2.1.94 (beta) Yowser/2.5 Safari/537.36'}

""" featch element to parser """
def text_separator(user_text, user_sep):
    user_list = user_text.split(f'{user_sep}')
    user_list = list(user_list)
    return user_list

""" featch html"""
def featch_html(user_text):
    response = requests.get(f'https://beta.docs.cntd.ru/search?q={user_text}')
    if response.status_code == 200:
        print(f'\nПолучение сведений о документе: {user_text}')
    else:
        print(f'Ошибка соединения {response.status_code}')
    return response.text


""" parsers for bs4"""
def parser(user_text):
    soup = BeautifulSoup(featch_html(user_text), 'lxml')
    search_tag = soup.find_all('svg', class_='kIcon document-list_i_ic')
    if not search_tag:
        res = 'Документ не обнаружен\n'
        print(res)
    else:
        res = search_tag[0]['title']
        print(res)
    return res


if __name__ == '__main__':
    user_text = input('Введите список документов к проверке: ')
    user_separator = input(
        'Укажите разделитель по тексту вашего списка для деления на подзапросы: ')
    resalt_list = text_separator(user_text, user_separator)
    for i in resalt_list:
        parser(i)

    # parser('ГОСТ-7657849,ГОСТ 5781-82,ГОСТ 8509-93')
