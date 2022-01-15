import os
import pandas as pd
import datetime

class CreateEmailList:

    def __init__(self, df, col, path, title, text):
        self.df = df#data_file
        self.col = col#칼럼
        self.path = path#경로
        self.title = title#제목
        self.text = text#본문

    # filenm_list만들기
    def make_filenm_list(self):
        # 전체 칼럼 보기 설정
        pd.set_option('display.max_columns', None)

        # 협력사 data 불러오기
        partners = pd.read_excel(self.df, engine='openpyxl')
        # print(partners)

        # 브랜드 null값 삭제
        partners = partners.dropna(subset=[self.col])

        # null값 확인
        # print(partners.isnull().sum())

        self.partners = partners#make_email_list에서 변수로 활용

        # data폴더 파일 이름 목록 불러오기
        file_list = os.listdir(self.path)#경로
        # print(file_list)#attachment에 확장자명까지 기입

        # 확장자명 제외한 이름 출력
        file_name = []
        for file in file_list:
            if file.count(".")==1:
                name= file.split('.')[0]
                file_name.append(name)
            else:
                for i in range(len(file)-1, 0, -1):
                    if file[i]=='.':
                        file_name.append(file[:i])
                        break
        print(file_name)
        # print(len(file_name))#22개

        self.file_name = file_name#make_email_list에서 변수로 활용
        self.file_list = file_list#make_email_list에서 변수로 활용

    def make_email_list(self):
        # email_list df 만들기
        # 불러온 파일 업체명이 partners의 '브랜드' 업체명과 일치하면
        # 이메일1 -> recipient 변수명에 저장

        recipient=[]
        # 어차피 22개만 찾아야하므로 다돌릴 필요가 없음
        for i, row in self.partners[:22].iterrows():#변수 활용
            # print(i)#0~21
            find_brand = self.partners.loc[self.partners['브랜드'].str.contains(self.file_name[i])]#filenm과 일치하는 '브랜드'칼럼 df 출력, 변수 활용
            # print(find_brand.values)
            find_brand_list = find_brand.values.tolist()#행값 리스트 만들기
            recipient.append(find_brand_list[0][6])#이메일1만 추출해서 담기
        # print(recipient)

        # 불러온 파일명은 그대로 첨부파일 명에 기재
        attachment = self.file_list#변수 활용

        # df 생성(recipient, title, text, attachment)
        table_name = {
            'recipient':recipient,
            'title': self.title,# title 동일
            'text': self.text,# text 동일
            'attachment': attachment
        }
        email_list = pd.DataFrame(table_name)
        print(email_list)

        # 인덱스 컬럼 없이 값만 엑셀 저장
        email_list.to_excel('email_list.xlsx', index=False, header=False)
        print('파일 생성 완료')

now = datetime.datetime.now()  # 지금시간
nowToday = now.strftime('%m/%d')  # 일자

#인스턴스 생성
ce = CreateEmailList('.\\listOfPartners.xlsx', '브랜드', '.\\data\\', '[웍스컴바인] BMW JOY MALL ' + f'{nowToday} 상품발주 확인요청의 件', '''\
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
