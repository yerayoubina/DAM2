import sys

from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QTableView

from Taboa.ModeloTaboa import ModeloTaboa


class ExemploQTableView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo de QtableView")

        self.datos = [['Nome', 'Dni', 'Xénero', 'Falecido', ],
                      ['Ana Perez', '5455445', 'Muller', False],
                      ['Paco Porras', '8888677845', 'Home', True],
                      ['Roque Vila', '3324556', 'Home', False],
                      ['Lina Morgan', '11234909', 'Muller', True]
                      ]

        cajav = QVBoxLayout()

        # VISTA TABLA
        self.tvwTaboa = QTableView()
        modelo = ModeloTaboa(self.datos)
        self.tvwTaboa.setModel(modelo)
        self.tvwTaboa.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        ''' cabecera = self.tvwTaboa.horizontalHeader()
        cabecera.setSectionResizeMode(self,)
        cabecera.setSectionResizeMode(1, 2)
        cabecera.setSectionResizeMode(2, 1)

        # Personalizar el texto de las cabeceras
        cabecera_modelo = self.tvwTaboa.model().headerData
        cabecera.setHeaderData(0, Qt.Orientation.Horizontal, "Nombre")
        cabecera.setHeaderData(1, Qt.Orientation.Horizontal, "DNI")
        cabecera.setHeaderData(2, Qt.Orientation.Horizontal, "Género")
        cabecera.setHeaderData(3, Qt.Orientation.Horizontal, "Fallecido") '''

        # AÑADIR TABLA AL LAYOUR
        cajav.addWidget(self.tvwTaboa)

        # Configurar el widget central con el layout
        container = QWidget()
        container.setLayout(cajav)
        self.setCentralWidget(container)
        self.setFixedSize(400, 300)


app = QApplication(sys.argv)
ventana = ExemploQTableView()
ventana.show()
app.exec()
