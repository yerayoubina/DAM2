import sys

from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QTableView, QHBoxLayout, QLineEdit, QComboBox, QCheckBox, QPushButton

from Taboa.ModeloTaboa import ModeloTaboa


class ExemploQTableView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo de QTableView")

        # Datos de la tabla
        self.datos = [
            ['Nome', 'Dni', 'Xénero', 'Falecido'],
            ['Ana Perez', '5455445', 'Muller', False],
            ['Paco Porras', '8888677845', 'Home', True],
            ['Roque Vila', '3324556', 'Home', False],
            ['Lina Morgan', '11234909', 'Muller', True],
        ]

        # Layouts principales
        cajav = QVBoxLayout()
        cajah = QHBoxLayout()
        cajahBotones = QHBoxLayout()
        cajav.addLayout(cajah)
        cajav.addLayout(cajahBotones)

        # Widgets para la edición
        self.txtNome = QLineEdit()
        cajah.addWidget(self.txtNome)
        self.txtDni = QLineEdit()
        cajah.addWidget(self.txtDni)
        self.cmbXenero = QComboBox()
        self.cmbXenero.addItems(('Home', 'Muller', 'Outro'))
        cajah.addWidget(self.cmbXenero)
        self.chkFalecido = QCheckBox('Falecido')
        cajah.addWidget(self.chkFalecido)

        # BOTONES
        self.btnAñadir = QPushButton("Añadir")
        self.btnBorrar = QPushButton("Borrar")
        self.btnEditar = QPushButton("Editar")

        cajahBotones.addWidget(self.btnAñadir)
        cajahBotones.addWidget(self.btnBorrar)
        cajahBotones.addWidget(self.btnEditar)

        # Vista de la tabla
        self.tvwTaboa = QTableView()
        modelo = ModeloTaboa(self.datos)
        self.tvwTaboa.setModel(modelo)
        self.tvwTaboa.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.tvwTaboa.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)

        # Conectar señal de selección con el método
        self.tvwTaboa.selectionModel().selectionChanged.connect(self.on_selection_changed)

        # Conectar el botón Añadir
        #self.btnAñadir.clicked.connect(self.on_btnAñadir)

        # Añadir la tabla al layout
        cajav.addWidget(self.tvwTaboa)

        # Configurar el widget central
        container = QWidget()
        container.setLayout(cajav)
        self.setCentralWidget(container)
        self.setFixedSize(400, 300)

    def on_selection_changed(self, selected, deselected):
        indices = self.tvwTaboa.selectionModel().selectedIndexes()
        if indices:
            row = indices[0].row()
            self.txtNome.setText(self.datos[row][0])
            self.txtDni.setText(self.datos[row][1])
            self.cmbXenero.setCurrentText(self.datos[row][2])
            self.chkFalecido.setChecked(self.datos[row][3])

    '''def on_btnAñadir(self):
        nome = self.txtNome.text()
        dni = self.txtDni.text()
        xenero = self.cmbXenero.currentText()
        falecido = self.chkFalecido.isChecked()

        if not nome or not dni:
            print("Por favor, rellena todos los campos obligatorios.")
            return

        nuevo_registro = [nome, dni, xenero, falecido]
        self.tvwTaboa.model().add_row(nuevo_registro)

        self.txtNome.clear()
        self.txtDni.clear()
        self.cmbXenero.setCurrentIndex(0)
        self.chkFalecido.setChecked(False)

    '''

app = QApplication(sys.argv)
ventana = ExemploQTableView()
ventana.show()
app.exec()
