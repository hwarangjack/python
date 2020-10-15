from selenium import webdriver

driver = webdriver.Chrome()
url='https://google.com'
driver.get(url)

driver.find_element_by_css_selector('.gLFyf gsfi').send_keys('파이썬')
