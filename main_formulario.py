import sys 
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from untitled import Ui_TelaLogin
from formulario import Ui_MainWindow

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.telaLogin = Ui_TelaLogin()
        self.telaLogin.setupUi(self)
        self.telaLogin.pushButton_entrar.clicked.connect(self.entrar)
    
    def entrar(self):
        user = "admin"
        senha= "123"

        if self.telaLogin.lineEdit_email.text()== user:
            if self.telaLogin.lineEdit__senha.text() ==senha:
                self.telaFormulario = Ui_MainWindow()
                self.telaFormulario.setupUi(self)
                self.telaFormulario.pushButton_Finalizar.clicked.connect(self.finalizar_formulario)

    def finalizar_formulario(self):
        msg= QMessageBox()
        msg.setWindowTitle("Formulário Concluído! ")
        msg.setText("Formulário finalizado com sucesso.")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()


            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())

