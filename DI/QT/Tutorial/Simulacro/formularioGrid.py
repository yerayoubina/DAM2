import sys

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QApplication, QMainWindow, \
    QLabel, QRadioButton, QButtonGroup, QFrame



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Grid Form")

        # EJEMPLOS CONEXIONES
        """
        # Conectar el botón a la función on_click
            self.button.clicked.connect(self.on_click)
            
        # Conectar el QLineEdit a la función on_text_changed
        self.line_edit.textChanged.connect(self.on_text_changed)
        
        # Conectar el QCheckBox a la función on_checkbox_toggled
        self.checkbox.toggled.connect(self.on_checkbox_toggled)
        
        # Conectar el QSlider a la función on_slider_value_changed
        self.slider.valueChanged.connect(self.on_slider_value_changed)
        
        # Conectar el QComboBox a la función on_index_changed
        self.combo_box.currentIndexChanged.connect(self.on_index_changed)
        """

        #CONTENEDORES
        container = QWidget()
        # self.setStyleSheet("border: 2px solid black;")

        self.mainLayout = QVBoxLayout()
        self.gridLayout = QGridLayout()
        self.formLayout = QFormLayout()

        #LABELS FORM
        self.input_nombre = self.createInput()
        self.input_apellido = self.createInput()
        self.input_direccion = self.createInput()
        self.input_edad = self.createInput()

        #CONEXIONES LABEL
        self.input_nombre.textChanged.connect(self.imprimirLabels)
        # FORM
        self.formLayout.addRow("Nombre", self.input_nombre)
        self.formLayout.addRow("Apellido", self.input_apellido)
        self.formLayout.addRow("Direccion", self.input_direccion)
        self.formLayout.addRow("Edad", self.input_edad)

        # RadioButtons group
        self.grupo_colores = QButtonGroup()
        self.radioButtonRed = self.radioButtonColor("Rojo")
        self.radioButtonGreen = self.radioButtonColor("Verde")
        self.radioButtonAzul = self.radioButtonColor("Azul")



        # GRID STRUCTURE
        self.gridLayout.addWidget(QLabel("Datos Personales"),0,0,1,1)
        self.gridLayout.addWidget(self.separador(), 1,0,1,4)
        self.gridLayout.addLayout(self.formLayout,2,0,4,2)
        self.gridLayout.addWidget(QLabel("Elige un color"), 7,0,1,1)
        self.gridLayout.addWidget(self.separador(), 6,0,1,4)
        self.gridLayout.addWidget(self.radioButtonRed, 7,1,1,1)
        self.gridLayout.addWidget(self.radioButtonGreen, 7,2,1,1)
        self.gridLayout.addWidget(self.radioButtonAzul, 7,3,1,1)




        # MAIN LAYOUT STRUCTURE
        self.mainLayout.addLayout(self.gridLayout)

        container.setLayout(self.mainLayout)
        self.setCentralWidget(container)

    def separador(self):
        separator = QFrame(self)
        separator.setFrameShape(QFrame.Shape.HLine)
        return separator

    def radioButtonColor(self, strColor):
        radioButton = QRadioButton(f"{strColor}")
        self.grupo_colores.addButton(radioButton)
        return radioButton

    def createInput(self, placeholder = ""):
        input = QLineEdit(f"{placeholder}")
        input.setMinimumWidth(100)
        return input

    def imprimirLabels(self):
        texto = self.input_nombre.text()
        print(texto)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
