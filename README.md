# bmwjoymall RPA Guide

## 필요 라이브러리 설치 

pip install -r requirements.txt

## exe 실행파일 Build
- -w : 콜솔창x -F : onefile 

cd 폴더 설치 경로

pyinstaller -w -F run.py

## build 완료 시

dist 폴더에 run.exe 파일 생성 확인

## app 실행

dist 폴더 안에 필수 data file 이동시키기 

-listOfPartners.xlsx 

-sendRequest.xls 

## 주의 사항
- 파일명 변경x
