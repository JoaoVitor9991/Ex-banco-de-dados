

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(926, 845)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.nome_txt = QFrame(self.centralwidget)
        self.nome_txt.setObjectName(u"nome_txt")
        self.nome_txt.setGeometry(QRect(60, 0, 801, 701))
        self.nome_txt.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.nome_txt.setFrameShape(QFrame.Shape.StyledPanel)
        self.nome_txt.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_formulario = QLabel(self.nome_txt)
        self.txt_formulario.setObjectName(u"txt_formulario")
        self.txt_formulario.setEnabled(True)
        self.txt_formulario.setGeometry(QRect(270, 10, 221, 61))
        font = QFont()
        font.setFamilies([u"Segoe UI Symbol"])
        font.setPointSize(28)
        self.txt_formulario.setFont(font)
        self.label_2 = QLabel(self.nome_txt)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 110, 71, 20))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.nome_line = QLineEdit(self.nome_txt)
        self.nome_line.setObjectName(u"nome_line")
        self.nome_line.setGeometry(QRect(160, 110, 531, 22))
        self.cpf_txt = QLabel(self.nome_txt)
        self.cpf_txt.setObjectName(u"cpf_txt")
        self.cpf_txt.setGeometry(QRect(60, 150, 49, 16))
        self.cpf_txt.setFont(font1)
        self.cpf_line = QLineEdit(self.nome_txt)
        self.cpf_line.setObjectName(u"cpf_line")
        self.cpf_line.setGeometry(QRect(160, 150, 281, 22))
        self.Endereo_txt = QLabel(self.nome_txt)
        self.Endereo_txt.setObjectName(u"Endereo_txt")
        self.Endereo_txt.setGeometry(QRect(50, 290, 91, 31))
        self.Endereo_txt.setFont(font1)
        self.Endereo_line = QLineEdit(self.nome_txt)
        self.Endereo_line.setObjectName(u"Endereo_line")
        self.Endereo_line.setGeometry(QRect(160, 300, 531, 22))
        self.radioButton_Masculino = QRadioButton(self.nome_txt)
        self.radioButton_Masculino.setObjectName(u"radioButton_Masculino")
        self.radioButton_Masculino.setGeometry(QRect(110, 190, 91, 20))
        self.radioButton_Feminino = QRadioButton(self.nome_txt)
        self.radioButton_Feminino.setObjectName(u"radioButton_Feminino")
        self.radioButton_Feminino.setGeometry(QRect(220, 190, 89, 20))
        self.radioButton_Outro = QRadioButton(self.nome_txt)
        self.radioButton_Outro.setObjectName(u"radioButton_Outro")
        self.radioButton_Outro.setGeometry(QRect(310, 190, 89, 20))
        self.txt_sexo = QLabel(self.nome_txt)
        self.txt_sexo.setObjectName(u"txt_sexo")
        self.txt_sexo.setGeometry(QRect(60, 190, 49, 16))
        self.txt_sexo.setFont(font1)
        self.Tel_txt = QLabel(self.nome_txt)
        self.Tel_txt.setObjectName(u"Tel_txt")
        self.Tel_txt.setGeometry(QRect(50, 340, 71, 16))
        self.Tel_txt.setFont(font1)
        self.Tel_line = QLineEdit(self.nome_txt)
        self.Tel_line.setObjectName(u"Tel_line")
        self.Tel_line.setGeometry(QRect(160, 340, 531, 22))
        self.Data_nasciment_txt = QLabel(self.nome_txt)
        self.Data_nasciment_txt.setObjectName(u"Data_nasciment_txt")
        self.Data_nasciment_txt.setGeometry(QRect(10, 380, 151, 16))
        self.Data_nasciment_txt.setFont(font1)
        self.DataNascimento_data = QDateEdit(self.nome_txt)
        self.DataNascimento_data.setObjectName(u"DataNascimento_data")
        self.DataNascimento_data.setGeometry(QRect(160, 380, 110, 22))
        self.checkBox_Sim = QCheckBox(self.nome_txt)
        self.checkBox_Sim.setObjectName(u"checkBox_Sim")
        self.checkBox_Sim.setGeometry(QRect(200, 470, 76, 20))
        self.checkBox_Sim.setFont(font1)
        self.txt_checkbox = QLabel(self.nome_txt)
        self.txt_checkbox.setObjectName(u"txt_checkbox")
        self.txt_checkbox.setGeometry(QRect(10, 430, 471, 21))
        self.txt_checkbox.setFont(font1)
        self.checkBox_Nao = QCheckBox(self.nome_txt)
        self.checkBox_Nao.setObjectName(u"checkBox_Nao")
        self.checkBox_Nao.setGeometry(QRect(370, 470, 76, 20))
        self.checkBox_Nao.setFont(font1)
        self.email_txt = QLabel(self.nome_txt)
        self.email_txt.setObjectName(u"email_txt")
        self.email_txt.setGeometry(QRect(60, 230, 49, 16))
        self.email_txt.setFont(font1)
        self.email_line = QLineEdit(self.nome_txt)
        self.email_line.setObjectName(u"email_line")
        self.email_line.setGeometry(QRect(160, 230, 391, 22))
        self.Avanar_btn = QPushButton(self.nome_txt)
        self.Avanar_btn.setObjectName(u"Avanar_btn")
        self.Avanar_btn.setGeometry(QRect(600, 650, 161, 41))
        self.Avanar_btn.setFont(font1)
        self.Avanar_btn.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 926, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_formulario.setText(QCoreApplication.translate("MainWindow", u"Formul\u00e1rio", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.cpf_txt.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.Endereo_txt.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.radioButton_Masculino.setText(QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.radioButton_Feminino.setText(QCoreApplication.translate("MainWindow", u"Feminino", None))
        self.radioButton_Outro.setText(QCoreApplication.translate("MainWindow", u"Outro", None))
        self.txt_sexo.setText(QCoreApplication.translate("MainWindow", u"Sexo:", None))
        self.Tel_txt.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.Data_nasciment_txt.setText(QCoreApplication.translate("MainWindow", u"Data de Nascimento:", None))
        self.checkBox_Sim.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.txt_checkbox.setText(QCoreApplication.translate("MainWindow", u"Voc\u00ea tem alguma limita\u00e7\u00e3o que impe\u00e7a a realiza\u00e7\u00e3o de atividades?", None))
        self.checkBox_Nao.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.email_txt.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.Avanar_btn.setText(QCoreApplication.translate("MainWindow", u"Avan\u00e7ar", None))
    # retranslateUi

