def upload_foto(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(None, "Escolha uma foto", "", "Imagens (*.png *.jpg *.bmp *.jpeg)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.lbl_foto.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))

            self.photo_path = file_name  # Save the path of the image