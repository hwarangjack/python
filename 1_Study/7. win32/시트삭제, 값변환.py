import re
import os
import win32com.client
import time


# 파일탐색 함수
def checkfile(path, target):
    cp=re.compile(target)
    for i in os.listdir(path):
        abs_path = os.path.join(path,i)
        if os.path.isfile(abs_path):    #os.path.join 함수는 절대경로가 있는 파일만 Read 할 수 있는 것 같음
            if cp.match(i):
                empty_list.append(abs_path)
        elif os.path.isdir(abs_path):
            checkfile(abs_path, target)


# 대상파일 리스트로 정리하기
empty_list=[]
path=os.path.dirname(os.path.abspath(__file__))
how='^(홍성군청)*'
checkfile(path,how)


# Win32com 사용하여 객체 접근하기
excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = True
excel.displayalerts = False

for i in empty_list:
    print(i)
    wb = excel.workbooks.Open(i)
    ws1 = wb.worksheets('샘플자료')
    ws1.Range('a1:o55').value = ws1.Range('a1:o55').value

    ws2 = wb.worksheets('기초산정표')
    ws3 = wb.worksheets('명단')
    ws2.Delete()
    ws3.Delete()

    # 수정파일 저장
    abs_name = os.path.split(i)  # 리스트로 구분 : 절대경로 & 파일명(확장자 포함)
    dirpath = abs_name[0]        # 절대경로 변수지정
    Full_Filename = abs_name[1]
    List_Filename = os.path.splitext(Full_Filename)
    filename = List_Filename[0]+"(20210810)"  # 파일명 변수지정 : 파일명을 확장자와 분리하고, 파일명 추가편집 
    filedot = List_Filename[1]                # 확장자 변수지정 : 확장자를 파일명과 분리
    Re_abs_name = os.path.join(dirpath,filename+filedot)        # 절대경로 재편집 : 기존 절대경로 + 편집 파일명
    wb.SaveAs(Re_abs_name[:-1], FileFormat=56)      # FileFormat : 51(.xlsx) 56(.xls)
    wb.Close()
    print(os.path.basename(i)+' 완료')
    
