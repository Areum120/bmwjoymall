import os
import sys
import datetime
import pythoncom
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

#패키지 함수 불러오기
from product_classification import convert_to_xlsx
from product_classification import excel_classification
from product_classification import create_email_list
from product_classification import mailing_auto

# load the ui file
form_class = uic.loadUiType('..\\gui\\collalab_rpa.ui')[0]

# 버튼1 쓰레드 클래스
class Thread1(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        print('thread1 시작')
        # 메인 스레드에서는 정상적으로 동작하는 코드가 서브 스레드에서는 오류가 발생
        # pythoncom 모듈의 CoInitialize() 함수를 run() 메서드 안에서 호출
        pythoncom.CoInitialize()
        path = os.getcwd()+'\\'+'sendRequest.xls'#현재 폴더 경로 생성
        print(path)
        convert_to_xlsx.converToxlsx(path)
        # 사용 후 uninitialize
        pythoncom.CoUninitialize()
        self.sleep(1)
        print('thread1 완료')

# 버튼2 쓰레드 클래스
class Thread2(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        print('thread2 시작')
        CE = excel_classification.ClassificationExcel('sendRequest.xlsx', 'listOfPartners_name.xlsx')
        CE.make_product_dict()
        CE.find_product()
        self.sleep(1)
        print('thread2 완료')

#  버튼3 쓰레드 클래스
class Thread3(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        print('thread3 시작')
        now = datetime.datetime.now()  # 지금시간
        nowToday = now.strftime('%m/%d')  # 오늘일자생성
        print(nowToday)

        title = self.parent.line_text.text()
        print(title[0:21])#[웍스컴바인] BMW JOY MALL
        print(title[20:33])#상품발주 확인요청의 件
        cntxt = self.parent.text_text.toPlainText()
        # print(cntxt)

        CC = create_email_list.CreateEmailList('.\\listOfPartners.xlsx', title[0:21] + f'{nowToday}'+ title[20:33], cntxt)
        #메소드 호출
        CC.make_filenm_list()
        CC.make_email_list()
        self.sleep(1)
        print('thread3 완료')

#  버튼4 쓰레드 클래스
class Thread4(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        print('thread4 시작')
        id = self.parent.line_text_2.text()
        pw = self.parent.line_text_3.text()
        es = mailing_auto.SendEmail(id, pw, 'email_list.xlsx')
        es.send_email()#Username and Password not accepted 에러 앱비밀번호 재수정
        self.sleep(1)
        print('thread4 완료')

class UI(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 타이틀
        self.setWindowTitle('BMW Joymall 업무 프로세스 자동화 app')

        self.line_text = self.findChild(QLineEdit, 'lineEdit')#title
        self.text_text = self.findChild(QTextEdit, 'textEdit_text')#본문

        self.line_text_2 = self.findChild(QLineEdit, 'lineEdit_2')#이메일
        self.line_text_3 = self.findChild(QLineEdit, 'lineEdit_3')#pw

        # print(self.line_text.text())
        # print(self.text_text.toPlainText())
#       thread3에 글자 내용을 어떻게 전달? parent인자로 전달

# click the pushButton
        self.pushButton.clicked.connect(self.click_button_1) #xlsx형식변환
        self.pushButton_2.clicked.connect(self.click_button_2) #업체별 주문파일 생성
        self.pushButton_create_email_list.clicked.connect(self.click_button_3) #이메일리스트 생성
        self.pushButton_send_email.clicked.connect(self.click_button_4)#메일 자동 발송

    def click_button_1(self):
        x1 = Thread1(self)
        x1.start()#thread1 run 동작

    def click_button_2(self):
        x2 = Thread2(self)
        x2.start()  # thread2 run 동작

    def click_button_3(self):
        x3 = Thread3(self)
        x3.start()  # thread3 run 동작

    def click_button_4(self):
        x4 = Thread4(self)
        x4.start()  # thread4 run 동작

    # exception 발생시 종료 방지(스레드 켜지기 전에 main이 끝나서 프로그램 종료됨)
    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        # sys.exit(1)
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook
    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook

# initialize The App
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     UIWindow = UI()
#     UIWindow.show()
#     app.exec_()
