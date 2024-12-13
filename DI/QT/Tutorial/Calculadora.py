import sys

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QGridLayout, QPushButton, QVBoxLayout, QWidget, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Título
        self.setWindowTitle("Calculadora")
        self.setGeometry(50,50,200,200)

        #Elementos
        container = QWidget()
        boxV = QVBoxLayout()
        self.grid = QGridLayout()
        self.labelText = QLabel("texto de prueba")
        


        # Estructurar grid
        self.grid.addWidget(self.addButton(1),0,0,1,1)
        self.grid.addWidget(self.addButton(2),0,0,2,4)

        boxV.addWidget(self.labelText)
        boxV.addLayout(self.grid)
        container.setLayout(boxV)
        self.setCentralWidget(container)


    def addButton(self, name):
        return QPushButton(f"Botón {name}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()