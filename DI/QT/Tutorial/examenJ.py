
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QHBoxLayout, QGridLayout, QWidget, QVBoxLayout)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 10-12_2024")
        self.setFixedSize(450, 450)

        # declaraciones
        self.lblNome = QLabel("Nome")
        self.lblApelido = QLabel("Apelido")
        self.lblTratamento = QLabel("Tratamento")
        self.lblUsuario = QLabel("Usuario")
        self.txtNome = QLineEdit()
        self.txtApelido = QLineEdit()
        self.txtTratamento = QLineEdit()
        self.txtUsuario = QLineEdit()
        self.lblFormato = QLabel("Formato")
        self.cmbFormato = QComboBox()

        self.lblDireccionC = QLabel("Dirección de correo")
        self.txtDireccionC = QLineEdit()

        self.lstDireccionC = QListWidget()

        self.btnEngadir = QPushButton("Engadir")
        self.btnEditar = QPushButton("Editar")
        self.btnBorrar = QPushButton("Borrar")
        self.btnPorDefecto = QPushButton("Por Defecto")
        self.lblFormatoCorreo = QLabel("Formato de correo: ")

        self.rbtHtml = QRadioButton("HTML")
        self.rbtTextoPlano = QRadioButton("Texto Plano")
        self.rbtPersonalizado = QRadioButton("Personalizado")

        self.btnAceptar = QPushButton("Aceptar")
        self.btnCancelar = QPushButton("Cancelar")

        # elementos combo
        self.cmbFormato.addItem("HTML")
        self.cmbFormato.addItem("Texto plano")
        self.cmbFormato.addItem("Personalizado")

        # layouts
        self.layout_principal = QVBoxLayout()
        self.layout_grid = QGridLayout()
        self.list_botones = QHBoxLayout()
        self.aux_botones = QVBoxLayout()
        self.correo_cancelar = QGridLayout()

        # ponemos el layout grid
        self.layout_grid.addWidget(self.lblNome, 0, 0, 1, 1)
        self.layout_grid.addWidget(self.txtNome, 0, 1, 1, 1)
        self.layout_grid.addWidget(self.lblApelido, 1, 0, 1, 1)
        self.layout_grid.addWidget(self.txtApelido, 1, 1, 1, 1)

        self.layout_grid.addWidget(self.lblTratamento, 2, 0, 1, 1)
        self.layout_grid.addWidget(self.txtTratamento, 3, 0, 1, 1)

        self.layout_grid.addWidget(self.lblUsuario, 2, 1, 1, 1)
        self.layout_grid.addWidget(self.txtUsuario, 3, 1, 1, 1)

        self.layout_grid.addWidget(self.lblFormato, 4, 0, 1, 1)
        self.layout_grid.addWidget(self.cmbFormato, 4, 1, 1, 1)

        # lista y botones
        self.list_widget = QListWidget()
        self.list_botones.addWidget(self.list_widget)

        self.aux_botones.addWidget(self.btnEngadir)
        self.aux_botones.addWidget(self.btnEditar)
        self.aux_botones.addWidget(self.btnBorrar)
        self.aux_botones.addWidget(self.btnPorDefecto)
        self.aux_botones.addWidget(self.lblFormatoCorreo)
        self.aux_botones.addWidget(self.lblFormato)
        self.aux_botones.addWidget(self.rbtHtml)
        self.aux_botones.addWidget(self.rbtTextoPlano)
        self.aux_botones.addWidget(self.rbtPersonalizado)

        self.list_botones.addLayout(self.aux_botones)

        # correo y cancelar
        self.correo_cancelar.addWidget(self.lblDireccionC, 0, 0, 1, 1)
        self.correo_cancelar.addWidget(self.txtDireccionC, 1, 0, 1, 3)

        self.correo_cancelar.addWidget(self.btnCancelar, 2, 1, 1, 1)
        self.correo_cancelar.addWidget(self.btnAceptar, 2, 2, 1, 1)

        # conexiones
        self.btnEngadir.clicked.connect(self.anade_elemento)
        self.cmbFormato.currentIndexChanged.connect(self.mostrar_mensaje_combo)
        self.rbtHtml.clicked.connect(self.sincronizar_radio_buttons)
        self.rbtTextoPlano.clicked.connect(self.sincronizar_radio_buttons)
        self.rbtPersonalizado.clicked.connect(self.sincronizar_radio_buttons)
        self.btnBorrar.clicked.connect(self.boton_eliminar_elemento)

        self.layout_principal.addLayout(self.layout_grid)
        self.layout_principal.addLayout(self.list_botones)
        self.layout_principal.addLayout(self.correo_cancelar)

        container = QWidget()
        container.setLayout(self.layout_principal)

        self.setCentralWidget(container)
        self.show()

    def mostrar_mensaje_combo(self):
        if self.cmbFormato.currentIndex() == 0:
            print("El usuario ha pulsado la opcion de html")
        elif self.cmbFormato.currentIndex() == 1:
            print("El usuario ha pulsado la opcion de Texto plano")
        elif self.cmbFormato.currentIndex() == 2:
            print("EL usuario ha pulsado la opcion de personalizado")

    def sincronizar_radio_buttons(self):
        if self.rbtHtml.isChecked():
            self.cmbFormato.setCurrentIndex(0)
        elif self.rbtTextoPlano.isChecked():
            self.cmbFormato.setCurrentIndex(1)
        elif self.rbtPersonalizado.isChecked():
            self.cmbFormato.setCurrentIndex(2)

    def anade_elemento(self):
        if self.txtTratamento.text() != "" or self.txtUsuario.text() != "" or self.txtApelido.text() != "" or self.txtDireccionC.text() != "":
            nome = self.txtNome.text()
            apelido = self.txtApelido.text()
            direccion = self.txtDireccionC.text()
            tratamento = self.txtTratamento.text()

            self.list_widget.addItem(nome + " , " + apelido + " ,  " + direccion + " , " + tratamento)
            self.limpiar_campos()

    def boton_eliminar_elemento(self):
        elementos = self.list_widget.selectedItems()
        if elementos:
            for i in elementos:
                self.list_widget.takeItem(self.list_widget.row(i))
            self.list_widget.clearSelection()

    def limpiar_campos(self):
        self.txtNome.clear()
        self.txtApelido.clear()
        self.txtDireccionC.clear()
        self.txtTratamento.clear()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()

    aplicacion.exec()

