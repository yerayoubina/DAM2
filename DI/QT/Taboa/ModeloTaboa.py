from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtGui import QColor, QIcon


class ModeloTaboa(QAbstractTableModel):
    def __init__(self, taboa):
        super().__init__()
        self.taboa = taboa

    def rowCount(self, indice):
        return len(self.taboa)

    def columnCount(self, indice):
        return len(self.taboa[0])

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.EditRole or rol == Qt.ItemDataRole.DisplayRole:
            valor = self.taboa[indice.row()][indice.column()]
            return valor

        if rol == Qt.ItemDataRole.BackgroundRole:
            color = QColor('')  # Valor predeterminado (fondo blanco)

            # Si es "Home", fondo amarillo
            if self.taboa[indice.row()][2] == "Home":
                color = QColor('yellow')
            # Si es "Muller", fondo rosa
            elif self.taboa[indice.row()][2] == "Muller":
                color = QColor('pink')
            return color

        if rol == Qt.ItemDataRole.DecorationRole:
            if isinstance(self.taboa[indice.row()][indice.column()], bool):
                if self.taboa[indice.row()][indice.column()]:
                    return QIcon('resources/tick.png')
        return None
