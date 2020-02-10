import requests
from bs4 import BeautifulSoup

# search_text = input('what are you looking for? ')
search_text = 'python'
url = 'https://www.google.com/search?q=' + search_text
header = {'accept-encoding': 'gzip, deflate, br',
          'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
          'user-agent': 'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_14_6) AppleWebKit/537.36(KHTML, like Gecko)Chrome/80.0.3987.87 Safari/537.36'}

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# fair_copy = open('fair_copy.html', 'w')
# fair_copy.write(str(soup))
# fair_copy.close

title_of_results = soup.select('.rc .r')
# title_of_results = soup('div',{'class':"kCrYT"})
print(type(title_of_results))
for i in title_of_results:
    print(i.a['href'])
print(len(title_of_results))