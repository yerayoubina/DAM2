import sys
from ctypes.wintypes import HBRUSH

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QCheckBox, QApplication, QLabel, QComboBox, QVBoxLayout, QWidget, QListWidget, \
    QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        container = QWidget()
        mainLayout = QVBoxLayout()
        verticalBox = QVBoxLayout()
        horizontalBox =  QHBoxLayout()


    ## CHECK BOX

        self.setWindowTitle("Check Box")
        label = QLabel("Esto es un checkcbox de label")
        checkbox = QCheckBox(label.text())
        checkbox.stateChanged.connect(self.show_stateCHECKBOX)
        mainLayout.addWidget(checkbox)

    ## COMBO BOX
        combobox = QComboBox()
        combobox.addItems(["one","two","three"])
        combobox.setEditable(True)

        combobox.currentTextChanged.connect(self.textChangedCOMBOBOX)
        combobox.currentIndexChanged.connect(self.indexChangedCOMBOBOX)

       # verticalBox.addWidget(checkbox)
        mainLayout.addWidget(combobox)

    ## ListWidget

        listWidget = QListWidget()
        listWidget.addItems(["banana", "sandia", "melon"])


        horizontalBox.addWidget(listWidget)
        horizontalBox.addWidget(combobox)
        mainLayout.addLayout(verticalBox)
        mainLayout.addLayout(horizontalBox)
        container.setLayout(mainLayout)

        self.setCentralWidget(container)

    def show_stateCHECKBOX(self, s):
        print(s == Qt.CheckState.Checked.value)
        print(s)

    def textChangedCOMBOBOX(self,s):
        print(s)

    def indexChangedCOMBOBOX(self, s):
        print(s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
