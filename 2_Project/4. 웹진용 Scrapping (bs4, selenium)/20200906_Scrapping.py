from urllib.request import urlopen
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

file_name=input('검색결과를 저장할 파일이름을 입력하세요 : ')
elabor_id=input('E-labor ID를 입력하세요(이메일 형태) : ')
elabor_pw=input('E-labor PW를 입력하세요 : ')
search_topic = input('E-labor 에서 찾으실 주제를 검색하세요 : ')
nlrc_searching=input('중앙노동위원회에서 찾으실 주제를 검색하세요(최신자료는 [근로자]로 검색) :')
case_num = int(input('검색 사례 갯수를 입력하세요'))


#매일노동뉴스
labor_news_url='http://www.labortoday.co.kr/'
labor_html=urlopen(labor_news_url)
soup2=BeautifulSoup(labor_html, 'html.parser')
labor_news = soup2.find_all('a', class_='float-left flow-hide height-19 size-13 auto-maright-10 auto-martop-5 auto-fontA OnLoad')

with open(f'{file_name}.txt','a', encoding='utf8') as f:
    f.write('\n\n\n\n################### [   매일뉴동뉴스  ] ###################\n\n')

print('================================매일노동뉴스================================')

for k in labor_news:
    k1=k.text
    k2=labor_news_url+k.attrs['href']
    print(k1)
    print(k2)
    print('')

    with open(f'{file_name}.txt','a', encoding='utf8') as f:
        f.write(k1+'\n')
        f.write(k2+'\n\n')


# 노동법률
url = 'https://www.worklaw.co.kr/'
labor_law_html=urlopen(url)
soup3=BeautifulSoup(labor_law_html, "html.parser")
news=soup3.select('#container > div.clt > div.type1-0 > div.type1-1 > div.type1-1_r > ul > li > a')

with open(f'{file_name}.txt', 'a', encoding='utf8') as f:
    f.write('\n\n\n\n ################### [   노동법률  ] ###################\n\n')

print('================================노동법률 메인 뉴스================================')

for m in news:
    m1=m.text
    m2_onclick=m.attrs['onclick']
    m2_adrress=m2_onclick.index('pidx=')+len('pidx=')
    m2_slice=m2_onclick[m2_adrress:m2_adrress+5]
    m2=f'https://www.worklaw.co.kr/view/view.asp?in_cate=108&in_cate2=1051&bi_pidx={m2_slice}'
    print(m1)
    print(m2)
    print('')
    
    with open(f'{file_name}.txt' ,'a', encoding='utf8') as f:
        f.write(m1+'\n')
        f.write(m2+'\n\n')



# 고용노동부
moel_news_url='http://www.moel.go.kr/news/enews/report/enewsList.do'
moel_html=urlopen(moel_news_url)
soup2=BeautifulSoup(moel_html, 'html.parser')
moel_news = soup2.find_all('a', class_='b_tit')

with open(f'{file_name}.txt','a', encoding='utf8') as f:
    f.write('\n\n\n\n ################### [   고용노동부  ] ###################\n\n')

print('================================고용노동부 뉴스소식(보도자료)================================')

for l in moel_news:
    l1=l.text
    l2=l.attrs['href']
    l3=f'http://www.moel.go.kr/news/enews/report/enewsView.do?news_seq={l2[-5:]}'
    print(l1)
    print(l3)
    print('')

    with open(f'{file_name}.txt','a', encoding='utf8') as f:
        f.write(l1+'\n')
        f.write(l3+'\n\n')


# E-labor (( 최신 사례 추출 ))

    # 로그인
elabor_login_url='https://www.elabor.co.kr/login/'
driver=webdriver.Chrome()
driver.get(elabor_login_url)
driver.maximize_window()

driver.find_element_by_css_selector('#u_id').send_keys(elabor_id)
driver.find_element_by_css_selector('#u_pw').send_keys(elabor_pw)
driver.find_element_by_css_selector('.login-btn').click()
sleep(2)
driver.switch_to_alert().accept()
sleep(3)
driver.find_element_by_css_selector('#loadingMbanner > div > span').click()
sleep(1)



    # 종합검색 (Searching)
driver.get('https://www.elabor.co.kr/case/index.asp')
driver.find_element_by_css_selector('#research_keyword').send_keys(search_topic)
driver.find_element_by_css_selector('#research_keyword').send_keys(Keys.ENTER)

with open(f'{file_name}.txt','a', encoding='utf8') as f:
    f.write('\n\n\n\n ################### [  E-LABOR  ] ###################\n\n')
    f.write(f'\n\n ------------------ [  {search_topic} 관련 ] ------------------\n\n')

page=driver.find_element_by_css_selector('#cs-list-tbl').find_element_by_css_selector('tbody')

for i in range(case_num):
    topic=page.find_elements_by_css_selector('tr')[i]
    court=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[0].text
    contents=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[1].text
    date=topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('span').text
    topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('a').click()
    
    driver.switch_to_window(driver.window_handles[-1])
    detail=driver.find_element_by_css_selector('#case-txt-body > div').text
    driver.close()
    driver.switch_to_window(driver.window_handles[0])

    designed_court=court+' '+date+' '
    designed_contents='핵심요약 : '+contents
    designed_detail=f'요    약 :\n {detail}'

    print(f'[[[[ case {i+1}]]]]\n')
    print(designed_court)
    print(designed_contents)
    print(designed_detail)
    print('====================================')

    with open(f'{file_name}.txt' ,'a', encoding='utf8') as f:
        f.write(f'[[[[ case {i+1}]]]]\n')
        f.write(designed_court+'\n')
        f.write(designed_contents+'\n')
        f.write(designed_detail+'\n\n')

