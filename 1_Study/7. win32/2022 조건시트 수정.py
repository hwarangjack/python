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


# # 파일지우기
# empty_list=[]
# path='C:\\users\\jjjac\\desktop\\HR\\☆ 자문'
# how='2022년\s*임금대장\s*.+(py)+'
# checkfile(path,how)

# for i in empty_list:
#     print(i)
#     os.remove(i)



# 대상파일 리스트로 정리하기
empty_list=[]
path='C:\\users\\jjjac\\desktop\\HR\\☆ 자문'
how='2022년\s*임금대장\s*.+[.]x+'
checkfile(path,how)
print(empty_list,'\n')


# Win32com 사용하여 객체 접근하기
excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = True
excel.displayalerts = False


for i in empty_list:
    wb = excel.workbooks.Open(i)
    ws = wb.worksheets('(조건)')

    #수정
    p5= ws.Range('p5')
    p5.value = 0.03495

    p6= ws.Range('p6')
    p6.value = 0.1227

    o17= ws.Range('o17')
    o17.value = "2022.1~2022.6"
    o18= ws.Range('o18')
    o18.value = "2022.7~2022.12"

    p17= ws.Range('p17')
    p17.value = 0.045
    p18= ws.Range('p18')
    p18.value = 0.045

    q17= ws.Range('q17')
    q17.value = 0.03495
    q18= ws.Range('q18')
    q18.value = 0.03495

    r17= ws.Range('r17')
    r17.value = 0.1227
    r18= ws.Range('r18')
    r18.value = 0.1227

    s17= ws.Range('s17')
    s17.value = 0.008
    s18= ws.Range('s18')
    s18.value = 0.009


    # 수정파일 저장
    List_Filename = os.path.splitext(i)
    filename = List_Filename[0]+"(win32com)"  # 파일명 변수지정 : 파일명을 확장자와 분리하고, 파일명 추가편집 
    filedot = List_Filename[1]                # 확장자 변수지정 : 확장자를 파일명과 분리
    wb.SaveAs(filename+filedot)
    wb.Close()
    print(i, '완료')
    
