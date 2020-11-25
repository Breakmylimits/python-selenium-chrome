from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup



driver = webdriver.Chrome()
url= 'https://www.google.com/'
driver.get(url)

page_html = driver.page_source
 
data = soup(page_html, 'html.parser')


elem_search = driver.find_element_by_name('q')
elem_search.clear()
elem_search.send_keys('emi fukada')
elem_search.send_keys(Keys.ENTER)

