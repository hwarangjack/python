from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PySide2.QtGui import QIcon
import sys




class widget(QWidget):

    def __init__(self):
        super().__init__()
        self.set_window()
        self.set_icon()
        self.set_btn()


    def set_window(self):
        sizeH=1300
        sizeW=800
        self.setWindowTitle('첫 위젯')
        self.setGeometry(300,120,sizeH,sizeW)
        self.setMinimumSize(sizeH,sizeW)

    def set_icon(self):
        icon1=QIcon('.\\image\\icon.jpg')
        self.setWindowIcon(QIcon(icon1))

    def set_btn(self):
        locationH=100
        locationW=100

        #Btn 생성
        btn1 = QPushButton('노동법률',self)
        btn2 = QPushButton('매일노동뉴스',self)
        btn3 = QPushButton('노동법률 Scarap',self)


        #Btn 위치조정
        btn1.move(locationH,locationW)
        btn2.move(locationH+100,locationW)
        btn3.move(locationH+200,locationW)

        #Btn 이벤트 할당
        btn1.clicked.connect(self.btn1_event)

    def btn1_event(self):
        intro = QMessageBox.question(self,'노동법률','노동법률 Scarap을 실행하시겠습니까?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if intro == QMessageBox.Yes:
            app.quit()
        
        else:
            pass

    def hello(self):
        print(self.btn.text())


app=QApplication(sys.argv)
hr_widget=widget()
hr_widget.show()
app.exec_()
sys.exit()
