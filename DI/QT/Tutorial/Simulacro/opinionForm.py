import sys

from PyQt6.QtCore import QDateTime, QDate, Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QFormLayout, QGridLayout, QLineEdit, \
    QDateEdit, QDataWidgetMapper, QPushButton, QHBoxLayout, QButtonGroup, QRadioButton, QTextEdit, QSpacerItem, \
    QSizePolicy


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario de contacto")


        # ESTRUCTURA CONTENEDORES
        container = QWidget()
        self.mainLayout = QVBoxLayout()
        self.formLayout = QFormLayout()

        self.hbox_colores = QHBoxLayout() # Dentro del formulario
        self.colores_group = QButtonGroup() # Dentro del hbox_colores
        self.hboxBotonesSubmit = QHBoxLayout()


        #HBOX BOTONES PIE
        self.btn_enviar = QPushButton("Enviar")
        self.btn_cancelar = QPushButton("salir")

        self.hboxBotonesSubmit.addWidget(self.btn_enviar)
        self.hboxBotonesSubmit.addWidget(self.btn_cancelar)



        # CAMPOS FORMULARIOS
        self.input_nombre = self.input()
        self.input_apellido1 = self.input()
        self.input_apellido2 = self.input()
        self.input_direccion = self.input()
        self.input_cp = self.input()
        self.fechaNac = QDateEdit()
        self.fechaNac.setCalendarPopup(True)
        self.fechaNac.setDate(QDate.currentDate())
        self.fechaNac.setDisplayFormat("dd/MM/yyyy")
        self.fechaNac.setMaximumWidth(100)
        self.radioButtonRed = self.createRadioButton("Red", self.colores_group)
        self.radioButtonGreen = self.createRadioButton("Green", self.colores_group)
        self.radioButtonPink = self.createRadioButton("Pink", self.colores_group)
        self.textEdit = QTextEdit()
        self.textEdit.setPlaceholderText("Escribe aquí")
        self.textEdit.setFixedSize(300,100)

        self.btn_mostrarColor = QPushButton()
        self.btn_mostrarColor.setMinimumWidth(200)
        self.btn_mostrarColor.setMinimumHeight(100)

        # COLORES
        self.hbox_colores.addWidget(self.radioButtonRed)
        self.hbox_colores.addWidget(self.radioButtonGreen)
        self.hbox_colores.addWidget(self.radioButtonPink)


        # ESTRUCTURA FORMULARIO
        self.formLayout.addRow("Nombre", self.input_nombre)
        self.formLayout.addRow("Primer Apellido", self.input_apellido1)
        self.formLayout.addRow("Segundo Apellido", self.input_apellido2)
        self.formLayout.addRow("Código Postal", self.input_cp)
        self.formLayout.addRow("Fecha de Nacimiento", self.fechaNac)
        self.formLayout.addRow("Esto es un boton rojo", self.buttonColor("red"))
        self.formLayout.addRow("Elige un color", self.hbox_colores)
        self.formLayout.addRow(self.btn_mostrarColor)
        self.formLayout.setAlignment(self.btn_mostrarColor, Qt.AlignmentFlag.AlignHCenter)
        self.formLayout.addRow("Sugerencias", self.textEdit)

        self.mainLayout.addLayout(self.formLayout)
        self.mainLayout.addLayout(self.hboxBotonesSubmit)
        container.setLayout(self.mainLayout)
        self.setCentralWidget(container)


    def input(self):
        input = QLineEdit()
        input.setMaximumWidth(100)
        return input

    def buttonColor(self, color):
        button = QPushButton(f"Botón {color}")
        palette = button.palette()
        palette.setColor(QPalette.ColorRole.Button, QColor(color))
        button.setPalette(palette)
        button.setMaximumWidth(100)
        button.setEnabled(False)
        return button

    def createRadioButton(self, color, groupButtons):
        radioButton = QRadioButton(color)
        groupButtons.addButton(radioButton)
        radioButton.clicked.connect(self.get_checked_radio_button)
        return radioButton

    def get_checked_radio_button(self):
        checked_button = self.colores_group.checkedButton()
        if checked_button:
            print(f"El radio button seleccionado es: {checked_button.text()}")
            self.btn_mostrarColor.setStyleSheet(f"background-color: {checked_button.text()} ;")

        else:
            print("No hay ningún radio button seleccionado")




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()