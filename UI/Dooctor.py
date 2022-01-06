from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import Dooctor_UI

class Dooctor(QtWidgets.QMainWindow, Dooctor_UI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Dooctor, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = Dooctor()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
