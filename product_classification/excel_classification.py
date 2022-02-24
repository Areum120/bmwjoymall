import pandas as pd


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

        path = 'data\\'
        num = list(range(len(self.brands)))
        for i, row in self.processd_df.iterrows():#엑셀 주문 건수 갯수만큼 돌리기
           # print(row)
           for j in range(len(self.brands)):#brands의 갯수만큼 돌리기
               # print(self.brands[j][0])#리스트의 값만 뽑기
               # print(row['상품명'])
               if self.brands[j][0] in row['상품명']:#전체 df 상품명에서 brands 값명이 있으면
                   num[j] = row #df를 num[j]에 저장
                   print(num[j])
                   if len(num[j]) != 0:#df가 비어 있지 않으면
                       self.partners[j] == num[j]#파트너사 변수와 1:1 맵핑
                       num[j].to_excel(f'{path}{self.partners[j]}.xlsx')#partners 이름으로 excel 저장


# #인스턴스 생성
# CE = ClassificationExcel('sendRequest.xlsx', 'listOfPartners.xlsx')#sendRequest.xlsx, listOfPartners_name.xlsx->listOfPartners 자동입력
#
# #메소드 호출
# CE.make_product_dict()
# CE.find_product()


