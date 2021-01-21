import requests
from bs4 import BeautifulSoup
import csv


# 1.Кількість сторінок
# 2.Згенеруват url
# 3.Зібрати дані

# https://rst.ua/oldcars/?task=newresults&make%5B%5D=0&year%5B%5D=0&year%5B%5D=0&price%5B%5D=0&price%5B%5D=0&engine%5B%5D=0&engine%5B%5D=0&gear=0&fuel=0&drive=0&condition=0&from=sform
# start = 1
# url - https://rst.ua/oldcars/?task=newresults&start=1


def get_html(url):
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('test_rst.csv', 'a') as f:
        #         order = []
        writer = csv.writer(f)
        writer.writerow((data['title'],
                         data['url'],
                         data['price_uah'],
                         data['price_usd'],
                         data['year'],
                         data['mileage'],
                         data['engine'],
                         data['engine_type'],
                         data['gearbox'],
                         data['region'],
                         data['status'],
                         data['info_about_car'],)
                        )


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination')


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = (soup.find('div', class_='rst-page-wrap').find_all('div', class_='rst-ocb-i rst-ocb-i-premium rst-uix-radius ')
          + soup.find('div', class_='rst-page-wrap').find_all('div',
            class_='rst-ocb-i rst-ocb-i-premium rst-uix-radius rst-ocb-i-crash')
          + soup.find('div', class_='rst-page-wrap').find_all('div',
            class_='rst-ocb-i rst-ocb-i-premium rst-uix-radius rst-ocb-i-blue'))

    #     all_cars = ts + tss
    for td in ts:
        try:
            title = td.find('h3', class_='rst-ocb-i-h').find('span').text[7:].strip()
            print(title)
        except:
            title = ''
        try:
            url = 'https://rst.ua' + td.find('a', class_='rst-ocb-i-a').get('href')
            print(url)
        except:
            url = ''
        try:
            price_uah = 'Price in UAH - ' + td.find('span', class_='rst-ocb-i-d-l-i-s rst-ocb-i-d-l-i-s-p').text.strip()
            print(price_uah)
        except:
            price_uah = ''
        try:
            price_usd = 'Price in USD - ' + td.find('span', class_='rst-uix-grey').text.strip()
            print(price_usd)
        except:
            price_usd = ''
        #         try:
        #             price_together = 'Year - ' + td.find('li',class_ = 'rst-ocb-i-d-l-i').text.strip()
        #             print(price_together)
        #         except:
        #             price_together = ''
        try:
            year = 'Year - ' + td.find('div', class_='rst-ocb-i-d').find('ul', class_='rst-ocb-i-d-l').findAll('li',
            class_='rst-ocb-i-d-l-i')[1].find('span', class_='rst-ocb-i-d-l-i-s').text.strip()
            print(year)
        except:
            year = ''
        try:
            mileage = 'Mileage - ' + \
                      td.find('div', class_='rst-ocb-i-d').find('ul', class_='rst-ocb-i-d-l').findAll('li',
            class_='rst-ocb-i-d-l-i')[1].text[10:].strip()
            print(mileage)
        except:
            mileage = ''
        try:
            engine = 'Engine - ' + td.find('div', class_='rst-ocb-i-d').find('ul', class_='rst-ocb-i-d-l').findAll('li',
            class_='rst-ocb-i-d-l-i')[2].find('span', class_='rst-ocb-i-d-l-i-s').text.strip()
            print(engine)
        except:
            engine = ''
        try:
            engine_type = 'Engine type - ' + \
                          td.find('div', class_='rst-ocb-i-d').find('ul', class_='rst-ocb-i-d-l').findAll('li',
            class_='rst-ocb-i-d-l-i')[2].text[10:17].strip()
            print(engine_type)
        except:
            engine_type = ''
        try:
            gearbox = 'Gearbox - ' + \
                      td.find('div', class_='rst-ocb-i-d').find('ul', class_='rst-ocb-i-d-l').findAll('li',
            class_='rst-ocb-i-d-l-i')[2].findAll('span', class_='rst-ocb-i-d-l-i-s')[1].text.strip()
            print(gearbox)
        except:
            gearbox = ''
        try:
            region = 'Region - ' + td.find('li', class_='rst-ocb-i-d-l-j').find('span',
            class_='rst-ocb-i-d-l-i-s').text.strip()
            print(region)
        except:
            region = ''
        try:
            status = 'Status - ' + td.find('div', class_='rst-ocb-i-d').find('ul', class_='rst-ocb-i-d-l').findAll('li',
            class_='rst-ocb-i-d-l-j')[1].find('span', class_='rst-ocb-i-d-l-i-s').text.strip()
            print(status)
        except:
            status = ''
        try:
            date = 'Date - ' + td.find('div', class_='rst-ocb-i-s').text.strip()
            #             split or re
            print(date)
        except:
            date = ''
        try:
            info_about_car = td.find('div', class_='rst-ocb-i-d-d').text.strip()
            print(info_about_car)
        except:
            info_about_car = ''
        print()
        data = {
            'title': title,
            'url': url,
            'price_uah': price_uah,
            'price_usd': price_usd,
            'year': year,
            'mileage': mileage,
            'engine': engine,
            'engine_type': engine_type,
            'gearbox': gearbox,
            'region': region,
            'status': status,
            'info_about_car': info_about_car
        }

    write_csv(data)


def main():
    #     https://rst.ua/oldcars/?task=newresults&make%5B%5D=0&year%5B%5D=0&year%5B%5D=0&price%5B%5D=0&price%5B%5D=0&engine%5B%5D=0&engine%5B%5D=0&gear=0&fuel=0&drive=0&condition=0&from=sform
    #     url = "https://rst.ua/oldcars/?task=newresults&start=1"
    base_url = 'https://rst.ua/oldcars/?task=newresults&make%5B%5D=0&year%5B%5D=0&year%5B%5D=0&price%5B%5D=0&price%5B%5D=0&engine%5B%5D=0&engine%5B%5D=0&gear=0&fuel=0&drive=0&condition=0&from=sform'
    page_part = '&start='
    for i in range(1, 17503):
        url_gen = base_url + page_part + str(i)
        print('-------------------------------------------------')
        print(url_gen)

        html = get_html(url_gen)
        get_page_data(html)


if __name__ == '__main__':
    main()