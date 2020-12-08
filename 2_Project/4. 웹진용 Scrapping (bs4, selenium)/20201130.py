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



labor_news_url='https://www.labortoday.co.kr/news/articleList.html?'
labor_html=urlopen(labor_news_url)
soup2=BeautifulSoup(labor_html, 'html.parser')
print(soup2)
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
