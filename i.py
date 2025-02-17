import sys 
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
#from PySide6.QtGui Import QPixmap 
#from ui_tela import Ui_form 

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #self.ui = Ui_form()
        self.ui.setup(self)

    def open_image(self):
        file_dialog =QFileDialog()
        file_path, = file_dialog.getOpenFileName(self, "open image ", "images(*.png *.jpg*jpeg);;all Files (*)")

        if file_path:
           # pixmap =Qpixmap(file_path)
            #self.ui.image.setPixmap(pixmap)
            self.ui.image.setScaledContentes(True)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())