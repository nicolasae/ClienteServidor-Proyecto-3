from .ventana import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    
def show():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    show()