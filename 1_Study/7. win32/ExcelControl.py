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
path='C:\Users\화랑\Desktop\예시'
how='2021년\s*임금대장\s*.+[.]x+'
checkfile(path,how)
print(empty_list,'\n')

# Win32com 사용하여 객체 접근하기
excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = True
excel.displayalerts = False

for i in empty_list:
    wb = excel.workbooks.Open(i)


    #변경할 내용
    ws = wb.worksheets('(조건)')
    ws.cells(6,16).value = 0.1152
    ws.cells(16,18).value = 0.1152
    ws.cells(6,16).interior.colorindex = 27
    ws.cells(16,18).interior.colorindex = 27
    abs_name = os.path.split(i)
    dirpath = abs_name[0]
    filename = os.path.splitext(abs_name[1])[0]+"(py)"
    filedot = os.path.splitext(abs_name[1])[1]
    full_name = os.path.join(dirpath,filename+filedot)
    wb.SaveAs(os.path.join(dirpath,filename+filedot))
    print(os.path.basename(i)+' 완료')

    wb.Close()
