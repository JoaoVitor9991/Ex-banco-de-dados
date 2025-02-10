
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("Cadastro")

        self.label_cpf = QLabel("CPF:")
        self.input_cpf = QLineEdit()
        self.input_cpf.setPlaceholderText("Digite seu CPF")

        self.label_name = QLabel("Nome Completo:")
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Digite seu nome")

        self.label_phone = QLabel("Telefone:")
        self.input_phone = QLineEdit()
        self.input_phone.setPlaceholderText("Digite seu telefone")

        self.button_submit = QPushButton("Finalizar Cadastro")
        self.button_submit.clicked.connect(self.submit_data)

        layout = QVBoxLayout()
        layout.addWidget(self.label_cpf)
        layout.addWidget(self.input_cpf)
        layout.addWidget(self.label_name)
        layout.addWidget(self.input_name)
        layout.addWidget(self.label_phone)
        layout.addWidget(self.input_phone)
        layout.addWidget(self.button_submit)

        self.setLayout(layout)

    def submit_data(self):
        cpf = self.input_cpf.text()
        name = self.input_name.text()
        phone = self.input_phone.text()
        print(f"Cadastro realizado: CPF={cpf}, Nome={name}, Telefone={phone}")

        