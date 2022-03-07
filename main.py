# Импортируем библиотеки
import requests
import time
from config import *
from pyfiglet import Figlet


def main():
    preview_text = Figlet(font='slant') # Выбираем шрифт начального экрана
    print(preview_text.renderText('IP CHECKER')) # Вводим текст начального экрана

    ip = input('Введите IP-адресс: ') # Тут пользователь вводит IP-адресс котрый нужно проверить
    get_info_by_ip(ip=ip)

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
       
        data = {
            'Status': response.get('status'),
            'Ip': response.get('query'),
            'Country': response.get('country'),
            'Country code': response.get('countryCode'),
            'Region': response.get('region'),
            'Region name': response.get('regionName'),
            'City': response.get('city'),
            'Zip': response.get('zip'),
            'Time zone': response.get('timezone'),
            'Isp': response.get('isp'),
            'Org': response.get('org'),
            'As': response.get('as'),
            'lat ': response.get('lat'),
            'Lon ': response.get('lon')            
            }
        for k, v in data.items():
            print(f'{k} : {v}')

        time.sleep(1) # Тут идет задержка в 1 секунду
        print("-" * 10)
        print(f'{author}') # обычная переменная из файла config.py
        print("-" * 10)

    except requests.exceptions.ConnectionError:
        print('ОШИБКА | Пожалуйста, проверьте ваше соединение') # Ошибка
      
if __name__ == '__main__':
    main()
