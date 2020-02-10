# from requests_html import HTMLSession
# from pprint import pprint

# url = 'http://google.com'

# session = HTMLSession()
# r = session.get(url)
# links =  r.html.absolute_links
# for i in links:
#     print(i)

# ### is that is better than requests

search_text = input('what are you looking for? ')
url = 'https://www.google.com/search?q=' + search_text
headers = {'ccept-language': 'en-US,en;q=0.9,fa;q=0.8'}

session = HTMLSession()

r = session.get(url, headers=headers)

print(r)

# list_of_links = r.html.absolute_links
# for i in list_of_links:
#     print(i)

titel = r.html.find('.r', first=True)
text_of_titles = titel.text
print(text_of_titles)