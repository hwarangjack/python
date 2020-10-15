import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QGroupBox, QTextEdit, QCheckBox, QProgressBar
from PySide2.QtGui import QIcon
import sys

import os

class window(QWidget):

    def __init__(self):
        super().__init__()
        self.name=''
        #기본세트 set 3종(windowtitle, geometry, windowicon)
        self.setWindowTitle('[노무법인 화랑 컨설팅] Auto Email')
        self.setGeometry(500,150,400,600)
        self.setMinimumSize(400,600)
        window_icon=QIcon('.\icon.jpg')
        self.setWindowIcon(window_icon)

        # Main Layout 설정
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        #1 main_layout > group1
        self.group1 = QGroupBox('불러올 Excel 파일명')
        self.main_layout.addWidget(self.group1)
        #1 main_layout > group1 > V Box
        self.vb1 = QVBoxLayout()
        self.group1.setLayout(self.vb1)
        #1 main_layout > group1 > V Box > Label
        self.lbl_filename = QLabel('※확장명(.xlsm, .xlsx 등)까지 기재')
        self.vb1.addWidget(self.lbl_filename)
        #1 main_layout > group1 > V Box > H Box
        self.hb_filename = QHBoxLayout()
        self.vb1.addLayout(self.hb_filename)
        #1 main_layout > group1 > V Box > H Box > LE
        self.le_filename = QLineEdit()
        self.hb_filename.addWidget(self.le_filename)
        #1 main_layout > group1 > V Box > H Box > BTN
        self.btn_filename = QPushButton('확 인')
        self.hb_filename.addWidget(self.btn_filename)
        self.btn_filename.clicked.connect(self.fix_filename)

        #2 main_layout > group2
        self.group2 = QGroupBox('발신자 네이버 Login')
        self.main_layout.addWidget(self.group2)
        #2 main_layout > group1 > H box
        self.hb2 = QHBoxLayout()
        self.group2.setLayout(self.hb2)
        #2 main_layout > group1 > H box > V Box 
        self.vb2 = QVBoxLayout()
        self.hb2.addLayout(self.vb2)
        #2 main_layout > group1 > H box > V Box > H box
        self.hb21=QHBoxLayout()
        self.vb2.addLayout(self.hb21)
        #2 main_layout > group1 > H box > V Box > H box > LE
        self.le_id=QLineEdit()
        self.hb21.addWidget(self.le_id)
        #2 main_layout > group1 > H box > V Box > H box > LB
        self.naver=QLabel('@naver.com')
        self.hb21.addWidget(self.naver)
        #2 main_layout > group1 > H box > V Box > LE
        self.le_pw=QLineEdit()
        self.le_pw.setEchoMode(QLineEdit.Password)
        self.vb2.addWidget(self.le_pw)
        #2 main_layout > group1 > H box > BTN
        self.btn_login = QPushButton('확 인')
        self.btn_login.setMaximumHeight(500)
        self.hb2.addWidget(self.btn_login)
        self.btn_login.clicked.connect(self.email_check)

        #3 main_layout > group3
        self.group3 = QGroupBox('메일내용')
        self.main_layout.addWidget(self.group3)
        #3 main_layout > group3 > V box
        self.vb3 = QVBoxLayout()
        self.group3.setLayout(self.vb3)
        #3 main_layout > group3 > V box > Label1
        self.lbl_subject = QLabel('메일제목')
        self.vb3.addWidget(self.lbl_subject)
        #3 main_layout > group3 > V box > LE
        self.le_subject=QLineEdit()
        self.vb3.addWidget(self.le_subject)
        #3 main_layout > group3 > V box > CK box
        self.chkb_subject_plus = QCheckBox('메일제목에 수신자 추가',self)
        self.vb3.addWidget(self.chkb_subject_plus)
        self.chkb_subject_plus.stateChanged.connect(self.plus_subject)
        #3 main_layout > group3 > V box > Label3
        self.lbl_contents = QLabel('※ 메일본문')
        self.vb3.addWidget(self.lbl_contents)
        #3 main_layout > group3 > V box > TE
        self.te_contents=QTextEdit()
        self.vb3.addWidget(self.te_contents)
        #3 main_layout > group3 > V box > BTN
        self.btn_subject=QPushButton('확 인')
        self.vb3.addWidget(self.btn_subject)
        self.btn_subject.clicked.connect(self.sbj_cts)

        #4 main_layout > group4
        self.group4 = QGroupBox('메일발송')
        self.main_layout.addWidget(self.group4)
        #4 main_layout > H box
        self.hb4 = QHBoxLayout()
        self.group4.setLayout(self.hb4)
        #4 main_layout > H box > BTN
        self.btn_send = QPushButton('발 송')
        self.hb4.addWidget(self.btn_send)
        self.btn_send.clicked.connect(self.send)
        #4 main_layout > H box > BTN
        self.btn_all_clear = QPushButton('초기화')
        self.hb4.addWidget(self.btn_all_clear)
        self.btn_all_clear.clicked.connect(self.reset)


    def fix_filename(self):
               
        if len(self.le_filename.text())==0:
            QMessageBox.about(self,'확인요청','파일이름을 입력하세요')

        elif self.le_filename.text().count('.')==0:
            QMessageBox.about(self,'확인요청',' .xlsx 등의 확장자까지 입력하세요')
        
        else:
            if self.le_filename.text() in os.listdir('.'):
               QMessageBox.about(self,'확인','파일이 정상적으로 확인됬습니다.')
               self.final_filename=self.le_filename.text()  #함수의 영역을 벋어나 self 차원에서 변수를 사용하고자 할 경우에는, 변수명 앞에 self를 붙여야 작동하는 것 같음
                              
            else:
                QMessageBox.about(self,'경고','현재 프로그램이 설치된 폴더 안에 입력하신 파일이 존재하지 않습니다.')
    

    def email_check(self):
        
        if len(self.le_id.text())&len(self.le_pw.text())==0:
            QMessageBox.about(self,'확인요청','이메일 ID와 PW를 모두 입력하세요')
        
        else:
            confirm = QMessageBox.information(self,'Login Email',f'메일 발신자를 {self.le_id.text()}으로 합니다.',
                                          QMessageBox.Yes|QMessageBox.No)
            if confirm == QMessageBox.Yes:
                self.id=self.le_id.text()+self.naver.text()  #함수의 영역을 벋어나 self 차원에서 변수를 사용하고자 할 경우에는, 변수명 앞에 self를 붙여야 작동하는 것 같음
                self.pw=self.le_pw.text()                    #함수의 영역을 벋어나 self 차원에서 변수를 사용하고자 할 경우에는, 변수명 앞에 self를 붙여야 작동하는 것 같음
                
            else:
                self.le_id.clear()
                self.le_pw.clear()

    def sbj_cts(self):
    
        if len(self.le_subject.text())&len(self.te_contents.toPlainText())==0:
            empty = QMessageBox.information(self,'메일제목, 메일본문' ,f'메일을 공란으로 설정하시겠습니까?',
                                                        QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
            if empty == QMessageBox.Yes:
                self.name=self.le_subject.text()                 #함수의 영역을 벋어나 self 차원에서 변수를 사용하고자 할 경우에는, 변수명 앞에 self를 붙여야 작동하는 것 같음
                self.contents=self.te_contents.toPlainText()     #함수의 영역을 벋어나 self 차원에서 변수를 사용하고자 할 경우에는, 변수명 앞에 self를 붙여야 작동하는 것 같음

            else:
                QMessageBox.about(self,'경고','메일제목과 메일내용이 저장되지 않았습니다.\n 다시 설정해주세요.')
                pass
        
        else:
            ready_sbj_cts = QMessageBox.information(self,'메일제목, 메일본문' ,f'다음의 내용으로 메일을 발송합니다\n\n[제 목] {self.le_subject.text()}\n\n[내 용]\n{self.te_contents.toPlainText()}',
                                                                            QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
            if ready_sbj_cts == QMessageBox.Yes:
                self.name=self.le_subject.text()                 #함수의 영역을 벋어나 self 차원에서 변수를 사용하고자 할 경우에는, 변수명 앞에 self를 붙여야 작동하는 것 같음
                self.contents=self.te_contents.toPlainText()     #함수의 영역을 벋어나 self 차원에서 변수를 사용하고자 할 경우에는, 변수명 앞에 self를 붙여야 작동하는 것 같음

            else:
                QMessageBox.about(self,'경고','메일제목과 메일내용이 저장되지 않았습니다.\n 다시 설정해주세요.')
                pass

    def plus_subject(self):
        if self.chkb_subject_plus.isChecked() == True:
            self.plus=1
        else:
            self.plus=0


    def send(self):

        try:
            df=pd.read_excel(self.final_filename, sheet_name=0)   #현재의 함수의 외의 영역에서 정의된 변수를 사용할 때에는, self 단위에서 변수를 사용해야 함
            to_list=df.values.tolist()
            
            # 기본조건 설정
            subject1=self.name          #메일제목
            contents=self.contents      #메일내용
            success=0
            fail=0
            deny=0

            for i in to_list:

                #i[0] = 인덱스 //// i[1] = 발송여부 //// i[2] = 성명 //// i[3] = 이메일주소
                if i[1] == 1:
                    success=success+1
                    to=i[3]
                    From =self.id                                 #현재의 함수의 외의 영역에서 정의된 변수를 사용할 때에는, self 단위에서 변수를 사용해야 함

                    if self.plus == 1:
                        subject2=f' ({i[2]})'
                    else:
                        subject2=""
                    subject=subject1+subject2

                    # 복합객체 신설, 변수할당
                    message = MIMEMultipart()

                    # message Part 1 ([발송자, 받는자, 주제, 글내용] 삽입)
                    message["from"] = From
                    message['to']= to
                    message['subject']=subject    
                    message.attach(MIMEText(contents))

                    # message Part 2 ([첨부파일] 삽입)
                    try:
                        file_name=f'{subject}.pdf'
                        part = MIMEBase('application','octet-stream') #고정값인듯?
                        part.set_payload(open(file_name,'rb').read()) #파일을 읽어서 MIMEBase에 업로드하고
                        encoders.encode_base64(part) #디코딩해라
                        part.add_header('content-disposition','attachment', filename=file_name)  #고정값인듯
                        message.attach(part)

                    except:
                        fail=fail+1
                        pass

                    # SMTP 메일발송 기초사항 설정
                    # SSL인증방식에서는 포트번호 465를 사용하고, TLS인증방법에서는 587을 사용(하고, starttls()함수 호출 필요)한다
                    smtp = smtplib.SMTP('smtp.naver.com',587)
                    smtp.ehlo
                    smtp.starttls()
                    smtp.login(self.id,self.pw)                             #현재의 함수의 외의 영역에서 정의된 변수를 사용할 때에는, self 단위에서 변수를 사용해야 함
                    smtp.sendmail(From, to, message.as_string())
                    smtp.quit()

                else:
                    deny=deny+1

            QMessageBox.about(self,'결과알림',f'총 대상 : {len(to_list)}\n 정상발송 : {success}\n 첨부파일 미첨부 : {fail}\n 발송거부 : {deny}')

        except:
            QMessageBox.about(self,'확인요청','내용을 다시 확인하시기 바랍니다.')

    def reset(self):
        self.le_filename.clear()
        self.final_filename=""

        self.le_id.clear()
        self.id=""

        self.le_pw.clear()
        self.pw=""

        self.le_subject.clear()
        self.name=""

        self.te_contents.clear()
        self.contents=""



app = QApplication(sys.argv)
window = window()
window.show()
app.exec_()
sys.exit()
