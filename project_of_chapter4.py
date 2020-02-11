import requests
from bs4 import BeautifulSoup
from lxml import etree
from requests_html import HTMLSession
from selenium import webdriver
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError



# url = input('what is your url: ')
url = 'http://www.dsit.org.ir/?cmd=page&Cid=92&title=Kontakt&lang=fa'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tag_a = soup.find_all('a')

# for i in tag_a:
#     print(i.text)


tag_iframe = soup.find('iframe')
# print(type(tag_iframe))
# print(tag_iframe['src'])
# print(tag_iframe)
print('-----------')
new_url = tag_iframe['src']
response = requests.get(new_url)
new_soup = BeautifulSoup(response.text, 'lxml')
# print(new_soup)
scr_tag = new_soup.find('script')
scr_tag = str(scr_tag)
scr_tag = scr_tag.split('"')
l=[]
for i in scr_tag:
    if 'http://' in i:
        l.append(i)
addres = str(l[0]).split("\\")
url = 'https://www.google.com/maps/search/' + addres[0].split('/')[-1]
response2 = requests.get(url, headers=headers)
soup2 = BeautifulSoup(response2.text, 'html.parser')
# print(soup2)
t = soup2.find_all('span')
for i in t:
    print(i.text)
print(t)

# tag_iframe.pop(1)
# for i in tag_iframe:
#     response = urllib.request.urlopen(i.attrs['src'])
#     iframe_soup = BeautifulSoup(response)



# text_of_html = str(soup)
# dom = etree.HTML(text_of_html)
# te = dom.xpath('/html/body/div[1]/div/div/div[8]/div/div/div/div[3]/a[contain(@hreh)]')
# te = dom.xpath('//*[@id="mapDiv"]/div/div/div[8]/div/div/div/div[3]/a')
# print([te])
# print(type(te))



# driver = webdriver.Chrome('/Users/mahdikhalilnezhad/PycharmProjects/WebScriping/chromedriver')
# driver.get(url)
# cli = driver.find_element_by_tag_name('document.querySelector("#mapDiv > div > div > div:nth-child(10) > div > div > div > a")')
# cli = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[8]/div/div/div/div[3]/a')
# cli.click()
# driver.close()



# session = HTMLSession()
# # r = session.get(url)
# # map_link = r.html.find('iframe:nth-child(1)', first=True)
# # map_link = map_link.html.find()
# # print(map_link)
# # map_link = str(map_link).split()
# # for i in map_link:
# #     print(i)
# # print(type(map_link))