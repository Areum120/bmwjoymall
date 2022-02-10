import sys
from PyQt5.QtWidgets import *
from gui.rpa_thread import UI


# initialize The App
if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        UIWindow = UI()
        UIWindow.show()
    except Exception as e:
            print(e)  # 에러를 표시하기 위해서
            input()  # 멈추게 하기 위해서
    app.exec_()

