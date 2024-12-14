import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QGridLayout, QPushButton, QVBoxLayout, QWidget, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Título
        self.setWindowTitle("Calculadora")
        self.setGeometry(50, 50, 300, 300)

        # Elementos
        container = QWidget()
        boxV = QVBoxLayout()
        self.grid = QGridLayout()
        self.labelText = QLabel("0")
        self.labelText.setStyleSheet("font-size: 24px; padding: 10px;")
        self.current_expression = ""

        # Estructurar grid
        self.create_buttons()

        boxV.addWidget(self.labelText)
        boxV.addLayout(self.grid)
        container.setLayout(boxV)
        self.setCentralWidget(container)

    def create_buttons(self):
        buttons = [
            ('0', 4, 0),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('+', 1, 3), ('-', 2, 3),
            ('x', 3, 3), ('/', 4, 3),
            ('C', 0, 0), ('=', 4, 2)
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(60, 60)
            button.setStyleSheet("font-size: 18px;")
            button.clicked.connect(self.on_button_click)
            self.grid.addWidget(button, row, col)

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()
        print(f"El boton presionado ha sido {text}")

        if text == "C":
            self.current_expression = ""
        elif text == "=":
            try:
                expression = self.current_expression.replace("x", "*")
                self.current_expression = str(eval(expression))
            except Exception:
                self.current_expression = "Error"
        else:
            self.current_expression += text

        self.labelText.setText(self.current_expression)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
