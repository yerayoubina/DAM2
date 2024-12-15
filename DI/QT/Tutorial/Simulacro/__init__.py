import sys
from inspect import trace
from tkinter.ttk import Combobox
from trace import Trace

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QFormLayout, QLineEdit, QWidget, QApplication, QComboBox, \
    QCheckBox, QRadioButton, QHBoxLayout, QGridLayout, QLabel, QListWidget, QPushButton, QMessageBox


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
        self.input_tareas = QLineEdit()





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
        self.input_tareas.setPlaceholderText("Añade una tarea")
        self.btn_add = QPushButton("Añadir")
        self.btn_edit = QPushButton("Editar")
        self.btn_delete = QPushButton("Borrar")

    # Posicionamiento grid
        self.gridLayoutTareas.addWidget(self.labelTitutloTareas,0,1,1,3)
        self.gridLayoutTareas.addWidget(self.tareasList,1,0,5,3)
        self.gridLayoutTareas.addWidget(self.btn_add, 1,3)
        self.gridLayoutTareas.addWidget(self.btn_edit, 2,3)
        self.gridLayoutTareas.addWidget(self.btn_delete, 3,3)
        self.gridLayoutTareas.addWidget(self.input_tareas,6,0,1,2)

    # Conexiones btn
        self.btn_add.clicked.connect(self.btn_anadir)
        self.btn_edit.clicked.connect(self.btn_editar)
        self.btn_delete.clicked.connect(self.btn_borrar)


        self.mainLayout.addLayout(self.gridLayoutTareas)
        self.mainLayout.addLayout(self.formLayoutDatos)
        container.setLayout(self.mainLayout)
        self.setCentralWidget(container)


    # FUNCIONES
    def btn_anadir(self):
        tarea = self.input_tareas.text()
        if tarea == '':
            print("campo vacio")
            self.Info("No se puede añadir tareas vacías")
        else:
            self.tareasList.addItem(tarea)
            self.input_tareas.clear()

    def Info(self, str):
        msg = QMessageBox()
        msg.setText(str)
        msg.setWindowTitle("Advertencia")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.exec()

    def btn_editar(self):
        tarea_seleccionada = self.tareasList.currentItem()

        if tarea_seleccionada is None:
            self.Info("No hay ninguan tarea seleccionada para editar")
            return
        tarea_seleccionada.setText(self.input_tareas.text())
        self.input_tareas.clear()

    def btn_borrar(self):
        if self.tareasList.currentItem() is None:
            self.Info("No se ha seleccionado ninguna tarea")
            return

        self.tareasList.takeItem(self.tareasList.row(self.tareasList.currentItem()))




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()