import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import datetime

#패키지 함수 불러오기
from product_classification import convert_to_xlsx
from product_classification import excel_classification
from product_classification import create_email_list
from product_classification import mailing_auto

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

#         load the ui file
        uic.loadUi('collalab_rpa.ui', self)

        # 타이틀
        self.setWindowTitle('BMW Joymall 업무 프로세스 자동화 program')

#         define our widgets
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button_2 = self.findChild(QPushButton, 'pushButton_2')
        self.button_3 = self.findChild(QPushButton, 'pushButton_create_email_list')
        self.button_4 = self.findChild(QPushButton, 'pushButton_send_email')

        self.line_text = self.findChild(QLineEdit, 'lineEdit')
        self.line_text_2 = self.findChild(QTextEdit, 'textEdit_text')

        #self.label = self.findChild(QLabel, 'label_5')

#         click the pushButton
        self.button.clicked.connect(self.click_button_1)#xlsx형식변환
        self.button_2.clicked.connect(self.click_button_2)#업체별 주문파일 생성
        self.button_3.clicked.connect(self.click_button_3)#이메일리스트 생성
        self.button_4.clicked.connect(self.click_button_4)#메일 발송

        # show The App
        self.show()

    def click_button_1(self):
        # fname = QFileDialog.getOpenFileName(self)
        # print(fname[0])
        # file_path = '{}'.format(fname[0]) # 경로 문자열 지정
        # self.label.setText(file_path)#문제없이 실행됨
        convert_to_xlsx.converToxlsx('.\\sendRequest.xls')
        #QFileDialog의 fname[0]이 convert_to_xlsx.converToxlsx 함수 안 path경로에 안먹힘

    def click_button_2(self):
        CE = excel_classification.ClassificationExcel('sendRequest.xlsx', 'listOfPartners_name.xlsx')
        CE.make_product_dict()
        CE.find_product()

    def click_button_3(self):
        now = datetime.datetime.now()  # 지금시간
        nowToday = now.strftime('%m/%d')  # 일자

        text1 = self.line_text.text()# line_edit text 값 가져오기
        text2 = self.line_text_2.text()
        print(text1)
        print(text2)

        CE = create_email_list.CreateEmailList('.\\listOfPartners.xlsx', text1, text2)
        CE.make_filenm_list()
        CE.make_email_list()

    def click_button_4(self):
        ES = mailing_auto.SendEmail('**', '**', 'email_list.xlsx')
        ES.send_email()

# initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
