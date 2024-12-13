import sys
from PyQt6.QtCore import QStringListModel, Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, 
    QPushButton, QHBoxLayout, QListView, QMessageBox
)

### MODELO ###
class TareasModelo(QStringListModel):
    """Modelo que maneja una lista de tareas."""
    def __init__(self, tareas=None):
        super().__init__(tareas or [])

    def agregar_tarea(self, tarea):
        """Agrega una nueva tarea al modelo."""
        lista_actual = self.stringList()
        lista_actual.append(tarea)
        self.setStringList(lista_actual)

    def actualizar_tarea(self, index, nueva_tarea):
        """Actualiza una tarea existente en el modelo."""
        lista_actual = self.stringList()
        if 0 <= index < len(lista_actual):
            lista_actual[index] = nueva_tarea
            self.setStringList(lista_actual)

    def eliminar_tarea(self, index):
        """Elimina una tarea del modelo."""
        lista_actual = self.stringList()
        if 0 <= index < len(lista_actual):
            lista_actual.pop(index)
            self.setStringList(lista_actual)


### VISTA ###
class TareasVista(QWidget):
    """Vista que muestra la lista de tareas y botones de control."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación CRUD con MVC en PyQt6")
        self.setGeometry(200, 200, 400, 300)

        # Layout principal
        self.layout = QVBoxLayout()

        # Vista de lista
        self.lista_view = QListView()
        self.layout.addWidget(self.lista_view)

        # Entrada de texto para nuevas tareas
        self.input = QLineEdit()
        self.input.setPlaceholderText("Escribe una nueva tarea")
        self.layout.addWidget(self.input)

        # Botones para CRUD
        self.button_layout = QHBoxLayout()

        self.add_button = QPushButton("Crear")
        self.update_button = QPushButton("Actualizar")
        self.delete_button = QPushButton("Eliminar")

        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.update_button)
        self.button_layout.addWidget(self.delete_button)

        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)


### CONTROLADOR ###
class TareasControlador:
    """Controlador que coordina el modelo y la vista."""
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        # Configurar la vista para usar el modelo
        self.vista.lista_view.setModel(self.modelo)

        # Conectar botones a las funciones
        self.vista.add_button.clicked.connect(self.agregar_tarea)
        self.vista.update_button.clicked.connect(self.actualizar_tarea)
        self.vista.delete_button.clicked.connect(self.eliminar_tarea)

    def agregar_tarea(self):
        tarea = self.vista.input.text().strip()
        if tarea:
            self.modelo.agregar_tarea(tarea)
            self.vista.input.clear()
        else:
            QMessageBox.warning(self.vista, "Advertencia", "El campo de texto está vacío.")

    def actualizar_tarea(self):
        indices = self.vista.lista_view.selectedIndexes()
        if indices:
            nueva_tarea = self.vista.input.text().strip()
            if nueva_tarea:
                index = indices[0].row()
                self.modelo.actualizar_tarea(index, nueva_tarea)
                self.vista.input.clear()
            else:
                QMessageBox.warning(self.vista, "Advertencia", "El campo de texto está vacío.")
        else:
            QMessageBox.warning(self.vista, "Advertencia", "Selecciona una tarea para actualizar.")

    def eliminar_tarea(self):
        indices = self.vista.lista_view.selectedIndexes()
        if indices:
            index = indices[0].row()
            self.modelo.eliminar_tarea(index)
        else:
            QMessageBox.warning(self.vista, "Advertencia", "Selecciona una tarea para eliminar.")


### FUNCIÓN PRINCIPAL ###
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Crear el modelo, la vista y el controlador
    modelo = TareasModelo()
    vista = TareasVista()
    controlador = TareasControlador(modelo, vista)

    vista.show()
    sys.exit(app.exec())