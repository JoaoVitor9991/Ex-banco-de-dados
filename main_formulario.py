import sys 
from PySide6.QtWidgets import QApplication
from formulario import login_formulario

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = login_formulario()
    window.show()
    sys.exit(app.exec())