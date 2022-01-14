import pandas as pd

# sendRequest 불러오기
df = pd.read_excel('sendRequest.xlsx', engine='openpyxl')
# print(df)

# 브랜드/업체명 분류
partners_name = pd.read_excel('listOfPartners_name.xlsx', engine='openpyxl')
# print(partners_name)

# /구분자로 분류
# partners_name['partners'] = partners_name['브랜드'].str.split("/")
# print(partners_name)

# df파일 첫번째 행을 칼럼으로 지정
df2 = df.rename(columns=df.iloc[1])
# print(df2)

# 0~1행 삭제
df2 = df2.drop([df2.index[0], df2.index[1]])
# print(df2)

# 인덱스 재설정
df2=df2.reset_index(drop=True)
# print(df2)

# 상품명
# product_name = df2['상품명']
# print(product_name)

# df2 '상품명' partners_dict key와 부분일치 문자열 행 데이터 불러오기
# print(partners[0])

# 예시 검색어 부분일치 조회
# baseus = df2.loc[df2['상품명'].str.contains('베이스어스')]
# print(baseus['상품명'])

# 예시 딕셔너리 for문
# for key in partners_dict:
    # print(key, ':', partners_dict[key])


# 중첩함수 만들어서 brands 지역변수 활용
# brands, partners 리스트, dict 만드는 기능
def make_product_dict(df, col, col2):
    # 구분자 분류
    df[col] = df[col2].str.split("/")
    brands =[]
    partners =[]
    for i, row in df.iterrows():
        brands.append(row[col][0])
        if len(row[col]) ==1:#요소가1개이면
            partners.append(row[col][0])#1번째요소=협력사
        else: #요소가2개이면
            partners.append(row[col][1])#2번째요소=협력사
    # partners_dict = dict(zip(brands, partners))# dict 변환
    # print(partners_dict)
    # print(brands)
    # print(len(brands))#110개
    # print(partners)
    # print(len(partners))#110개

    # 각 상품명에 brands 요소가 있는지 모두 확인하여 partners 이름으로 각각 excel 저장 기능
    def find_product(df, col):
        path = 'data\\'
        num = list(range(110))
        for i, row in df[:110].iterrows():
            # print(i)#132개
            # print(brands[i])
            num[i] = df.loc[df[col].str.contains(brands[i])]#brands조회하여 df저장
            if len(num[i]) != 0:#df가 비어 있지 않으면
                partners[i] == num[i]#파트너사 변수 입력
                num[i].to_excel(f'{path}{partners[i]}.xlsx')#partners 이름으로 excel 저장
    #  brands[i] 갯수와 for문의 i 갯수가 다름, IndexError: list index out of range 해결->[:110]
    find_product(df2, '상품명')#함수 호출

make_product_dict(partners_name, 'partners', '브랜드')#함수 호출


