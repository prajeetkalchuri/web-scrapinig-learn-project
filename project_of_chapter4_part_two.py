import requests
from bs4 import BeautifulSoup
from lxml import etree

url = 'https://www.amazon.com/s?k=shoe&i=fashion-mens-intl-ship&ref=nb_sb_noss_2'
header = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'accept-encoding': 'gzip, deflate, br',
          'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
          'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
          'sec-fetch-user': '?1'}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

# fair_copy = open('fair_copy.html', 'w')
# fair_copy.write(str(soup))
# fair_copy.close

link_of_some_shoe = soup.select_one('.index\=10 .a-text-normal')
print('------------------------------')
link_of_some_shoe = link_of_some_shoe['href']
link_of_some_shoe = str(link_of_some_shoe)
sp = link_of_some_shoe.split('/ref')
for i in sp:
    print(i)


header2 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'accept-encoding': 'gzip, deflate, br',
          'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
          'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
          'sec-fetch-user': '?1'}

shoe_link = 'https://www.amazon.com' + sp[0]

response2 = requests.get(url, headers=header2)
soup2 = BeautifulSoup(response2.text, 'html.parser')

fair_copy = open('fair_copy2.txt', 'w')
fair_copy.write(str(soup2))
fair_copy.close
