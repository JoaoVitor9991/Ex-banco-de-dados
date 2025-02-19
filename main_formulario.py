import sys 
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from untitled import Ui_TelaLogin
from formulario import Ui_MainWindow
from conecaoBD import conectar
import mysql.connector 

def validar_login(email, senha):
    conexao = conectar()
    if conexao is None:
        return False
    cursor = conexao.cursor()

    sql = "SELECT * FROM usuario WHERE email = %s AND senha =%s"
    valores = (email, senha)

    cursor.execute(sql, valores)
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        print("Login Bem-sucedido!")
        return True
    else:
        print("Usuário ou senha inválidos!")
        return False
    


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.telaLogin = Ui_TelaLogin()
        self.telaLogin.setupUi(self)
        self.telaLogin.pushButton_entrar.clicked.connect(self.entrar)
    
    def entrar(self):
        email=  self.telaLogin.lineEdit_email.text() 
        senha = self.telaLogin.lineEdit__senha.text()
        if email and senha:
            if validar_login(email, senha):
                self.telaFormulario = Ui_MainWindow()
                self.telaFormulario.setupUi(self)
            else:
                print("Usuario ou senha invalidos")
        else:
            print("Preencha todos os campos.")


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

