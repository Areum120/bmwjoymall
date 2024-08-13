# bmw joy mall RPA 개발(2022.01~2202.02)

## 쇼핑몰 상품 주문 요청서 엑셀파일 자동 생성 및 메일 자동화 개발

-주문요청서 브랜드사 별 엑셀파일 분류, parsing, excel form 생성, email list 생성 및 자동 발송
- language: python
- framework : GUI, GUI designer
- [기획서](https://shy-ferryboat-2ca.notion.site/RPA-c87df6d07b194e82acd97752ccdc0ac3) 

## bmwjoymall RPA Guide

### 필요 라이브러리 설치 

pip install -r requirements.txt

### exe 실행파일 Build
- -w : 콜솔창x -F : onefile 

cd 폴더 설치 경로

pyinstaller -w -F run.py

### build 완료 시

dist 폴더에 run.exe 파일 생성 확인

### app 실행

dist 폴더 안에 필수 data file 이동시키기 

-listOfPartners.xlsx 

-sendRequest.xls 

### 주의 사항
- 파일명 변경x
- 구글 이메일 계정으로 자동발송 시 구글 2단계 인증 설정 필요(2단계 설정 불가능 시 보안단계 낮추기)

# 24.08.13 update
C:\Users\tjfsu\Desktop\2023\크몽\AutoEase_rpa>pyinstaller --onefile --noconsole step2/excel_clsfn.py
'pyinstaller'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다. 오류시 

### 설치 경로 찾기
python -m site --user-site

예를 들어 아래 경로로 나오면 아래 경로 Scripts 폴더 안에 설치 되어 있음.
C:\Users\USERNAME\AppData\Roaming\Python\PythonXX\site-packages

아래 명령어로 설치하면 됨
C:\Users\USERNAME\AppData\Roaming\Python\PythonXX\Scripts\pyinstaller.exe --onefile --noconsole step2/order_rpa/excel_clsfn.py
