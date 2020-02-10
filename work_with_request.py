import requests
from bs4 import BeautifulSoup


dic_title_athour = {}
dic_cheeper_book = {}
dic_prices = {}
dic_price = {}
list_title = []
list_athour = []
list_price = []

search = input("type book name: ")
# search = 'asghar farhadi'
search = search.replace(' ', '+')
css_selector = ''
url = 'https://www.amazon.com/'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'lxml')
select_book = soup.find_all("option", value="search-alias=stripbooks-intl-ship")
select_book = str(select_book)
filed_of_search = select_book.split('"')[1]
filed_of_search = filed_of_search.split('=')[1]

new_url = url + 's?k=' + search + '&i=' + filed_of_search

r = requests.get(new_url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
title = soup.select('.a-color-base.a-text-normal')
athour = soup.select('.sg-col-12-of-28 .a-row.a-color-secondary')
title_and_price = soup.select(".a-price-whole , .a-color-base.a-text-normal")

for i in title:
    list_title.append(i.get_text())

for i in athour:
    a = i.get_text()
    a = str(a)
    a = a.replace('\n' , '')
    a = a.replace('  ', '')
    list_athour.append(a)

for i in range(len(list_title)):
    try:
        dic_title_athour[list_title[i]] = list_athour[i]
    except IndexError:
        print('some book have not athour!!')

title_and_price = list(title_and_price)

for i in title_and_price:
    a = i.get_text( )
    a = str(a)
    a = a.replace('\n' , '')
    a = a.replace('  ', '')
    list_price.append(a)


for i in list_price:
    a = i.replace('$', '')
    b = list_price.index(i)
    list_price.remove(i)
    list_price.insert(b, a)


for i in list_price:
    if i == '.' or i == '$' or i == '':
        b = list_price.index(i)
        list_price.pop(b)


for i in list_price:
    try:
        a = float(i)
        a = int(a)
        b = list_price.index(i)
        list_price.remove(i)
        list_price.insert(b, a)
    except ValueError:
        pass

for i in list_price:
    if type(i) == int and i == 0:
        list_price.remove(i)

for i in list_price:
    try:
        if type(i) == int and type(list_price[list_price.index(i)+1]) == str:
            continue
        elif type(i) == str and type(list_price[list_price.index(i)+1]) == str:
            continue
        elif type(i) == int and type(list_price[list_price.index(i)+1]) == int:
            if list_price[list_price.index(i)] < list_price[list_price.index(i)+1]:
                list_price.remove(list_price[list_price.index(i)+1])
            elif i > list_price[list_price.index(i)+1]:
                list_price.remove(i)
            else:
                list_price.remove(i)
    except IndexError:
        pass
for i in list_price:
    if i == "Paperback" and type(list_price[list_price.index(i)-1]) == int :
        list_price.remove(list_price[list_price.index(i)-1])

for i in list_price:
    try:
        if type(i) == str:
            dic_prices[i] = list_price[list_price.index(i)+1]
    except IndexError:
        pass
d = ''
try:
    d = min (dic_prices, key=lambda x: dic_prices[x])
except TypeError:
    pass
dic_price[d] = dic_prices[d]


print(dic_title_athour)
print(dic_price)
