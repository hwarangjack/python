import time
from urllib.request import urlopen
from urllib.parse import quote_plus, urlunparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

context=[]

def getItemByElabor(topic, count):
    # login
    driver=webdriver.Chrome()
    driver.get('https://www.elabor.co.kr/login/')
    driver.maximize_window()
    id='hwarang-hr@naver.com'
    pw='ghkfkd2020~'
    driver.find_element_by_css_selector('#u_id').send_keys(id)
    driver.find_element_by_css_selector('#u_pw').send_keys(pw)
    driver.find_element_by_css_selector('.login-btn').click()
    sleep(2)
    driver.switch_to_alert().accept()
    sleep(3)
    driver.find_element_by_css_selector('#loadingMbanner > div > span').click()
    sleep(1)

    # Get the article
    topic=topic
    count=count   
    driver.get('https://www.elabor.co.kr/case/index.asp')
    driver.find_element_by_css_selector('#research_keyword').send_keys(topic)
    driver.find_element_by_css_selector('#research_keyword').send_keys(Keys.ENTER)
    page=driver.find_element_by_css_selector('#cs-list-tbl').find_element_by_css_selector('tbody')
    context = []

    for i in range(count):
        topic=page.find_elements_by_css_selector('tr')[i]
        court=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[0].text
        contents=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[1].text
        date=topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('span').text
        topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('a').click()
        driver.switch_to_window(driver.window_handles[-1])
        sleep(10)
        detail=driver.find_element_by_css_selector('#case-txt-body > div').text
        driver.close()
        driver.switch_to_window(driver.window_handles[0])

        designed_court=court+' '+date
        designed_contents=contents
        designed_detail=detail

        item = [designed_court, designed_contents, designed_detail]
        context.append(item)
        driver.close()
    return context

def getItemByMoel(count):
    html=urlopen('http://www.moel.go.kr/news/enews/report/enewsList.do')
    soup=BeautifulSoup(html, 'html.parser')
    news = soup.find_all('a', class_='b_tit')
    firstPostUrl = news[1].attrs['href']
    UrlNum = firstPostUrl[-5:]
    context = []

    for i in range(count):
        intUrlNum = int(UrlNum)-i
        strUrlNum = str(intUrlNum)
        html2=urlopen(f'http://www.moel.go.kr/news/enews/report/enewsView.do?news_seq={strUrlNum}')
        soup2=BeautifulSoup(html2, 'html.parser')
        title = soup2.select_one('#txt > div.board_view_02 > div.b_info > dl.w100 > dd')
        content = soup2.select_one('#txt > div.board_view_02 > div.b_info > div')
        item = [title.text, content.text]
        context.append(item)

    return context


def UploadItemWebzine(items):
    TargetUrl = 'https://hrang.co.kr/board/webzine/'
    driver=webdriver.Chrome()
    driver.get(TargetUrl)
    driver.maximize_window()
    driver.find_element_by_css_selector('body > header > div.header-login > li:nth-child(1) > a').click()
    driver.find_element_by_css_selector('#id_username').click()
    driver.find_element_by_css_selector('#id_username').send_keys('hrang')
    driver.find_element_by_css_selector('#id_username').send_keys(Keys.TAB)
    driver.find_element_by_css_selector('#id_password').send_keys('wlffjt87')
    driver.find_element_by_css_selector('body > div > div > form > div:nth-child(2) > button').click()

    driver.get(TargetUrl)

    for i in items:
        sleep(1)
        driver.find_element_by_css_selector('body > div > div > div.content_wrapper > div.location_flexend > a > button').click()

        driver.find_element_by_css_selector('#id_casenum').click()
        driver.find_element_by_css_selector('#id_casenum').send_keys(i[0])
        driver.find_element_by_css_selector('#id_casenum').send_keys(Keys.TAB)

        driver.find_element_by_css_selector('#id_keyword').send_keys(i[1])
        driver.find_element_by_css_selector('#id_keyword').send_keys(Keys.TAB)

        driver.find_element_by_css_selector('#id_keysentence').send_keys(i[2])
        driver.find_element_by_css_selector('#id_keysentence').send_keys(Keys.TAB)
        sleep(2)
        driver.find_element_by_css_selector('body > div > div > div.content_wrapper > form > div.location_flexend > button').click()


def UploadItemNews(items):
    TargetUrl = 'https://hrang.co.kr/board/news/'
    driver=webdriver.Chrome()
    driver.get(TargetUrl)
    driver.maximize_window()
    driver.find_element_by_css_selector('body > header > div.header-login > li:nth-child(1) > a').click()
    driver.find_element_by_css_selector('#id_username').click()
    driver.find_element_by_css_selector('#id_username').send_keys('hrang')
    driver.find_element_by_css_selector('#id_username').send_keys(Keys.TAB)
    driver.find_element_by_css_selector('#id_password').send_keys('wlffjt87')
    driver.find_element_by_css_selector('body > div > div > form > div:nth-child(2) > button').click()

    driver.get(TargetUrl)

    for i in items:
        sleep(1)
        
        i[0] = '[고용노동부]'+i[0]

        driver.find_element_by_css_selector('body > div > div > div.content_wrapper > div.location_flexend > a > button').click()

        driver.find_element_by_css_selector('#id_news_headline').click()
        sleep(1)
        driver.find_element_by_css_selector('#id_news_headline').send_keys(i[0])
        sleep(1)

        driver.find_element_by_css_selector('#id_news_content').click()
        sleep(1)
        driver.find_element_by_css_selector('#id_news_content').send_keys(i[1])
        sleep(5)
        driver.find_element_by_css_selector('body > div > div > div.content_wrapper > form > div.location_flexend > button').click()


UploadItemNews(
    getItemByMoel(5)
)
