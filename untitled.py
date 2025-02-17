# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import icon_rc
from conecaoBD import conectar
import mysql.connector
from PyQt5.QtWidgets import QMessageBox

def validar(email, senha):
    conexao = conectar()

    if conexao is None:
        return None
    
    cursor = conexao.cursor()

    sql_verificar = 'SELECT id FROM usuario WHERE email=%s'
    cursor.execute(sql_verificar, (email,))
    resultado = cursor.fetchone()

    if resultado:
        print("Login Bem sucedido")
        return resultado[0]
    else:
        try:
            sql_inserir= "INSERTO INTO usuario (email, senha) VALUES (%s, %s)"
            valores = (email, senha)
            cursor.execute(sql_inserir, valores)
            conexao.commit()
            print("Usuario criado e logado.")
            return cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return None
        finally:
            cursor.close()
            conexao.close()
class Ui_TelaLogin(object):
    def setupUi(self, TelaLogin):
        if not TelaLogin.objectName():
            TelaLogin.setObjectName(u"TelaLogin")
        TelaLogin.resize(800, 565)
        self.centralwidget = QWidget(TelaLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -20, 811, 741))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_Login = QLabel(self.frame)
        self.txt_Login.setObjectName(u"txt_Login")
        self.txt_Login.setGeometry(QRect(160, 90, 221, 81))
        font = QFont()
        font.setFamilies([u"Palatino Linotype"])
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(True)
        self.txt_Login.setFont(font)
        self.txt_Login.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.txt_senha_2 = QLabel(self.frame)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setGeometry(QRect(30, 210, 49, 16))
        font1 = QFont()
        font1.setPointSize(12)
        self.txt_senha_2.setFont(font1)
        self.lineEdit_email = QLineEdit(self.frame)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(100, 210, 271, 22))
        self.txt_senha = QLabel(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(30, 270, 49, 16))
        self.txt_senha.setFont(font1)
        self.lineEdit__senha = QLineEdit(self.frame)
        self.lineEdit__senha.setObjectName(u"lineEdit__senha")
        self.lineEdit__senha.setGeometry(QRect(100, 270, 271, 22))
        self.lineEdit__senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton_entrar = QPushButton(self.frame)
        self.pushButton_entrar.setObjectName(u"pushButton_entrar")
        self.pushButton_entrar.setGeometry(QRect(170, 330, 121, 51))
        self.pushButton_entrar.setStyleSheet(u"background-color: rgb(111, 255, 44);")
        self.img = QLabel(self.frame)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(460, 90, 341, 241))
        self.img.setPixmap(QPixmap(u":/f/imagem.jpg"))
        TelaLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaLogin)

        QMetaObject.connectSlotsByName(TelaLogin)
    # setupUi

    def retranslateUi(self, TelaLogin):
        TelaLogin.setWindowTitle(QCoreApplication.translate("TelaLogin", u"MainWindow", None))
        self.txt_Login.setText(QCoreApplication.translate("TelaLogin", u"Login", None))
        self.txt_senha_2.setText(QCoreApplication.translate("TelaLogin", u"E-mail:", None))
        self.txt_senha.setText(QCoreApplication.translate("TelaLogin", u"Senha:", None))
        self.pushButton_entrar.setText(QCoreApplication.translate("TelaLogin", u"Entrar", None))
        self.img.setText("")
    # retranslateUi

