import requests
from bs4 import BeautifulSoup
import re

search_t = input('type name of website: ')
url = 'http://' + search_t

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# faile = open('fair_copy.html', 'w')
# faile.write(str(soup))
# faile.close

t = soup.get_text()
Re = re.findall(r'[bootstrap]', t)
print (Re)