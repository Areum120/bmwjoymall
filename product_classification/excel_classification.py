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

        # /구분자로 분류
        partners_name['partners'] = partners_name['브랜드'].str.split("/")
        # print(partners_name)

        brands =[]
        partners =[]
        for i, row in partners_name.iterrows():
            brands.append(row['partners'][0])
            if len(row['partners']) ==1:#요소가1개이면
                partners.append(row['partners'][0])#1번째요소=협력사
            else: #요소가2개이면
                partners.append(row['partners'][1])#2번째요소=협력사
        # partners_dict = dict(zip(brands, partners))# dict 변환
        # for key in partners_dict:
        # print(key, ':', partners_dict[key])# key,value 출력

        # print(partners_dict)
        print(brands)
        # print(len(brands))#110개
        print(partners)
        # print(len(partners))#110개

        self.brands = brands#find_product에서 활용
        self.partners = partners#find_product에서 활용

    # 각 상품명에 brands 요소가 있는지 모두 확인하여 partners 이름으로 각각 excel 저장 기능
    def find_product(self):
        path = 'data\\'
        num = list(range(110))
        for i, row in self.processd_df[:len(self.brands)].iterrows():#brands의 갯수만큼 돌리기
            # print(i)#132개
            # print(brands[i])
            num[i] = self.processd_df.loc[self.processd_df['상품명'].str.contains(self.brands[i])]#brands조회하여 df저장
            if len(num[i]) != 0:#df가 비어 있지 않으면
                self.partners[i] == num[i]#파트너사 변수 입력
                num[i].to_excel(f'{path}{self.partners[i]}.xlsx')#partners 이름으로 excel 저장
    #  brands[i] 갯수와 for문의 i 갯수가 다름, IndexError: list index out of range 해결->[:110]

#인스턴스 생성
CE = ClassificationExcel('sendRequest.xlsx', 'listOfPartners_name.xlsx')

#메소드 호출
CE.make_product_dict()
CE.find_product()


