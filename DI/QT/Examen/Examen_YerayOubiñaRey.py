
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QCheckBox, QComboBox, QSlider, QDial,
    QLabel, QGroupBox, QVBoxLayout,  QGridLayout, QWidget, QMessageBox, QListWidget
)



class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 17-12-2024")
        self.setGeometry(100, 100, 600, 400)

        self.nPista = 0

        # Widgets
        self.tedCadroTexto = QListWidget()

        self.btnAbrirFich = QPushButton("Abrir ficheiro")
        self.btnReproducir = QPushButton("Reproducir ficheiro")
        self.btnGardar = QPushButton("Gardar")
        self.btnEliminar = QPushButton("Eliminar")
        self.dilVolume = QDial()
        self.chkAnimado = QCheckBox("Animado")

        self.btnSaltar = QPushButton("Saltar")
        self.cmbSaltar = QComboBox()
        self.cmbSaltar.addItems(['0','1','2','3','4','5','6','7','8'])



        self.chkFiltrar = QCheckBox("Filtrar antes de reproducir")
        self.chkEXML = QCheckBox("É XML")
        self.chkRepNPL = QCheckBox("Reproducción NPL")

        self.lblVolume = QLabel("Volume:")
        self.lblFormato = QLabel("Formato:")
        self.lblSaidaAudio = QLabel("Saída de Audio")

        self.sldVolume = QSlider(Qt.Orientation.Horizontal)
        self.sldVolume.setMinimum(0)
        self.sldVolume.setMaximum(8)
        self.cmbFormato = QComboBox()
        self.cmbSaidaAudio = QComboBox()

        # Configurar acciones para botones
        self.btnAbrirFich.clicked.connect(self.subirPista)
        self.chkFiltrar.stateChanged.connect(self.add_option)
        self.chkEXML.stateChanged.connect(self.add_option)
        self.chkRepNPL.stateChanged.connect(self.add_option)
        self.btnGardar.clicked.connect(self.add_option)


        # Opciones GroupBox
        opcionsReproduccion = QGroupBox("Opcións de reproducción")
        layout_opcions = QVBoxLayout()
        layout_opcions.addWidget(self.chkFiltrar)
        layout_opcions.addWidget(self.chkEXML)
        layout_opcions.addWidget(self.chkRepNPL)
        opcionsReproduccion.setLayout(layout_opcions)

        #CONESXIONES
        self.dilVolume.valueChanged.connect(self.infoDial)
        self.cmbSaltar.currentIndexChanged.connect(self.saltar_cmb)


        # Layout principal
        mainLayout = QVBoxLayout()
        gridLayout = QGridLayout()
        mainLayout.addLayout(gridLayout)




        # ESTRUCTURA GRID
        gridLayout.addWidget(self.tedCadroTexto, 0,0,4,3)
        gridLayout.addWidget(self.dilVolume,0,3,1,2 )
        gridLayout.addWidget(self.chkAnimado, 1,3,1,1)
        gridLayout.addWidget(self.btnSaltar, 2,3,1,1)
        gridLayout.addWidget(self.cmbSaltar, 2,4,1,1)
        gridLayout.addWidget(self.btnAbrirFich, 4,0,1,1)
        gridLayout.addWidget(self.btnReproducir, 4,1,1,1)
        gridLayout.addWidget(self.btnGardar, 4,2,1,1)
        gridLayout.addWidget(self.btnEliminar, 4,3,1,2)
        gridLayout.addWidget(opcionsReproduccion, 5,0,3,2)
        gridLayout.addWidget(self.lblVolume, 5,2,1,1)
        gridLayout.addWidget(self.sldVolume, 5,3,1,2)
        gridLayout.addWidget(self.lblFormato, 6,2,1,1)
        gridLayout.addWidget(self.cmbFormato, 6,3,1,2)
        gridLayout.addWidget(self.lblSaidaAudio, 7,2,1,1)
        gridLayout.addWidget(self.cmbSaidaAudio, 7,3,1,2)






        # Establecer layout principal
        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

    # 2  Punto mostrar dial por consola

    def infoDial(self):
        value = self.dilVolume.value()
        print(f"VALOR DO DIAL: {value}")

    # 3 Punto combox modifica el QSlider
    def saltar_cmb(self):
        valorCombobox = self.cmbSaltar.currentIndex()
        print(valorCombobox)


    # 4 mostrar en lista las opciones con Gardar    ou eliminar
    def add_option(self):
        valor = ""
        lista = ['']
        if self.chkFiltrar.isChecked() and self.chkFiltrar.isChecked():
            lista.append(self.chkFiltrar.text())
            valor = self.chkRepNPL.text()
            self.tedCadroTexto.addItem(f" Opcións : {valor}")

        if self.chkEXML.isChecked() and self.chkEXML.isChecked():
            lista.append(self.chkEXML.text())
            valor = self.chkEXML.text()
            self.tedCadroTexto.addItem(f" Opcións : {valor}")

        if self.chkRepNPL.isChecked() and self.chkRepNPL.isChecked():
            lista.append(self.chkRepNPL.text())
            valor = self.chkRepNPL.text()
            self.tedCadroTexto.addItem(f" Opcións : {valor}")



        """self.addPista()
        texto = ""
        pista = self.nPista.__str__()
        for txt in lista:
            texto += txt + ' - '"""






    def addPista(self):
        self.nPista  += 1

    def susPista(self):
        if(self.nPista > 0):
            self.nPista -= 1


    #  5. SUBIR O BAJAR POR LAS PISTAS
    def subirPista(self):
        if self.tedCadroTexto.currentItem() is None:
           self.Info("No hay seleccionado ningua pista de la lista")

        if self.nPista > self.tedCadroTexto.currentRow():
            return

    def bajarPista(self):
       if self.tedCadroTexto.currentItem() is None:
           self.Info("No hay seleccionado ningua pista de la lista")

    def Info(self, str):
        msg = QMessageBox()
        msg.setText(str)
        msg.setWindowTitle("Advertencia")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.exec()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    aplicacion.exec()
