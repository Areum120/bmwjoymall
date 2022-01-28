from convert_to_xlsx import converToxlsx
from excel_classification import ClassificationExcel
from create_email_list import CreateEmailList
from mailing_auto import SendEmail
import datetime

# xlsx변환
converToxlsx('C:\\Users\\웍스컴바인\\Desktop\\work\\BMWJoymall\\product_classification\\sendRequest.xls')


# 업체별 엑셀파일 생성
#인스턴스 생성
CE = ClassificationExcel('sendRequest.xlsx', 'listOfPartners_name.xlsx')
#메소드 호출
CE.make_product_dict()
CE.find_product()


# 이메일리스트 생성

now = datetime.datetime.now()  # 지금시간
nowToday = now.strftime('%m/%d')  # 일자

#인스턴스 생성
ce = CreateEmailList('.\\listOfPartners.xlsx', '[웍스컴바인] BMW JOY MALL ' + f'{nowToday} 상품발주 확인요청의 件', '''\
    안녕하세요.
    웍스컴바인 김기정입니다.
    금일자로 주문건 접수되어 출고요청 전달드립니다.
    확인부탁드리겠습니다.
    항상 많은 도움주셔서 감사드립니다.
    김기정 드림
    ''')

#메소드 호출
ce.make_filenm_list()
ce.make_email_list()


# 이메일 발송
#인스턴스 생성
es = SendEmail('**', '**', 'email_list.xlsx')
#메소드 호출
es.send_email()
