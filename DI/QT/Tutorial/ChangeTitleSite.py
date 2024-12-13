import sys

from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Tittle
        self.setWindowTitle("My app")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_botton_was_clicked)

        self.setCentralWidget(self.button)


    def the_botton_was_clicked(self):
        self.button.setText("You alreade clicked me.")
        self.button.setEnabled(False)


        #Also change the window title
        self.setWindowTitle("My oneshot App")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
