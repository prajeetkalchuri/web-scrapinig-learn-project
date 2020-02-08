'''
hi evry body , here is pycharm. body you know that but i must to tell you so important, i'm very happy.
'''
from requests_html import AsyncHTMLSession

search_url = input('what are you looking for?')
url_google = 'https://www.google.com/search?q=' + search_url
url_bing = 'https://www.bing.com/search?q=' + search_url
url_yahoo = 'https://search.yahoo.com/search?p=' + search_url
url_ask = 'https://www.ask.com/web?o=0&l=dir&qo=serpSearchTopBox&q=' + search_url

asession = AsyncHTMLSession()

async def google_engine():
    r = await asession.get(url_google)
async def bing_engin():
    r = await asession.get(url_bing)
async def yahoo_engin():
    r = await asession.get(url_yahoo)
async def ask_engin():
    r = await asession.get(url_ask)

r = asession.run(google_engine, bing_engin, yahoo_engin, ask_engin)

