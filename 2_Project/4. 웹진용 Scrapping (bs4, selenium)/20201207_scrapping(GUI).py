import PySide2
import os
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget, \
                            QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QGroupBox, QSpinBox
from PySide2.QtGui import QIcon
from urllib.request import urlopen
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep


class window(QWidget):

    def __init__(self):
        super().__init__()
        
        #기초윈도우 설정
        self.setWindowTitle('화랑 Web-Zine 도우미')
        self.setGeometry(50,50,500,250)
        
        #아이콘 설정
        self.icon = QIcon('.\icon.jpg')
        self.setWindowIcon(self.icon)

        #기초골격 Layout
        self.vb=QVBoxLayout()
        self.setLayout(self.vb)


        # Groupbox 설정
        self.group1 = QGroupBox('파일명')
        self.group2 = QGroupBox('News 기사 Scrap')
        self.group3 = QGroupBox('사례검색')

        self.vb.addWidget(self.group1)
        self.vb.addWidget(self.group2)
        self.vb.addWidget(self.group3)


        # V 레이아웃 설정
        self.vb1=QVBoxLayout()
        self.vb2=QVBoxLayout()
        self.vb3=QVBoxLayout()

        self.group1.setLayout(self.vb1)
        self.group2.setLayout(self.vb2)
        self.group3.setLayout(self.vb3)


        #레이아웃 설정 (H box)
        self.hb_1 = QHBoxLayout()
        self.hb_2 = QHBoxLayout()
        self.hb_3 = QHBoxLayout()
        self.hb_4 = QHBoxLayout()
        self.hb_5 = QHBoxLayout()
        self.hb_5_1 = QHBoxLayout()
        self.hb_5_2 = QHBoxLayout()
        
        self.vb1.addLayout(self.hb_1)
        self.vb2.addLayout(self.hb_2)
        self.vb2.addLayout(self.hb_3)
        self.vb2.addLayout(self.hb_4)
        self.vb3.addLayout(self.hb_5)
        self.vb3.addLayout(self.hb_5_1)
        self.vb3.addLayout(self.hb_5_2)
        
        #hb_1 설정
        self.save_name=QLabel('파일이름 :')
        self.hb_1.addWidget(self.save_name)

        self.file_name = QLineEdit()
        self.hb_1.addWidget(self.file_name)

        self.btn1=QPushButton('확인')
        self.hb_1.addWidget(self.btn1)

        self.btn1.clicked.connect(self.event_fileName)

        #hb_2 설정
        self.news1=QLabel('노동법률')
        self.hb_2.addWidget(self.news1)

        self.btn2=QPushButton('Scrap')
        self.hb_2.addWidget(self.btn2)

        self.btn2.clicked.connect(self.event_scrap_news1)

        #hb_3 설정
        self.news3=QLabel('매일노동뉴스')
        self.hb_3.addWidget(self.news3)

        self.btn3=QPushButton('Scrap')
        self.hb_3.addWidget(self.btn3)

        self.btn3.clicked.connect(self.event_scrap_news2)


        #hb_4 설정
        self.news4=QLabel('고용노동부')
        self.hb_4.addWidget(self.news4)

        self.btn4=QPushButton('Scrap')
        self.hb_4.addWidget(self.btn4)

        self.btn4.clicked.connect(self.event_scrap_moel)


        #hb_5 설정
        self.news5=QLabel('E-labor 사례검색')
        self.hb_5.addWidget(self.news5)


        #hb_5_1 (ID/PW)
        self.id = QLabel('ID')
        self.hb_5_1.addWidget(self.id)
        self.id_input = QLineEdit()
        self.hb_5_1.addWidget(self.id_input)

        self.pw = QLabel('P/W')
        self.hb_5_1.addWidget(self.pw)
        self.pw_input = QLineEdit()
        self.pw_input.setEchoMode(QLineEdit.Password)
        self.hb_5_1.addWidget(self.pw_input)

        self.case_num = QLabel('검색개수')
        self.hb_5_1.addWidget(self.case_num)
        
        self.case_num_input=QSpinBox()
        self.hb_5_1.addWidget(self.case_num_input)

        self.search = QLabel('검색어')
        self.hb_5_1.addWidget(self.search)
        self.search_input=QLineEdit()
        self.hb_5_1.addWidget(self.search_input)

        self.btn5=QPushButton('검색')
        self.hb_5_1.addWidget(self.btn5)
        self.btn5.clicked.connect(self.elabor_search)

        #hb_5_2 설정
        self.nlrc=QLabel('지노위 지역')
        self.hb_5_2.addWidget(self.nlrc)

        self.legion_input=QLineEdit()
        self.hb_5_2.addWidget(self.legion_input)

        self.case_num2 = QLabel('검색개수')
        self.hb_5_2.addWidget(self.case_num2)

        self.case_num2_input=QSpinBox()
        self.hb_5_2.addWidget(self.case_num2_input)
        
        self.search2 = QLabel('검색어')
        self.hb_5_2.addWidget(self.search2)
        self.search2_input=QLineEdit()
        self.hb_5_2.addWidget(self.search2_input)

        self.btn5_2=QPushButton('검색')
        self.hb_5_2.addWidget(self.btn5_2)

        self.btn5_2.clicked.connect(self.nlrc_search)



    def event_fileName(self):
        confirm = QMessageBox.information(self,'Save File Name',f'[{self.file_name.text()}.txt]로 파일을 저장합니다.',
                                                                QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            self.input_name=self.file_name.text()

        else:
            pass

    def event_scrap_news1(self):
        with open(f'{self.input_name}.txt', 'a', encoding='utf8') as f:
            f.write('\n\n\n\n ################### [   노동법률  ] ###################\n\n')
        print('================================노동법률 메인 뉴스================================')


        url = 'https://www.worklaw.co.kr/'
        labor_law_html=urlopen(url)
        soup3=BeautifulSoup(labor_law_html, "html.parser")


        news=soup3.select('#container > div.clt > div.type1-0 > div.type1-1 > div.type1-1_r > ul > li > a')
                           
        for m in news:
            m1=m.text
            m2_onclick=m.attrs['onclick']
            m2_adrress=m2_onclick.index('pidx=')+len('pidx=')
            m2_slice=m2_onclick[m2_adrress:m2_adrress+5]
            m2=f'https://www.worklaw.co.kr/view/view.asp?in_cate=108&in_cate2=1051&bi_pidx={m2_slice}'
            print(m1)
            print(m2)
            print('')
            
            with open(f'{self.input_name}.txt' ,'a', encoding='utf8') as f:
                f.write(m1+'\n')
                f.write(m2+'\n\n')


    def event_scrap_news2(self):
        with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
            f.write('\n\n\n\n################### [   매일뉴동뉴스  ] ###################\n\n')
        print('================================매일노동뉴스================================')

        labor_news_std_url='https://www.labortoday.co.kr/news/'
        labor_news_url='https://www.labortoday.co.kr/news/articleList.html?sc_section_code=S1N1&view_type=sm'
        labor_html=urlopen(labor_news_url)
        soup2=BeautifulSoup(labor_html, 'html.parser')
        nse=soup2.find_all('td', class_='list-titles')
        print(nse)

        for i in nse:
            j=i.find('a')
            j1=j.text
            j2=labor_news_std_url+j.attrs['href'][-29:]
            print(j1)
            print(j2)
            print('')

            with open(f'{self.input_name}.txt' ,'a', encoding='utf8') as f:
                f.write(j1+'\n')
                f.write(j2+'\n\n')

    def event_scrap_moel(self):
        # 고용노동부
        with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
            f.write('\n\n\n\n ################### [   고용노동부  ] ###################\n\n')
        print('================================고용노동부================================')


        # 고용노동부 - 보도자료
        with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
            f.write('\n\n ------------------ [  뉴스소식(보도자료) ] ------------------\n\n')
        print('================================뉴스소식(보도자료)================================')

        moel_news_url='http://www.moel.go.kr/news/enews/report/enewsList.do'
        moel_html=urlopen(moel_news_url)
        soup2=BeautifulSoup(moel_html, 'html.parser')
        moel_news = soup2.find_all('a', class_='b_tit')

        for l in moel_news:
            l1=l.text
            l2=l.attrs['href']
            l3=f'http://www.moel.go.kr/news/enews/report/enewsView.do?news_seq={l2[-5:]}'
            print(l1)
            print(l3)
            print('')

            with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
                f.write(l1+'\n')
                f.write(l3+'\n\n')


        # 고용노동부 - 정책자료(청년)
        with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
            f.write('\n\n ------------------ [  정책자료(청년) ] ------------------\n\n')
        print('================================정책자료(청년)================================')

        moel_policy_young='http://www.moel.go.kr/policy/policyinfo/young/list.do'
        moel_policy=urlopen(moel_policy_young)
        soup2=BeautifulSoup(moel_policy, 'html.parser')
        policy_news = soup2.select('#txt > div:nth-child(16) > div > ul > li >a')

        for p in policy_news:
            p1=p.text
            p2=p.attrs['href']
            p3=f'http://www.moel.go.kr/policy/policyinfo/young/bbsView.do?bbs_seq={p2[-11:]}'
            print(p1)
            print(p3)
            print('')

            with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
                f.write(p1+'\n')
                f.write(p3+'\n\n')

        # 고용노동부 - 정책자료(여성)
        with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
            f.write('\n\n ------------------ [  정책자료(여성) ] ------------------\n\n')
        print('================================정책자료(여성)================================')

        moel_policy2_woman='http://www.moel.go.kr/policy/policyinfo/woman/list.do'
        moel_policy2=urlopen(moel_policy2_woman)
        soup2=BeautifulSoup(moel_policy2, 'html.parser')
        policy2_news = soup2.select('#txt > div:nth-child(10) > div > ul > li >a')

        for w in policy2_news:
            w1=w.text
            w2=w.attrs['href']
            w3=f'http://www.moel.go.kr/policy/policyinfo/young/bbsView.do?bbs_seq={w2[-11:]}'
            print(w1)
            print(w3)
            print('')

            with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
                f.write(w1+'\n')
                f.write(w3+'\n\n')


        # 고용노동부 - 정책자료(근로조건개선)
        with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
            f.write('\n\n ------------------ [  정책자료(근로조건개선) ] ------------------\n\n')
        print('================================정책자료(근로조건개선)================================')

        moel_lobar_young='http://www.moel.go.kr/policy/policyinfo/lobar/list.do'
        moel_lobar=urlopen(moel_lobar_young)
        soup2=BeautifulSoup(moel_lobar, 'html.parser')
        lobar_news = soup2.select('#txt > div:nth-child(10) > div > ul > li >a')

        for q in lobar_news:
            q1=q.text
            q2=q.attrs['href']
            q3=f'http://www.moel.go.kr/policy/policyinfo/young/bbsView.do?bbs_seq={q2[-11:]}'
            print(q1)
            print(q3)
            print('')

            with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
                f.write(q1+'\n')
                f.write(q3+'\n\n')


    def elabor_search(self):
        start_search = QMessageBox.information(self,'E-labor Case',f'[{self.search_input.text()}]와 관련된 Case {self.case_num_input.text()}개와, 최신 판례, 행정해석 각각 {self.case_num_input.text()}개씩 검색합니다.',
                                                                   QMessageBox.Yes | QMessageBox.No)

        if start_search == QMessageBox.Yes:
            self.elabor_id = self.id_input.text()
            self.elabor_pw = self.pw_input.text()
            self.topic = self.search_input.text()
            self.count = int(self.case_num_input.text())
            self.event_scrap_elabor()

        else:
            pass




    #E-labor

    def event_scrap_elabor(self):
        elabor_login_url='https://www.elabor.co.kr/login/'
        driver=webdriver.Chrome()
        driver.get(elabor_login_url)
        driver.maximize_window()

        driver.find_element_by_css_selector('#u_id').send_keys(self.elabor_id)
        driver.find_element_by_css_selector('#u_pw').send_keys(self.elabor_pw)
        driver.find_element_by_css_selector('.login-btn').click()
        sleep(2)
        driver.switch_to_alert().accept()
        sleep(3)
        driver.find_element_by_css_selector('#loadingMbanner > div > span').click()
        sleep(1)


            # 종합검색 (Searching)
        driver.get('https://www.elabor.co.kr/case/index.asp')
        driver.find_element_by_css_selector('#research_keyword').send_keys(self.topic)
        driver.find_element_by_css_selector('#research_keyword').send_keys(Keys.ENTER)

        with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
            f.write('\n\n\n\n ################### [  E-LABOR  ] ###################\n\n')
            f.write(f'\n\n ------------------ [  {self.topic} 관련 ] ------------------\n\n')

        page=driver.find_element_by_css_selector('#cs-list-tbl').find_element_by_css_selector('tbody')
#E01_w_md > div > div.case_contents > div.case-L > div.case-tit > span
        for i in range(self.count):
            topic=page.find_elements_by_css_selector('tr')[i]
            court=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[0].text
            contents=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[1].text
            date=topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('span').text
            topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('a').click()
            
            driver.switch_to_window(driver.window_handles[-1])
            detail=driver.find_element_by_css_selector('#case-txt-body > div').text
            driver.close()
            driver.switch_to_window(driver.window_handles[0])

            designed_court=court+' '+date
            designed_contents='핵심요약 :\n'+contents
            designed_detail=f'요    약 :\n {detail}'

            print(f'[[[[ case {i+1}]]]]\n')
            print(designed_court)
            print(designed_contents)
            print(designed_detail)
            print('====================================')

            with open(f'{self.input_name}.txt' ,'a', encoding='utf8') as f:
                f.write(f'[[[[ case {i+1}]]]]\n')
                f.write(designed_court+'\n\n')
                f.write(designed_contents+'\n\n')
                f.write(designed_detail+'\n\n')

        sleep(1)



        # 행정해석
        driver.get('https://www.elabor.co.kr/case/index.asp?inx=1&keyword=&research_keyword=&resrch_depth=&keyword_pfet=&keyword_cont=&keyword_excd=&fd_opt=fd_all^cs_title^cs_text^cs_base2^&cate_opt=2^&dt_opt=1&dt_st=&dt_ed=&odr_type=1&andor=1&pType=list&gopage=1&detail_search_chk=undefined&svc_ver=2')

        with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
            f.write(f'\n\n ------------------ [  최신사례(행정해석) ] ------------------\n\n')

        page=driver.find_element_by_css_selector('#cs-list-tbl').find_element_by_css_selector('tbody')
        for i in range(self.count):
            topic=page.find_elements_by_css_selector('tr')[i]
            court=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[0].text
            contents=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[1].text
            date=topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('span').text
            topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('a').click()
            
            driver.switch_to_window(driver.window_handles[-1])
            detail=driver.find_element_by_css_selector('#case-txt-body > div').text
            driver.close()
            driver.switch_to_window(driver.window_handles[0])

            designed_court=court+' '+date
            designed_contents='핵심요약 :\n'+contents
            designed_detail=f'요    약 :\n {detail}'

            print(f'[[[[ case {i+1}]]]]\n')
            print(designed_court)
            print(designed_contents)
            print(designed_detail)
            print('====================================')

            with open(f'{self.input_name}.txt' ,'a', encoding='utf8') as f:
                f.write(f'[[[[ case {i+1}]]]]\n')
                f.write(designed_court+'\n\n')
                f.write(designed_contents+'\n\n')
                f.write(designed_detail+'\n\n')

        sleep(1)

            # 판례
        driver.get('https://www.elabor.co.kr/case/index.asp?inx=1&keyword=&research_keyword=&resrch_depth=&keyword_pfet=&keyword_cont=&keyword_excd=&fd_opt=fd_all^cs_title^cs_text^cs_base2^&cate_opt=4^5^6^9^&dt_opt=1&dt_st=&dt_ed=&odr_type=1&andor=1&pType=list&gopage=1&detail_search_chk=undefined&svc_ver=2')

        with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
            f.write(f'\n\n ------------------ [  최신사례(판례) ] ------------------\n\n')

        page=driver.find_element_by_css_selector('#cs-list-tbl').find_element_by_css_selector('tbody')
        for i in range(self.count):
            topic=page.find_elements_by_css_selector('tr')[i]
            court=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[0].text
            contents=topic.find_elements_by_css_selector('td')[1].find_elements_by_css_selector('span')[1].text
            date=topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('span').text
            topic.find_elements_by_css_selector('td')[2].find_element_by_css_selector('a').click()
            
            driver.switch_to_window(driver.window_handles[-1])
            detail=driver.find_element_by_css_selector('#case-txt-body > div').text
            driver.close()
            driver.switch_to_window(driver.window_handles[0])

            designed_court=court+' '+date
            designed_contents='핵심요약 : \n'+contents
            designed_detail=f'요    약 :\n {detail}'

            print(f'[[[[ case {i+1}]]]]\n')
            print(designed_court)
            print(designed_contents)
            print(designed_detail)
            print('====================================')

            with open(f'{self.input_name}.txt' ,'a', encoding='utf8') as f:
                f.write(f'[[[[ case {i+1}]]]]\n')
                f.write(designed_court+'\n\n')
                f.write(designed_contents+'\n\n')
                f.write(designed_detail+'\n\n')

        driver.close()


    def nlrc_search(self):
        start_search2 = QMessageBox.information(self,'노동위원회 Case',f'[{self.search2_input.text()}]와 관련된 Case {self.case_num2_input.text()}개를 검색합니다.',
                                                                   QMessageBox.Yes | QMessageBox.No)

        if start_search2 == QMessageBox.Yes:
            if self.legion_input.text() == '서울':
                self.legion_input = 'seoul'
            elif self.legion_input.text() == '경기':
                self.legion_input = 'gyeonggi'
            elif self.legion_input.text() == '인천':
                self.legion_input = 'incheon'
            else:
                self.legion_input = 'nlrc'
            self.topic2 = self.search2_input.text()
            self.count2 = int(self.case_num2_input.text())
            self.event_scrap_nlrc()

        else:
            pass

    #노동위원회

    def event_scrap_nlrc(self):
        driver=webdriver.Chrome()
        driver.get(f'http://www.nlrc.go.kr/nlrc/{self.legion_input}/md/search_case.go')
        driver.maximize_window()

        with open(f'{self.input_name}.txt','a', encoding='utf8') as f:
            f.write(f'\n\n ------------------ [  중앙노동위원회 (판정사례) ] ------------------\n\n')

        driver.find_element_by_css_selector('#searchpQuery').send_keys(self.topic2)
        driver.find_element_by_css_selector('#searchpQuery').send_keys(Keys.ENTER)
        driver.find_element_by_css_selector('.text_list > .more').click()

        for i in range(self.count2):
            head=driver.find_element_by_css_selector('.text_list > dl').find_elements_by_css_selector('dt')[i].text
            article=driver.find_element_by_css_selector('.text_list > dl').find_elements_by_css_selector('.text-cut2')[i].text
            
            driver.find_element_by_css_selector('.text_list > dl').find_elements_by_css_selector('dt')[i].find_element_by_css_selector('a').click()
            driver.switch_to_window(driver.window_handles[-1])
            summery=driver.find_element_by_css_selector('#contents > table > tbody > tr:nth-child(4) > td').text
            driver.close()
            driver.switch_to_window(driver.window_handles[0])

            with open(f'{self.input_name}.txt' ,'a', encoding='utf8') as f:
                f.write(f'[[[[ case {i+1}]]]]\n')
                f.write(f'사건번호 : {head}\n\n')
                f.write(f'핵심요약 : {summery}\n\n')
                f.write(f'요   약 :\n{article}\n\n\n')

        sleep(1)
        driver.close()



app=QApplication(sys.argv)
window=window()
window.show()
app.exec_()
sys.exit()





    



