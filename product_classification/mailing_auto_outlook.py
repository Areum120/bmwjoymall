import win32com.client
import openpyxl as op
import os

# 아웃룩 메일 보내기

class send_outlook_email:
    def __init__(self, df):
        self.df = df

    def load_excel(self):
        # 엑셀 읽기
        wb = op.load_workbook(self.df)#workbook객체 생성
        ws = wb.active#활성화 시트 객체 생성
        mail_list=[]
        for row in ws.iter_rows():
            temp = (row[0].value, row[1].value, row[2].value, row[3].value, row[4].value)
            mail_list.append(temp)
            # print(temp)
        self.mail_list = mail_list
        return self.mail_list
        # excel = win32com.client.Dispatch("Excel.Application")
        # wb = excel.Workbooks.Open(self.df) #workbook객체 생성
        # ws = wb.active
        # self.sheet = ws.Sheets('Sheet1') # worksheet객체 생성

    # def send_email(mail_list : list):
    #     print(mail_list)
    #     print(list)
    def send_email(self):
        outlook = win32com.client.Dispatch("Outlook.Application")#아웃룩지정

        # 엑셀 데이터 읽어오기
        for send_one in self.mail_list: #mail_list에 대한 리스트 반복
            new_email = outlook.CreateItem(0) #메일 보내기 창 객체 생성
            recipient = send_one[0]# 메일 수신자
            recipient2 = send_one[1]# 참조
            title = send_one[2]# 제목
            text = send_one[3]# 내용
            atch_files = send_one[4] #첨부파일

            new_email.To = recipient# 메일 수신자
            if recipient2 is not None:
                new_email.CC = recipient2.split('/') # 참조
            new_email.Subject = title  # 제목
            new_email.HTMLBody = text # 내용
            new_email.Attachments.Add(os.getcwd() + '\\data\\' + atch_files)#첨부파일 추가

            new_email.Send()
            print('발송 완료')

    '''
    data 출력
        print(ws.cells(1,1).Value)
        print(ws.cells(2,1).Value)
        print(ws.cells(3,1).Value)
    '''

    # if __name__ =="__main__":
    # #     atch = os.getcwd() + '\\data\\' + '[웍스컴바인]발주요청서_2022-03-02_AUTOCOS.xlsx'
    #     mail_list = load_excel(os.getcwd() + '\\' +'email_list.xlsx')
    #     send_email(mail_list)

# SOE = send_outlook_email(os.getcwd() + '\\' +'email_list.xlsx')
# SOE.load_excel()
# SOE.send_email()