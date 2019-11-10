import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text


# функция получающая строку и преобразующаяя ее к нормальному виду
def refind(s):
    r = s.split(' ')[0]  # делим по пробелу
    res = r.replace(',', '')
    return res


def write_csv(data):  # функция записи в файл
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['rating']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[1]
    plugins = popular.find_all('article')  # список артиклей со страницы

    for plugin in plugins:
        name = plugin.find('h2').text
        url = plugin.find('h2').find('a').get('href')
        rat = plugin.find('span', class_='rating-count').find('a').text
        rating = refind(rat)
        # print(rating)

        data = {'name': name,
                'url': url,
                'rating': rating}
        # print(data)

        write_csv(data)

    return plugins


def main_2():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main_2()
