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
            'IP >': response.get('query'),
            'INT PROV >': response.get('isp'),
            'ORG >': response.get('org'),
            'COUNTRY >': response.get('country'),
            'REGION NAME >': response.get('regionName'),
            'CITY >': response.get('city'),
            'ZIP >': response.get('zip'),
            'LAT >': response.get('lat'),
            'LON >': response.get('lon'),
        }
        for k, v in data.items():
            print(f'{k} : {v}')

        time.sleep(1) # Тут идет задержка в 1 секунду
        print(f'{author}') # обычная переменная из файла config.py
 
    except requests.exceptions.ConnectionError:
        print('ОШИБКА | Пожалуйста, проверьте ваше соединение') # Ошибка
      
if __name__ == '__main__':
    main()