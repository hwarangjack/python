import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication


class exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setGeometry(400,150,1200,700)
        self.setWindowTitle('exam')
        btn1=QPushButton('Push',self)
        btn1.clicked.connect(QCoreApplication.instance().quit)
        self.show()


    def closeEvent(self, QcloseEvent):
        anw= QMessageBox.question(self,'끝내시겠습니까?','종료하시겠습니까?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if anw == QMessageBox.Yes:
            QcloseEvent.accept()
        else:
            QcloseEvent.ignore()




app=QApplication(sys.argv)
w=exam()
sys.exit(app.exec_())
