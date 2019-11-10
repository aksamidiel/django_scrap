import requests
from bs4 import BeautifulSoup


def get_html(url):
    resp = requests.get(url)  # запрос на url
    return resp.text


def get_data(html):  # функция парсинга  _> передача для распарсиравания в beautifulsoup
    soup = BeautifulSoup(html, 'lxml')
    headers_lev_1 = soup.find('div', id='home-welcome').find('header').find('h1').text
    return headers_lev_1


def main():
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))  # вывели html код страницы


if __name__ == '__main__':
    main()
