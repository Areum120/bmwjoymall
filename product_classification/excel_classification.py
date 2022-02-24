import pandas as pd
import datetime
from openpyxl.styles import Font
from openpyxl import load_workbook

class ClassificationExcel:
    #Constructor
    def __init__(self, df, df2):
        self.df = df#주문파일(1page)
        self.df2 = df2#파트너사정보파일

    # brands, partners 리스트, dict 만드는 기능
    def make_product_dict(self):

        # sendRequest 불러오기
        df = pd.read_excel(self.df, engine='openpyxl')
        # print(df)

        # df파일 첫번째 행을 칼럼으로 지정
        processed_df = df.rename(columns=df.iloc[1])
        # print(df2)

        # 0~1행 삭제
        processed_df = processed_df.drop([processed_df.index[0], processed_df.index[1]])
        # print(processed_df)

        # 인덱스 재설정
        processed_df = processed_df.reset_index(drop=True)
        # print(processed_df)

        # 상품명
        # product_name = processed_df['상품명']
        # print(product_name)

        # processed_df '상품명' partners_dict key와 부분일치 문자열 행 데이터 불러오기
        # print(partners[0])

        # 예시 검색어 부분일치 조회
        # baseus = processed_df.loc[df2['상품명'].str.contains('베이스어스')]
        # print(baseus['상품명'])

        self.processd_df = processed_df #가공한 df파일, #find_product에서 활용

        # 브랜드/업체명 파일 불러오기
        partners_name = pd.read_excel(self.df2, engine='openpyxl')
        # print(partners_name)

        # '브랜드' 칼럼 결측치있는 행 전체 제거
        partners_name = partners_name.dropna(axis = 'index', how='any', subset=['브랜드'])
        # print(partners_name)

        # 브랜드 list 생성
        brands = partners_name['브랜드'].str.split('/').tolist()

        # 업체명 list 생성
        partners = partners_name['업체명'].tolist()

        print(brands)
        print(partners)
        print(len(brands))#115개
        print(len(partners))#115개

        # 결측치 확인
        # print(partners_name[partners_name.partners.isnull()])

        # dict 변환
        # partners_dict = dict(zip(brands, partners))
        # for key in partners_dict:
        # print(key, ':', partners_dict[key])# key,value 출력

        # print(partners_dict)

        self.brands = brands#find_product에서 활용
        self.partners = partners#find_product에서 활용

    # 각 상품명에 brands 요소가 있는지 모두 확인하여 partners 이름으로 각각 excel 저장 기능
    def find_product(self):
        # data폴더 자동 생성 기능 추가하기

        now = datetime.datetime.now()  # 지금시간
        self.nowToday = now.strftime('%Y-%m-%d')  # 일자

        self.path = 'data\\'
        for i, row in self.processd_df.iterrows():#엑셀 주문 건수 갯수만큼 돌리기
           # print(i, row)
           for j in range(len(self.brands)):#brands의 갯수만큼 돌리기
               # print(self.brands[j][0])#리스트의 값만 뽑기
               # print(row['상품명'])
               if self.brands[j][0] in row['상품명']:#전체 df 상품명에서 brands 값명이 있으면
                   # df 생성(recipient, title, text, attachment)
                   table_name = {#엑셀 세로로 저장되는 문제 가로로 저장하기 위한 1:1 딕셔너리 맵핑
                       '주문번호': row['주문번호'],
                       '상품번호': row['상품번호'],
                       '상품코드': row['상품코드'],
                       '바코드': row['바코드'],
                       '주문자': row['주문자'],
                       '수령인': row['수령인'],
                       '전화번호': row['전화번호'],
                       '핸드폰': row['핸드폰'],
                       '상품명': row['상품명'],
                       '옵션': row['옵션'],
                       '수량': row['수량'],
                       '판매가격': row['판매가격'],
                       '옵션가격': row['옵션가격'],
                       '총판매가격': row['총판매가격'],
                       '배송비구분': row['배송비구분'],
                       '배송비': row['배송비'],
                       '무료배송금액': row['무료배송금액'],
                       '실 배송비': row['실 배송비'],
                       '주문일': row['주문일'],
                       '주소': row['주소'],
                       '주문시요구사항': row['주문시요구사항'],
                   }
                   excel_table = pd.DataFrame(table_name, index=[0])
                   print(excel_table)
                   if len(excel_table) != 0:#df가 비어 있지 않으면
                       self.partners[j] == excel_table#파트너사 변수와 1:1 맵핑
                       excel_table.to_excel(f'{self.path}[웍스컴바인]발주요청서_{self.nowToday}_{self.partners[j]}.xlsx', index=False)#partners 이름으로 excel 저장, index없이 저장

    # 저장한 주문파일 엑셀 시트 내용 수정하기
    # def change_excel_sheet(self):
    #     # 폴더 안의 엑셀 파일 하나씩 불러오기
    #     wb = load_workbook(f'{self.path}[웍스컴바인]발주요청서_2022-02-24_AUTOCOS.xlsx')#엑셀파일 가져오기
    #     ws = wb.active #활성화
    #     # 1,2행을 새로 삽입한다
    #     # 전체 행 개수를 세서 num 변수에 삽입
    #     # 1행에 f'발송요청내역 [총 {num}건, 1 페이지] {self.nowToday}'
    #     # 열 너비를 설정
    #     ws.columns_dimensions[['A']['U']].width = 15
    #     wb.save(f'{self.path}[웍스컴바인]발주요청서_2022-02-24_AUTOCOS.xlsx')


#인스턴스 생성
CE = ClassificationExcel('sendRequest.xlsx', 'listOfPartners.xlsx')#sendRequest.xlsx, listOfPartners_name.xlsx->listOfPartners 자동입력

#메소드 호출
CE.make_product_dict()
CE.find_product()
# CE.change_excel_sheet()

