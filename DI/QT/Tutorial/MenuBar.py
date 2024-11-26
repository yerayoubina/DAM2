import sys
import PyQt6.QtWidgets
from PyQt6.QtGui import QAction


class MainWindow(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana con Menú")
        self.setGeometry(100, 100, 600, 400)

        # Crear la barra de menús
        menu_bar = self.menuBar()

        # Agregar menús
        archivo_menu = menu_bar.addMenu("Archivo")
        ayuda_menu = menu_bar.addMenu("Ayuda")

        # Crear acciones para el menú "Archivo"
        nueva_accion = QAction("Nuevo", self)
        abrir_accion = QAction("Abrir", self)
        salir_accion = QAction("Salir", self)

        #Conecta el QAction con cerrar
        salir_accion.triggered.connect(self.close)  # Cierra la ventana

        # Agregar acciones al menú "Archivo"
        archivo_menu.addAction(nueva_accion)
        archivo_menu.addAction(abrir_accion)
        archivo_menu.addSeparator()  # Línea divisoria
        archivo_menu.addAction(salir_accion)

        # Crear acción para el menú "Ayuda"
        acerca_accion = QAction("Acerca de", self)
        ayuda_menu.addAction(acerca_accion)

        # Conectar la acción "Acerca de" a un mensaje
        acerca_accion.triggered.connect(self.mostrar_acerca_de)

    def mostrar_acerca_de(self):
        print("Esta es una aplicación PyQt6 básica.")


app = PyQt6.QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
