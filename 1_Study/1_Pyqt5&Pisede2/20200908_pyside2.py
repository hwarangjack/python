from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtGui import QIcon
import sys




class widget(QWidget):

    def __init__(self):
        super().__init__()
        self.set_window()
        self.set_icon()

        self.btn=QPushButton('첫 푸시버튼',self)
        self.btn.move(300,200)
        self.btn.clicked.connect(self.hello)

    def set_window(self):
        sizeH=1300
        sizeW=800
        self.setWindowTitle('첫 위젯')
        self.setGeometry(300,120,sizeH,sizeW)
        self.setMinimumSize(sizeH,sizeW)

    def set_icon(self):
        self.setWindowIcon(QIcon('.\image\icon.jpg'))
        

    def hello(self):
        print(self.btn.text())


app=QApplication(sys.argv)
hr_widget=widget()
hr_widget.show()
app.exec_()
sys.exit()
