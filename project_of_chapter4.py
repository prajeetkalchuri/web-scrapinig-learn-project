import requests
from bs4 import BeautifulSoup
from lxml import etree
from requests_html import HTMLSession
from selenium import webdriver



# url = input('what is your url: ')
url = 'http://www.dsit.org.ir/?cmd=page&Cid=92&title=Kontakt&lang=fa'


r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
tag_a = soup.find_all('a')
for i in tag_a:
    print(i.text)

# text_of_html = str(soup)
# dom = etree.HTML(text_of_html)
# te = dom.xpath('/html/body/div[1]/div/div/div[8]/div/div/div/div[3]/a[contain(@hreh)]')
# te = dom.xpath('//*[@id="mapDiv"]/div/div/div[8]/div/div/div/div[3]/a')
# print([te])
# print(type(te))




# driver = webdriver.Chrome('/Users/mahdikhalilnezhad/PycharmProjects/WebScriping/chromedriver')
# driver.get(url)
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