import sys
from PyQt5.QtWidgets import *
from gui.rpa_thread import UI


# initialize The App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    UIWindow.show()
    app.exec_()

