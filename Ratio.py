import requests
from bs4 import BeautifulSoup
import xlsxwriter

workbook = xlsxwriter.Workbook('Ratio.xlsx')
worksheet = workbook.add_worksheet( )
css_selector1 = 'th'
css_selector2 = '#ratiotbl a'
css_selector3 = 'td+ td'
url = 'http://fipiran.com/Codal/Ratio'

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')  # about parser: you should know that we can use deferent parser... like "lxml"
elements1 = soup.select(css_selector1)
elements2 = soup.select(css_selector2)
elements3 = soup.select(css_selector3)
col_count = 0
row_count = 1

# in here we want get information from website and inport them to excel file by Rasio name
for i in elements1:
    worksheet.write_string(0, col_count, i.get_text())
    col_count += 1

for i in elements2:
    worksheet.write_string(row_count, 0, i.get_text())
    row_count += 1

l= []
for i in elements3:
    l.append(i.get_text())
x = 0
y = 12
for i in l:
    l[x:y] = [l[x:y]]
    x += 1
    y += 1

col_count = 1
row_count = 1
for i in l:
    for j in i:
        worksheet.write(row_count, col_count, j)
        col_count +=1
    row_count += 1
    col_count = 1

workbook.close()
#########################################################