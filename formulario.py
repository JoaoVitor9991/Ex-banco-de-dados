# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1137, 840)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 10, 1141, 821))
        font = QFont()
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 20, 301, 61))
        font1 = QFont()
        font1.setPointSize(30)
        self.label.setFont(font1)
        self.txt_nomecompleto = QLabel(self.frame)
        self.txt_nomecompleto.setObjectName(u"txt_nomecompleto")
        self.txt_nomecompleto.setGeometry(QRect(60, 150, 141, 16))
        self.txt_nomecompleto.setFont(font)
        self.line_nomecompleto = QLineEdit(self.frame)
        self.line_nomecompleto.setObjectName(u"line_nomecompleto")
        self.line_nomecompleto.setGeometry(QRect(220, 150, 591, 22))
        self.txt_cpf = QLabel(self.frame)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setGeometry(QRect(160, 180, 49, 16))
        self.txt_cpf.setFont(font)
        self.line_cpf = QLineEdit(self.frame)
        self.line_cpf.setObjectName(u"line_cpf")
        self.line_cpf.setGeometry(QRect(220, 180, 261, 22))
        self.txt_endereco = QLabel(self.frame)
        self.txt_endereco.setObjectName(u"txt_endereco")
        self.txt_endereco.setEnabled(True)
        self.txt_endereco.setGeometry(QRect(120, 210, 91, 16))
        self.txt_endereco.setFont(font)
        self.line_endereco = QLineEdit(self.frame)
        self.line_endereco.setObjectName(u"line_endereco")
        self.line_endereco.setGeometry(QRect(220, 210, 421, 22))
        self.txt_tel = QLabel(self.frame)
        self.txt_tel.setObjectName(u"txt_tel")
        self.txt_tel.setGeometry(QRect(130, 240, 91, 16))
        self.txt_tel.setFont(font)
        self.line_tel = QLineEdit(self.frame)
        self.line_tel.setObjectName(u"line_tel")
        self.line_tel.setGeometry(QRect(220, 240, 411, 22))
        self.radioButton_Masculino = QRadioButton(self.frame)
        self.radioButton_Masculino.setObjectName(u"radioButton_Masculino")
        self.radioButton_Masculino.setGeometry(QRect(210, 320, 89, 20))
        self.radioButton_Feminino = QRadioButton(self.frame)
        self.radioButton_Feminino.setObjectName(u"radioButton_Feminino")
        self.radioButton_Feminino.setGeometry(QRect(210, 350, 89, 20))
        self.radioButton_Outro = QRadioButton(self.frame)
        self.radioButton_Outro.setObjectName(u"radioButton_Outro")
        self.radioButton_Outro.setGeometry(QRect(210, 380, 89, 20))
        self.pushButton_Finalizar = QPushButton(self.frame)
        self.pushButton_Finalizar.setObjectName(u"pushButton_Finalizar")
        self.pushButton_Finalizar.setGeometry(QRect(870, 723, 171, 61))
        self.pushButton_Finalizar.setFont(font)
        self.pushButton_Finalizar.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        self.txt_sexo = QLabel(self.frame)
        self.txt_sexo.setObjectName(u"txt_sexo")
        self.txt_sexo.setGeometry(QRect(150, 320, 49, 16))
        self.txt_sexo.setFont(font)
        self.checkBox_Sim = QCheckBox(self.frame)
        self.checkBox_Sim.setObjectName(u"checkBox_Sim")
        self.checkBox_Sim.setGeometry(QRect(120, 590, 76, 20))
        self.checkBox_Sim.setFont(font)
        self.txt_pergunta_condicao_FISICA = QLabel(self.frame)
        self.txt_pergunta_condicao_FISICA.setObjectName(u"txt_pergunta_condicao_FISICA")
        self.txt_pergunta_condicao_FISICA.setGeometry(QRect(120, 550, 571, 31))
        self.txt_pergunta_condicao_FISICA.setFont(font)
        self.checkBox_Nao = QCheckBox(self.frame)
        self.checkBox_Nao.setObjectName(u"checkBox_Nao")
        self.checkBox_Nao.setGeometry(QRect(210, 590, 76, 20))
        self.checkBox_Nao.setFont(font)
        self.txt_Data_nascimento = QLabel(self.frame)
        self.txt_Data_nascimento.setObjectName(u"txt_Data_nascimento")
        self.txt_Data_nascimento.setGeometry(QRect(80, 470, 181, 16))
        self.txt_Data_nascimento.setFont(font)
        self.dateEdit_data_nascimento = QDateEdit(self.frame)
        self.dateEdit_data_nascimento.setObjectName(u"dateEdit_data_nascimento")
        self.dateEdit_data_nascimento.setGeometry(QRect(270, 470, 110, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1137, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Formul\u00e1rio", None))
        self.txt_nomecompleto.setText(QCoreApplication.translate("MainWindow", u"Nome completo:", None))
        self.txt_cpf.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.txt_endereco.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.txt_tel.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.radioButton_Masculino.setText(QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.radioButton_Feminino.setText(QCoreApplication.translate("MainWindow", u"Feminino", None))
        self.radioButton_Outro.setText(QCoreApplication.translate("MainWindow", u"Outro", None))
        self.pushButton_Finalizar.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
        self.txt_sexo.setText(QCoreApplication.translate("MainWindow", u"Sexo:", None))
        self.checkBox_Sim.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.txt_pergunta_condicao_FISICA.setText(QCoreApplication.translate("MainWindow", u"Possui alguma condi\u00e7\u00e3o f\u00edsica que o impe\u00e7a de realizar atividades?", None))
        self.checkBox_Nao.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.txt_Data_nascimento.setText(QCoreApplication.translate("MainWindow", u"Data de Nascimento:", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([]) 
    mainWindow = QMainWindow()  
    ui = Ui_MainWindow()  
    ui.setupUi(mainWindow)  
    mainWindow.show()  
    app.exec()  