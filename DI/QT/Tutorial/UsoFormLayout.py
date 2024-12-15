import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QFormLayout, QLineEdit,
    QComboBox, QCheckBox, QPushButton, QVBoxLayout
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formulario de Ejemplo")
        self.setGeometry(100, 100, 300, 200)

        # Crear el layout principal
        main_layout = QVBoxLayout()

        # Crear un formulario con QFormLayout
        self.form_layout = QFormLayout()

        # Añadir campos al formulario y guardar referencias
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.country_combobox = QComboBox()
        self.country_combobox.addItems(["España", "México", "Argentina", "Colombia"])
        self.subscribe_checkbox = QCheckBox()

        self.form_layout.addRow("Nombre:", self.name_input)
        self.form_layout.addRow("Email:", self.email_input)
        self.form_layout.addRow("País:", self.country_combobox)
        self.form_layout.addRow("Suscribirse:", self.subscribe_checkbox)

        # Botón de enviar
        submit_button = QPushButton("Enviar")
        submit_button.clicked.connect(self.on_submit)

        # Añadir el formulario y el botón al layout principal
        main_layout.addLayout(self.form_layout)
        main_layout.addWidget(submit_button)

        # Configurar el layout principal en el contenedor central
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def on_submit(self):
        # Acceder a los campos usando las referencias guardadas
        print(f"Nombre: {self.name_input.text()}")
        print(f"Email: {self.email_input.text()}")
        print(f"País: {self.country_combobox.currentText()}")
        print(f"Suscribirse: {self.subscribe_checkbox.isChecked()}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
