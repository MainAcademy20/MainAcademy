import requests
import bs4

def user_search():
    while True:
        user_search = input("Введіть код ЄДР для пошуку: ") # 20474912 #20113829
        if user_search.isdigit() and len(user_search) == 8:
            return user_search
        else:
            print('Неправильний формат коду ЄДР. Спробуйте ще раз.')
            continue

payload = {'edrpou': user_search()}
url = 'https://stockmarket.gov.ua/api/v1/feed-index.xml'
r = requests.get(url, params=payload)
soup = bs4.BeautifulSoup(r.text, 'xml')

params = soup.find_all('param')
for param in params:
    if param.get('name') == 'D_NAME':
        name = param.text
        break

try:
    print(name)
except NameError:
    print('Запису не знайдено.')

for link in soup.find_all('item'):
    report_url = link.get('href')
    timestamp = link.get('timestamp')

    if report_url.endswith('.txt'):
        print("Дата оприлюднення даних: ", timestamp[:10])
        print("Пряме посилання: ", report_url)
        print('Текст звіту: ')
        report_url_deep = requests.get(report_url)
        report_url_deep_detali_txt = bs4.BeautifulSoup(report_url_deep.content, 'html.parser', )
        print(report_url_deep_detali_txt)

    elif report_url.endswith('.xml'):
        print("Дата оприлюднення даних: ", timestamp[:10])
        print("Пряме посилання: ", report_url)
        print('Текст звіту: ')
        report_url_deep = requests.get(report_url)
        report_url_deep_detali_xml = bs4.BeautifulSoup(report_url_deep.content, 'xml')
        for link in report_url_deep_detali_xml.find_all('z:row'):
                content = link.get('ZMIST')
                if content != None:
                    print(content)
