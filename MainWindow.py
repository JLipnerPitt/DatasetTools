from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


app = QApplication(sys.argv)
window = MainWindow()  # creates main window
window.show()  # shows main window
app.exec()  # launches application