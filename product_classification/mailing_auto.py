from email.message import EmailMessage
from smtplib import SMTP_SSL
from pathlib import Path
from openpyxl import load_workbook


class EmailSender:
    MY_ID = ''
    MY_PW = ''# 앱비밀번호16자리

    # 받는사람, 제목, 본문, 첨부파일
    def send_mail(self, id, pw, recipient, title, text, attachment=False):
        # 템플릿 생성
        msg = EmailMessage()

        # 로그인 계정/pw
        MY_ID = id
        MY_PW = pw

        # 보내는 사람 / 받는 사람 / 제목 입력
        msg["From"] = MY_ID
        msg["To"] = recipient.split(",")
        msg["Subject"] = title

        # 본문 구성
        msg.set_content(text)

        # 파일 첨부
        if attachment:
            filenm = Path(attachment).name
            with open('./data/'+attachment, 'rb') as f:
                msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename=filenm)

        # 보내는 사람 로그인 및 smtp 서버로 발송
        with SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(MY_ID, MY_PW)
            smtp.send_message(msg)
        # 완료 메시지
        print("발송 성공")

    # 엑셀파일에서 가져온 정보를 활용해 함수 반복 실행
    wb = load_workbook('email_list.xlsx', data_only=True)
    ws = wb.active

    for row in ws.iter_rows():
        recipient = row[0].value
        print(recipient)
        title = row[1].value
        text = row[2].value
        attachment = row[3].value
        send_mail(recipient, title, text, attachment)

es = EmailSender('**', '**')

