import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox


class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Primera Ventana")
        self.setGeometry(100,100,400,400)

        # Crear un botón
        self.boton = QPushButton("Presióname", self)
        self.boton.setGeometry(150, 120, 100, 40)  # x, y, ancho, alto

        # Conectar el botón a una función
        self.boton.clicked.connect(self.mostrar_mensaje)

    def mostrar_mensaje(self):
            QMessageBox.information(self, "Mensaje", "¡Hola, PyQt6!")


app = QApplication(sys.argv)
window = FirstWindow()
window.show()
app.exec()

