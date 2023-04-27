from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from bs4 import BeautifulSoup
import lxml
import time

driver = webdriver.Chrome()

driver.get('https://www.flipkart.com/')

login_cancel = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/button')))
if login_cancel != None:
    login_cancel.click()

search_box = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.CLASS_NAME,'_3704LK')))
search_box.send_keys('python books')

src_button = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.CLASS_NAME,'L0Z3Pu')))
src_button.click()

time.sleep(15)
page_src = driver.page_source

soup = BeautifulSoup(page_src,"lxml")

book_card = soup.find_all('div',class_ ='_4ddWXP')
book_details= []
for item in book_card:
    name = item.find('a',class_='s1Q9rs').text
    author = item.find('div',class_='_3Djpdu').text
    book_details.append([name,author])

print(book_details)




