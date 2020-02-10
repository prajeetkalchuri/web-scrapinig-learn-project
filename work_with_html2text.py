import requests
import html2text

url = 'https://www.freecodecamp.org/learn/responsive-web-design/basic-html-and-html5/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
h = html2text.HTML2Text()
r = requests.get(url, headers=headers)
text = h.handle(r.text)

faile = open('fair_copy.txt', 'w')
faile.write(text)
faile.close()

