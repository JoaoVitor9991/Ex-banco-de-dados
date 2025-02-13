import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame, QLabel, QLineEdit, QMenuBar, QPushButton, QWidget, QVBoxLayout, QStatusBar
)
from PySide6.QtGui import QFont

class Ui_LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("LoginForm")
        self.resize(800, 600)

        layout = QVBoxLayout(self)

        self.txt_login = QLabel("Login", self)
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        self.txt_login.setFont(font)
        self.txt_login.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.txt_login)

        self.txt_email = QLabel("E-mail:", self)
        layout.addWidget(self.txt_email)

        self.line_email = QLineEdit(self)
        layout.addWidget(self.line_email)

        self.txt_senha = QLabel("Senha", self)
        layout.addWidget(self.txt_senha)

        self.line_senha = QLineEdit(self)
        self.line_senha.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.line_senha)

        self.pushButton_Entrar = QPushButton("Entrar", self)
        layout.addWidget(self.pushButton_Entrar)

        self.pushButton_Entrar.clicked.connect(self.on_login)

    def on_login(self):
        # For simplicity, you can check if the login data is correct
        # and then switch to the main form.
        self.parent().setCurrentIndex(1)  # Switch to the main form

class Ui_MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainForm")
        self.resize(1137, 840)

        layout = QVBoxLayout(self)

        self.frame = QFrame(self)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        layout.addWidget(self.frame)

        self.label = QLabel("Formulário", self.frame)
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.frame.layout().addWidget(self.label)

        self.txt_nomecompleto = QLabel("Nome completo:", self.frame)
        self.frame.layout().addWidget(self.txt_nomecompleto)

        self.line_nomecompleto = QLineEdit(self.frame)
        self.frame.layout().addWidget(self.line_nomecompleto)

        # Add more widgets for CPF, address, etc., as in the original code.

        self.pushButton_Finalizar = QPushButton("Finalizar", self.frame)
        self.frame.layout().addWidget(self.pushButton_Finalizar)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulário")

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        self.login_form = Ui_LoginForm()
        self.main_form = Ui_MainForm()

        self.stacked_widget.addWidget(self.login_form)
        self.stacked_widget.addWidget(self.main_form)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
