# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collalab.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    # label, button
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 769)
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_file_upload = QtWidgets.QPushButton(Dialog)
        self.pushButton_file_upload.setObjectName("pushButton_file_upload")
        self.horizontalLayout_5.addWidget(self.pushButton_file_upload)
        self.pushButton_partners_orders = QtWidgets.QPushButton(Dialog)
        self.pushButton_partners_orders.setObjectName("pushButton_partners_orders")
        self.horizontalLayout_5.addWidget(self.pushButton_partners_orders)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_1_ex3_2 = QtWidgets.QLabel(Dialog)
        self.label_1_ex3_2.setObjectName("label_1_ex3_2")
        self.gridLayout_2.addWidget(self.label_1_ex3_2, 2, 0, 1, 1)
        self.label_1_ex3 = QtWidgets.QLabel(Dialog)
        self.label_1_ex3.setObjectName("label_1_ex3")
        self.gridLayout_2.addWidget(self.label_1_ex3, 1, 0, 1, 1)
        self.label_1_ex4 = QtWidgets.QLabel(Dialog)
        self.label_1_ex4.setObjectName("label_1_ex4")
        self.gridLayout_2.addWidget(self.label_1_ex4, 3, 0, 1, 1)
        self.label_1_ex2 = QtWidgets.QLabel(Dialog)
        self.label_1_ex2.setObjectName("label_1_ex2")
        self.gridLayout_2.addWidget(self.label_1_ex2, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_1_ex = QtWidgets.QLabel(Dialog)
        self.label_1_ex.setObjectName("label_1_ex")
        self.gridLayout.addWidget(self.label_1_ex, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_2_title = QtWidgets.QLabel(Dialog)
        self.label_2_title.setObjectName("label_2_title")
        self.verticalLayout.addWidget(self.label_2_title)
        self.textEdit_title = QtWidgets.QTextEdit(Dialog)
        self.textEdit_title.setObjectName("textEdit_title")
        self.verticalLayout.addWidget(self.textEdit_title)
        self.gridLayout_4.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2_text = QtWidgets.QLabel(Dialog)
        self.label_2_text.setObjectName("label_2_text")
        self.verticalLayout_2.addWidget(self.label_2_text)
        self.textEdit_text = QtWidgets.QTextEdit(Dialog)
        self.textEdit_text.setObjectName("textEdit_text")
        self.verticalLayout_2.addWidget(self.textEdit_text)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.pushButton_create_email_list = QtWidgets.QPushButton(Dialog)
        self.pushButton_create_email_list.setObjectName("pushButton_create_email_list")
        self.verticalLayout_2.addWidget(self.pushButton_create_email_list)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.label_2_ex1 = QtWidgets.QLabel(Dialog)
        self.label_2_ex1.setObjectName("label_2_ex1")
        self.verticalLayout_4.addWidget(self.label_2_ex1)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 3, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 4, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_3_id = QtWidgets.QLabel(Dialog)
        self.label_3_id.setObjectName("label_3_id")
        self.verticalLayout_5.addWidget(self.label_3_id)
        self.textEdit_id = QtWidgets.QTextEdit(Dialog)
        self.textEdit_id.setObjectName("textEdit_id")
        self.verticalLayout_5.addWidget(self.textEdit_id)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 5, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3_pw = QtWidgets.QLabel(Dialog)
        self.label_3_pw.setObjectName("label_3_pw")
        self.verticalLayout_6.addWidget(self.label_3_pw)
        self.textEdit_pw = QtWidgets.QTextEdit(Dialog)
        self.textEdit_pw.setObjectName("textEdit_pw")
        self.verticalLayout_6.addWidget(self.textEdit_pw)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.pushButton_send_email = QtWidgets.QPushButton(Dialog)
        self.pushButton_send_email.setObjectName("pushButton_send_email")
        self.verticalLayout_6.addWidget(self.pushButton_send_email)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.label_3_ex1 = QtWidgets.QLabel(Dialog)
        self.label_3_ex1.setObjectName("label_3_ex1")
        self.verticalLayout_6.addWidget(self.label_3_ex1)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 6, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButton_file_upload, self.pushButton_partners_orders)
        Dialog.setTabOrder(self.pushButton_partners_orders, self.textEdit_title)
        Dialog.setTabOrder(self.textEdit_title, self.textEdit_text)
        Dialog.setTabOrder(self.textEdit_text, self.pushButton_create_email_list)
        Dialog.setTabOrder(self.pushButton_create_email_list, self.textEdit_id)
        Dialog.setTabOrder(self.textEdit_id, self.textEdit_pw)
        Dialog.setTabOrder(self.textEdit_pw, self.pushButton_send_email)

    # text
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_file_upload.setText(_translate("Dialog", "File upload(xls)"))
        self.pushButton_partners_orders.setText(_translate("Dialog", "파트너사 주문파일 생성"))
        self.label_1_ex3_2.setText(_translate("Dialog", "* 브랜드명/업체명 변경은 listOfPartners_name.xlsx 파일을 수정해주세요."))
        self.label_1_ex3.setText(_translate("Dialog", "* 업로드한 xls 파일은 자동으로 xlsx 형식의 파일을 새로 생성합니다. "))
        self.label_1_ex4.setText(_translate("Dialog", "* 파트너사 별 주문파일은 data 폴더에서 확인 가능합니다."))
        self.label_1_ex2.setText(_translate("Dialog", "* 주문파일 이름은 \'sendRequest\'로 변경해주세요."))
        self.label_1.setText(_translate("Dialog", "1. 주문파일(xls)을 업로드 후, 파트너사 주문파일 생성 버튼을 눌러주세요."))
        self.label_1_ex.setText(_translate("Dialog", "예시) \'sendRequest.xls\'"))
        self.label_2.setText(_translate("Dialog", "2. 이메일 제목, 본문 입력 후 발송할 이메일리스트 파일을 생성해주세요."))
        self.label_2_title.setText(_translate("Dialog", "제목:"))
        self.textEdit_title.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[웍스컴바인] BMW JOY MALL \' + f\'{nowToday} 상품발주 확인요청의 件</p></body></html>"))
        self.label_2_text.setText(_translate("Dialog", "본문:"))
        self.textEdit_text.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">안녕하세요.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">웍스컴바인 김기정입니다.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">금일자로 주문건 접수되어 출고요청 전달드립니다.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">확인부탁드리겠습니다.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">항상 많은 도움주셔서 감사드립니다.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">김기정 드림</p></body></html>"))
        self.pushButton_create_email_list.setText(_translate("Dialog", "이메일리스트 생성"))
        self.label_2_ex1.setText(_translate("Dialog", "* 파트너사 정보 변경은 listOfPartners.xlsx 파일을 수정해주세요"))
        self.label_3.setText(_translate("Dialog", "3.구글 이메일 계정, 앱비밀번호 16자리 입력 후, 메일 발송 버튼을 눌러주세요."))
        self.label_3_id.setText(_translate("Dialog", "e-mail:"))
        self.textEdit_id.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">tjfsu120@gmail.com</p></body></html>"))
        self.label_3_pw.setText(_translate("Dialog", "PW:"))
        self.textEdit_pw.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">************</p></body></html>"))
        self.pushButton_send_email.setText(_translate("Dialog", "메일 발송"))
        self.label_3_ex1.setText(_translate("Dialog", "* 꼭 이메일리스트 내용 확인 후 발송버튼을 눌러주세요. "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

