# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_formulario.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-20, 0, 801, 561))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_login = QLabel(self.frame)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setGeometry(QRect(370, 130, 141, 51))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        self.txt_login.setFont(font)
        self.txt_login.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.txt_email = QLabel(self.frame)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(210, 220, 91, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.txt_email.setFont(font1)
        self.line_email = QLineEdit(self.frame)
        self.line_email.setObjectName(u"line_email")
        self.line_email.setGeometry(QRect(290, 230, 281, 21))
        self.txt_senha = QLabel(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(210, 260, 91, 31))
        self.txt_senha.setFont(font1)
        self.line_senha = QLineEdit(self.frame)
        self.line_senha.setObjectName(u"line_senha")
        self.line_senha.setGeometry(QRect(290, 270, 281, 22))
        self.pushButton_Entrar = QPushButton(self.frame)
        self.pushButton_Entrar.setObjectName(u"pushButton_Entrar")
        self.pushButton_Entrar.setGeometry(QRect(360, 333, 121, 51))
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButton_Entrar.setFont(font2)
        self.pushButton_Entrar.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def show_login_page(self):
        self.parent().setCurrentIndex(0)
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.txt_email.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.txt_senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.pushButton_Entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
    # retranslateUi
    
if __name__ == "__main__":
    app = QApplication([]) 
    mainWindow = QMainWindow()  
    ui = Ui_MainWindow()  
    ui.setupUi(mainWindow)  
    mainWindow.show()  
    app.exec()  