sleep(1)



    # 행정해석
driver.get('https://www.elabor.co.kr/case/index.asp?inx=1&keyword=&research_keyword=&resrch_depth=&keyword_pfet=&keyword_cont=&keyword_excd=&fd_opt=fd_all^cs_title^cs_text^cs_base2^&cate_opt=2^&dt_opt=1&dt_st=&dt_ed=&odr_type=1&andor=1&pType=list&gopage=1&detail_search_chk=undefined&svc_ver=2')

with open(f'{file_name}.txt','a', encoding='utf8') as f:
    f.write(f'\n\n ------------------ [  최신사례(행정해석) ] ------------------\n\n')

page=driver.find_element_by_css_selector('#cs-list-tbl').find_element_by_css_selector('tbody')
for i in range(case_num):
    topic=page.find_elements_by_css_selector('tr')[i]
    court=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[0].text
    contents=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[1].text
    date=topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('span').text
    topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('a').click()
    
    driver.switch_to_window(driver.window_handles[-1])
    detail=driver.find_element_by_css_selector('#case-txt-body > div').text
    driver.close()
    driver.switch_to_window(driver.window_handles[0])

    designed_court=court+' '+date+' '
    designed_contents='핵심요약 : '+contents
    designed_detail=f'요    약 :\n {detail}'

    print(f'[[[[ case {i+1}]]]]\n')
    print(designed_court)
    print(designed_contents)
    print(designed_detail)
    print('====================================')

    with open(f'{file_name}.txt' ,'a', encoding='utf8') as f:
        f.write(f'[[[[ case {i+1}]]]]\n')
        f.write(designed_court+'\n')
        f.write(designed_contents+'\n')
        f.write(designed_detail+'\n\n')

sleep(1)

    # 판례
driver.get('https://www.elabor.co.kr/case/index.asp?inx=1&keyword=&research_keyword=&resrch_depth=&keyword_pfet=&keyword_cont=&keyword_excd=&fd_opt=fd_all^cs_title^cs_text^cs_base2^&cate_opt=4^5^6^9^&dt_opt=1&dt_st=&dt_ed=&odr_type=1&andor=1&pType=list&gopage=1&detail_search_chk=undefined&svc_ver=2')

with open(f'{file_name}.txt','a', encoding='utf8') as f:
    f.write(f'\n\n ------------------ [  최신사례(판례) ] ------------------\n\n')

page=driver.find_element_by_css_selector('#cs-list-tbl').find_element_by_css_selector('tbody')
for i in range(case_num):
    topic=page.find_elements_by_css_selector('tr')[i]
    court=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[0].text
    contents=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[1].text
    date=topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('span').text
    topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('a').click()
    
    driver.switch_to_window(driver.window_handles[-1])
    detail=driver.find_element_by_css_selector('#case-txt-body > div').text
    driver.close()
    driver.switch_to_window(driver.window_handles[0])

    designed_court=court+' '+date+' '
    designed_contents='핵심요약 : '+contents
    designed_detail=f'요    약 :\n {detail}'

    print(f'[[[[ case {i+1}]]]]\n')
    print(designed_court)
    print(designed_contents)
    print(designed_detail)
    print('====================================')

    with open(f'{file_name}.txt' ,'a', encoding='utf8') as f:
        f.write(f'[[[[ case {i+1}]]]]\n')
        f.write(designed_court+'\n')
        f.write(designed_contents+'\n')
        f.write(designed_detail+'\n\n')

sleep(1)


# 중앙노동위원회

driver.get('http://www.nlrc.go.kr/nlrc/seoul/md/search_case.go')

with open(f'{file_name}.txt','a', encoding='utf8') as f:
    f.write(f'\n\n ------------------ [  중앙노동위원회 (판정사례) ] ------------------\n\n')

driver.find_element_by_css_selector('#searchpQuery').send_keys(nlrc_searching)
driver.find_element_by_css_selector('#searchpQuery').send_keys(Keys.ENTER)
driver.find_element_by_css_selector('.text_list > .more').click()

for i in range(case_num):
    head=driver.find_element_by_css_selector('.text_list > dl').find_elements_by_css_selector('dt')[i].text
    article=driver.find_element_by_css_selector('.text_list > dl').find_elements_by_css_selector('.text-cut2')[i].text
    
    driver.find_element_by_css_selector('.text_list > dl').find_elements_by_css_selector('dt')[i].find_element_by_css_selector('a').click()
    driver.switch_to_window(driver.window_handles[-1])
    summery=driver.find_element_by_css_selector('#contents > table > tbody > tr:nth-child(4) > td').text
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
   
    print(head)
    print(summery)
    print(article)
    print('----')

    with open(f'{file_name}.txt' ,'a', encoding='utf8') as f:
        f.write(f'[[[[ case {i+1}]]]]\n')
        f.write(f'사건번호 : {head}\n')
        f.write(f'핵심요약 : {summery}\n')
        f.write(f'요   약 :\n{article}\n\n\n')

sleep(1)
driver.close()