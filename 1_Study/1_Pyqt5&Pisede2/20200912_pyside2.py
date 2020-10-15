import PySide2
import os

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget, QLabel, QLineEdit, QVBoxLayout
from PySide2.QtGui import QIcon
from urllib.request import urlopen
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep


class widget(QWidget):

    def __init__(self):
        super().__init__()
        self.set_window()
        self.set_btn()
        self.set_icon()

    def set_window(self):
        sizeH=400
        sizeW=200
        self.setWindowTitle('화랑 Web Zine 자료 도우미')
        self.setGeometry(0,0,sizeH,sizeW)
        self.setMinimumSize(sizeH,sizeW)

        #위젯 윈도우 창을 모니터 가운데 위치하는 방법
        qrect = self.frameGeometry()
        centerpoint=QDesktopWidget().availableGeometry().center()
        qrect.moveCenter(centerpoint)
        self.move(qrect.topLeft())

    def set_icon(self):
        icon1=QIcon('.\\icon.jpg')
        self.setWindowIcon(QIcon(icon1))

    def set_btn(self):
        #Btn 생성
        btn1 = QPushButton('노동법률',self)
        btn2 = QPushButton('매일노동뉴스',self)
        btn3 = QPushButton('노동법률 Scarap',self)

        #Btn 위치조정
        locationH=20
        locationW=30
        btn1.move(locationH,locationW)
        btn2.move(locationH,locationW+50)
        btn3.move(locationH,locationW+100)

        #Btn 이벤트 할당
        btn1.clicked.connect(self.event_btn1)
        btn2.clicked.connect(self.event_btn2)


    def event_btn1(self):

        file_name=str(20200912)
        with open(f'{file_name}.txt', 'a', encoding='utf8') as f:
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
            
            with open(f'{file_name}.txt' ,'a', encoding='utf8') as f:
                f.write(m1+'\n')
                f.write(m2+'\n\n')


    def event_btn2(self):

        file_name=str(20200912)
        with open(f'{file_name}.txt','a', encoding='utf8') as f:
            f.write('\n\n\n\n################### [   매일뉴동뉴스  ] ###################\n\n')
        print('================================매일노동뉴스================================')

        labor_news_url='http://www.labortoday.co.kr/'
        labor_html=urlopen(labor_news_url)
        soup2=BeautifulSoup(labor_html, 'html.parser')
        labor_news = soup2.find_all('a', class_='float-left flow-hide height-19 size-13 auto-maright-10 auto-martop-5 auto-fontA OnLoad')

        for k in labor_news:
            k1=k.text
            k2=labor_news_url+k.attrs['href']
            print(k1)
            print(k2)
            print('')

            with open(f'{file_name}.txt','a', encoding='utf8') as f:
                f.write(k1+'\n')
                f.write(k2+'\n\n')


app=QApplication(sys.argv)
hr_widget=widget()
hr_widget.show()
app.exec_()
sys.exit()
