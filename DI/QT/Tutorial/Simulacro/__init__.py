import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QFormLayout, QLineEdit, QWidget, QApplication, QComboBox, \
    QCheckBox, QRadioButton, QHBoxLayout, QGridLayout, QLabel, QListWidget, QPushButton, QMessageBox, QButtonGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen")
        self.setFixedSize(400,400)

    # contenedores
        container = QWidget()
        self.mainLayout = QVBoxLayout()
        self.formLayoutDatos = QFormLayout()
        self.HboxRadioButtons = QHBoxLayout()
        self.gridLayoutTareas = QGridLayout()

    # QLineEdits
        self.input_Nome = QLineEdit()
        self.input_Apellido = QLineEdit()
        self.input_Tratamiento = QComboBox()
        self.input_Tratamiento.addItems(["Sr", "Sra"])
        self.input_Usuario = QLineEdit()
        self.input_Edad = QCheckBox("Mayor de 18 años")
        self.input_Terminos = QRadioButton("Acepta los terminos")
        self.input_Terminos.setChecked(True)
        self.input_email = QLineEdit()





        self.HboxRadioButtons.addWidget(self.input_Edad)
        self.HboxRadioButtons.addWidget(self.input_Terminos)

    # QFormLayoutDatos
        self.formLayoutDatos.addRow("Nombre: ", self.input_Nome)
        self.formLayoutDatos.addRow("Apellido: ", self.input_Apellido)
        self.formLayoutDatos.addRow("Tratamiento: ", self.input_Tratamiento)
        self.formLayoutDatos.addRow("Usuario: ", self.input_Usuario)
        self.formLayoutDatos.addRow(self.HboxRadioButtons)
        self.formLayoutDatos.addRow(self.gridLayoutTareas)

    # Elementos Grid
        self.labelTitutloTareas = QLabel("TAREAS")
        #self.labelTitutloTareas.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.gridLayoutTareas.setContentsMargins(0,20,0,0)
        self.tareasList = QListWidget()
        self.input_email.setPlaceholderText("Introduce el email")
        self.btn_add = QPushButton("Añadir")
        self.btn_edit = QPushButton("Editar")
        self.btn_delete = QPushButton("Borrar")


        self.button_group = QButtonGroup()
        self.radio1 = QRadioButton("HTML")
        self.radio2 = QRadioButton("Texto Plano")
        self.radio3 = QRadioButton("Personalizado")
        self.button_group.addButton(self.radio1)
        self.button_group.addButton(self.radio2)
        self.button_group.addButton(self.radio3)


    # Posicionamiento grid
        self.gridLayoutTareas.addWidget(self.labelTitutloTareas,0,1,1,3)
        self.gridLayoutTareas.addWidget(self.tareasList,1,0,5,3)
        self.gridLayoutTareas.addWidget(self.btn_add, 1,3)
        self.gridLayoutTareas.addWidget(self.btn_edit, 2,3)
        self.gridLayoutTareas.addWidget(self.btn_delete, 3,3)
        self.gridLayoutTareas.addWidget(self.radio1,4,3)
        self.gridLayoutTareas.addWidget(self.radio2,5,3)
        self.gridLayoutTareas.addWidget(self.radio3,6,3)

        self.gridLayoutTareas.addWidget(self.input_email, 6, 0, 1, 2)

    # Conexiones btn
        self.btn_add.clicked.connect(self.btn_anadir)
        self.btn_edit.clicked.connect(self.btn_editar)
        self.btn_delete.clicked.connect(self.btn_borrar)

    # Conectar la lista de tareas para que llame al método cuando se seleccione un item
        self.tareasList.itemClicked.connect(self.observerFields)


        self.mainLayout.addLayout(self.formLayoutDatos)
        container.setLayout(self.mainLayout)
        self.setCentralWidget(container)


    # FUNCIONES
    def btn_anadir(self):
        user = self.createUser()
        if user is None:
            print("campo vacio")
            self.Info("No se puede añadir usuario sin datos")
        else:
            self.tareasList.addItem(user.__toString__())
            self.clearField()


    def btn_editar(self):
        user = self.createUser()
        self.observerFields()
        if self.tareasList.currentItem() is None:
            self.Info("No hay ninguan usuario seleccionada para editar")
            return
        self.tareasList.currentItem().setText(user.__toString__())
        self.clearField()
        self.tareasList.clearSelection()

    def btn_borrar(self):
        if self.tareasList.currentItem() is None:
            self.Info("No se ha seleccionado ninguna usuario")
            return

        self.tareasList.takeItem(self.tareasList.row(self.tareasList.currentItem()))


    def clearField(self):
        self.input_Nome.clear()
        self.input_email.clear()
        self.input_Apellido.clear()
        self.input_Usuario.clear()

    def createUser(self):
        return Usuario(self.input_Nome.text(), self.input_Apellido.text(), self.input_Usuario.text(),
        self.input_email.text())

    def Info(self, str):
        msg = QMessageBox()
        msg.setText(str)
        msg.setWindowTitle("Advertencia")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.exec()

    def observerFields(self):
        if self.tareasList.currentItem() is not None:
            user_data = self.tareasList.currentItem().text().split(', ')
            self.input_Nome.setText(user_data[0])
            self.input_Apellido.setText(user_data[1])
            self.input_Usuario.setText(user_data[2])
            self.input_email.setText(user_data[3])



class Usuario:
    def __init__(self, nombre, apellido, usuario, email):
            self.nombre = nombre
            self.apellido = apellido
            self.usuario = usuario
            self.email = email

    def __toString__(self):
        return f"{self.nombre}, {self.apellido}, {self.usuario}, {self.email}"

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()