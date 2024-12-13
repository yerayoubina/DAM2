import sys

from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication

from Tutorial.FirstWindow import FirstWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def the_button_was_toggled(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)

app = QApplication(sys.argv)
window = FirstWindow()
window.show()
app.exec()