import os
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QPushButton, QCheckBox, QComboBox, QSlider, QDial,
    QLabel, QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QMessageBox, QFileDialog
)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 17-12-2024")
        self.setGeometry(100, 100, 800, 600)

        # Crear widgets
        self.tedCadroTexto = QTextEdit()

        self.btnAbrirFich = QPushButton("Abrir ficheiro")
        self.btnReproducir = QPushButton("Reproducir ficheiro")
        self.btnGardar = QPushButton("Gardar")
        self.btnEliminar = QPushButton("Eliminar")
        self.dilVolume = QDial()
        self.chkAnimado = QCheckBox("Animado")

        self.btnSaltar = QPushButton("Saltar")
        self.cmbSaltar = QComboBox()

        self.chkFiltrar = QCheckBox("Filtrar antes de reproducir")
        self.chkEXML = QCheckBox("É XML")
        self.chkRepNPL = QCheckBox("Reproducción NPL")

        self.lblVolume = QLabel("Volume:")
        self.lblFormato = QLabel("Formato:")
        self.lblSaidaAudio = QLabel("Saída de Audio")

        self.sldVolume = QSlider(Qt.Orientation.Horizontal)
        self.cmbFormato = QComboBox()
        self.cmbSaidaAudio = QComboBox()

        # Configurar acciones para botones
        self.btnAbrirFich.clicked.connect(self.abrir_ficheiro)
        self.btnReproducir.clicked.connect(self.reproducir_ficheiro)
        self.btnGardar.clicked.connect(self.gardar_ficheiro)
        self.btnEliminar.clicked.connect(self.eliminar_ficheiro)
        self.btnSaltar.clicked.connect(self.saltar_a_opcion)

        # Opciones de reproducción en un GroupBox
        opcionsReproduccion = QGroupBox("Opcións de reproducción")
        layout_opcions = QVBoxLayout()
        layout_opcions.addWidget(self.chkFiltrar)
        layout_opcions.addWidget(self.chkEXML)
        layout_opcions.addWidget(self.chkRepNPL)
        opcionsReproduccion.setLayout(layout_opcions)

        # Layout principal
        layout_principal = QVBoxLayout()

        # Primera fila: Botones principales
        layout_fila1 = QHBoxLayout()
        layout_fila1.addWidget(self.btnAbrirFich)
        layout_fila1.addWidget(self.btnReproducir)
        layout_fila1.addWidget(self.btnGardar)
        layout_fila1.addWidget(self.btnEliminar)
        layout_principal.addLayout(layout_fila1)

        # Segunda fila: Dial y check animado
        layout_fila2 = QHBoxLayout()
        layout_fila2.addWidget(self.dilVolume)
        layout_fila2.addWidget(self.chkAnimado)
        layout_principal.addLayout(layout_fila2)

        # Tercera fila: Opciones de reproducción y texto
        layout_fila3 = QHBoxLayout()
        layout_fila3.addWidget(opcionsReproduccion)
        layout_fila3.addWidget(self.tedCadroTexto)
        layout_principal.addLayout(layout_fila3)

        # Cuarta fila: Saltar
        layout_fila4 = QHBoxLayout()
        layout_fila4.addWidget(self.btnSaltar)
        layout_fila4.addWidget(self.cmbSaltar)
        layout_principal.addLayout(layout_fila4)

        # Quinta fila: Controles adicionales
        layout_fila5 = QGridLayout()
        layout_fila5.addWidget(self.lblVolume, 0, 0)
        layout_fila5.addWidget(self.sldVolume, 0, 1)
        layout_fila5.addWidget(self.lblFormato, 1, 0)
        layout_fila5.addWidget(self.cmbFormato, 1, 1)
        layout_fila5.addWidget(self.lblSaidaAudio, 2, 0)
        layout_fila5.addWidget(self.cmbSaidaAudio, 2, 1)
        layout_principal.addLayout(layout_fila5)

        # Establecer layout principal
        contenedor_central = QWidget()
        contenedor_central.setLayout(layout_principal)
        self.setCentralWidget(contenedor_central)

    # Funciones de los botones
    def abrir_ficheiro(self):
        QMessageBox.information(self, "Abrir Ficheiro", "Función de abrir ficheiro executada.")
        # Abrir un cuadro de diálogo para seleccionar un fichero
        ruta_fichero, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir Ficheiro",  # Título del diálogo
            "",  # Directorio inicial (vacío = directorio por defecto)
            "Todos os arquivos (*);;Arquivos de texto (*.txt)"  # Filtros de tipo de fichero
        )

        if ruta_fichero:  # Si el usuario seleccionó un fichero
            try:
                # Leer el contenido del fichero
                with open(ruta_fichero, 'r', encoding='utf-8') as fichero:
                    contenido = fichero.read()
                    # Mostrar el contenido en el QTextEdit
                    self.tedCadroTexto.setPlainText(contenido)
                QMessageBox.information(self, "Ficheiro Aberto", f"Ficheiro cargado: {ruta_fichero}")
            except Exception as e:
                # Manejar errores al abrir el fichero
                QMessageBox.critical(self, "Erro ao Abrir", f"Non se pode abrir o ficheiro:\n{str(e)}")

    def reproducir_ficheiro(self):
        QMessageBox.information(self, "Reproducir Ficheiro", "Reproducción iniciada.")

    def gardar_ficheiro(self):
        QMessageBox.information(self, "Gardar Ficheiro", "Ficheiro gardado correctamente.")

        def gardar_ficheiro(self):
            # Abrir un cuadro de diálogo para guardar un fichero
            ruta_fichero, _ = QFileDialog.getSaveFileName(
                self,
                "Gardar Ficheiro",  # Título del diálogo
                "",  # Directorio inicial (vacío = directorio por defecto)
                "Arquivos de texto (*.txt);;Todos os arquivos (*)"  # Filtros de tipo de fichero
            )

            if ruta_fichero:  # Si el usuario seleccionó una ubicación y nombre
                try:
                    # Obtener el contenido del QTextEdit
                    contenido = self.tedCadroTexto.toPlainText()
                    # Escribir el contenido en el fichero
                    with open(ruta_fichero, 'w', encoding='utf-8') as fichero:
                        fichero.write(contenido)
                    QMessageBox.information(self, "Ficheiro Gardado", f"Ficheiro gardado correctamente: {ruta_fichero}")
                except Exception as e:
                    # Manejar errores al guardar el fichero
                    QMessageBox.critical(self, "Erro ao Gardar", f"Non se pode gardar o ficheiro:\n{str(e)}")

    def eliminar_ficheiro(self):
        self.tedCadroTexto.clear()  # Vaciar el QTextEdit como ejemplo
        QMessageBox.information(self, "Eliminar Ficheiro", "Ficheiro eliminado.")

        def eliminar_ficheiro(self):
            # Abrir un cuadro de diálogo para seleccionar un fichero a eliminar
            ruta_fichero, _ = QFileDialog.getOpenFileName(
                self,
                "Seleccionar Ficheiro para Eliminar",  # Título del diálogo
                "",  # Directorio inicial
                "Todos os arquivos (*)"  # Filtros
            )

            if ruta_fichero:  # Si se seleccionó un fichero
                # Confirmación antes de eliminar
                respuesta = QMessageBox.question(
                    self,
                    "Confirmar Eliminación",
                    f"Estás seguro de que queres eliminar o ficheiro?\n{ruta_fichero}",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )

                if respuesta == QMessageBox.StandardButton.Yes:
                    try:
                        # Eliminar el fichero
                        os.remove(ruta_fichero)
                        QMessageBox.information(self, "Ficheiro Eliminado",
                                                f"Ficheiro eliminado correctamente:\n{ruta_fichero}")
                    except Exception as e:
                        # Manejar errores durante la eliminación
                        QMessageBox.critical(self, "Erro ao Eliminar", f"Non se pode eliminar o ficheiro:\n{str(e)}")

    def saltar_a_opcion(self):
        opcion = self.cmbSaltar.currentText()
        QMessageBox.information(self, "Saltar a Opción", f"Saltando a: {opcion}")


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    aplicacion.exec()
