import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QAbstractItemView, QMessageBox
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de Tareas")
        self.setGeometry(100, 100, 600, 400)

        # Layout principall vertical
        main_layout = QVBoxLayout()

        # Formulario de datos básicos
        self.form_layout = QHBoxLayout()
        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        self.edad_label = QLabel("Edad:")
        self.edad_input = QLineEdit()
        self.form_layout.addWidget(self.nombre_label)
        self.form_layout.addWidget(self.nombre_input)
        self.form_layout.addWidget(self.edad_label)
        self.form_layout.addWidget(self.edad_input)
        main_layout.addLayout(self.form_layout)

        # Tabla de tareas
        self.tareas_table = QTableWidget()
        self.tareas_table.setColumnCount(10)
        self.tareas_table.setHorizontalHeaderLabels(["Tareas","Cliente"])
        self.tareas_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        main_layout.addWidget(self.tareas_table)

        # Botones de acciones
        botones_layout = QHBoxLayout()
        self.agregar_button = QPushButton("Agregar Tarea")
        self.modificar_button = QPushButton("Modificar Tarea")
        self.eliminar_button = QPushButton("Eliminar Tarea")

        botones_layout.addWidget(self.agregar_button)
        botones_layout.addWidget(self.modificar_button)
        botones_layout.addWidget(self.eliminar_button)

        main_layout.addLayout(botones_layout)

        # Conexión de botones
        self.agregar_button.clicked.connect(self.agregar_tarea)
        self.modificar_button.clicked.connect(self.modificar_tarea)
        self.eliminar_button.clicked.connect(self.eliminar_tarea)

        # Contenedor principal
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def agregar_tarea(self):
        texto, ok = QLineEdit.getText(self, "Agregar Tarea", "Escribe la tarea:")
        if ok and texto:
            fila = self.tareas_table.rowCount()
            self.tareas_table.insertRow(fila)
            self.tareas_table.setItem(fila, 0, QTableWidgetItem(texto))

    def modificar_tarea(self):
        fila = self.tareas_table.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Error", "Selecciona una tarea para modificar")
            return

        texto_actual = self.tareas_table.item(fila, 0).text()
        texto, ok = QLineEdit.getText(self, "Modificar Tarea", "Edita la tarea:", QLineEdit.Normal, texto_actual)
        if ok and texto:
            self.tareas_table.setItem(fila, 0, QTableWidgetItem(texto))

    def eliminar_tarea(self):
        fila = self.tareas_table.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Error", "Selecciona una tarea para eliminar")
            return

        self.tareas_table.removeRow(fila)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
