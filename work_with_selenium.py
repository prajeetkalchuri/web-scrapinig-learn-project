from selenium import webdriver
import asyncio
import random
import datetime
from selenium.webdriver.support.ui import Select

email = input('type your email:')


def D() :
    list_of_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    d = datetime.date(1,1,1)
    d = d.today()
    d = str(d)
    d = d.split('-')
    y = d[0]
    m = d[1]
    d = d[2]
    y = int(y)
    m = int(m)
    d = int(d)
    Date = datetime.date(y,m,d)
    number_of_day = Date.isoweekday() - 1
    return list_of_days[number_of_day]


day = D()


async def main() :
    url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'
    driver = webdriver.Chrome('/Users/mahdikhalilnezhad/PycharmProjects/WebScriping/chromedriver')
    driver.maximize_window()
    driver.get(url)

    # await asyncio.sleep(1)
    # The code for the email import field
    search_namad_field = driver.find_element_by_id('user-message')
    search_namad_field.clear()
    search_namad_field.send_keys(email)
    # await asyncio.sleep(1)

    search_botton = driver.find_element_by_class_name("btn")
    search_botton.click()
    # await asyncio.sleep(1)

    # The code for entering two numbers and displaying their result
    search_namad_field = driver.find_element_by_id('sum1')
    search_namad_field.clear()
    search_namad_field.send_keys(random.randrange(100))
    # await asyncio.sleep(1)

    search_namad_field = driver.find_element_by_id('sum2')
    search_namad_field.clear()
    search_namad_field.send_keys(random.randrange(100))
    # await asyncio.sleep(1)

    # element = driver.find_element_by_xpath("//button[@onclick='return']")
    # element = driver.findElement(By.linkText("Get Total"));
    element = driver.find_element_by_class_name('btn')
    element.click()
    # await asyncio.sleep(1)

    # Part II of the project
    url = 'https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html'
    driver.get(url)
    # await asyncio.sleep(1)

    element = driver.find_element_by_id('select-demo')
    element.click()
    await asyncio.sleep(1)

    element = driver.find_element_by_xpath("//select[@id='select-demo']")
    element = Select(element)
    element.select_by_value(day)
    element = driver.find_element_by_class_name('row')
    element.click()

    await asyncio.sleep(3)
    driver.quit()


asyncio.run(main())
