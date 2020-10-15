from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# id = input('공인노무사회 아이디 입력 :')
# pw = input('공인노무사회 비밀번호 입력 :')

url='http://www.kcplaa.or.kr/'
driver=webdriver.Ie()
driver.get(url)

driver.maximize_window()
driver.find_element_by_css_selector('body > div > table:nth-child(1) > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > a').click()

# driver.find_element_by_css_selector('body > div > table:nth-child(3) > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td > input').click()
# driver.find_element_by_css_selector('body > div > table:nth-child(3) > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td > input').send_keys(id)

sleep(1000)