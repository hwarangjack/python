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
path='C:\\Users\\user\\Desktop\\예시'
how='2021년\s*임금대장\s*.+[.]x+'
checkfile(path,how)
print(empty_list,'\n')


# Win32com 사용하여 객체 접근하기
excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = True
excel.displayalerts = False

for i in empty_list:
    wb = excel.workbooks.Open(i)

    # 수정1 (특별공제 제외방식 수정)
    try:
        ws=wb.worksheets('임금대장 (세무)')

    except:
        try:
            ws=wb.worksheets('임금대장(세무)')

        except:
            ws=wb.worksheets('임금대장')

    cell= ws.Range('cb18')
    cell.value = "=CA18-CC18"
    cell.autofill(ws.Range('CB18:CB500'))
    
    cell= ws.Range('cg18')
    cell.value = "=$CB18-$BZ18"
    cell.autofill(ws.Range('cg18:cg500'))

    cell= ws.Range('ch18')
    cell.value = '=IF(RIGHT(T18,3)="퇴사자",0,CB18-$BZ18)'
    cell.autofill(ws.Range('ch18:ch500'))

    # 수정2 (퇴직금 산정방식 중 2월 산정방식 수정)
    ws2 = wb.worksheets('퇴직금')
    cell = ws2.Range('r12')
    cell.value = '=IF(OR(N12="말일",N12=31),IF(EOMONTH(AJ12,0)=AJ12,"",X11-1),IF(N12=DAY(AJ12),"",X11-1))'

    # 수정파일 저장
    abs_name = os.path.split(i)  # 리스트로 구분 : 절대경로 & 파일명(확장자 포함)
    dirpath = abs_name[0]        # 절대경로 변수지정
    Full_Filename = abs_name[1]
    List_Filename = os.path.splitext(Full_Filename)
    filename = List_Filename[0]+"(특별공제, 퇴직금)"  # 파일명 변수지정 : 파일명을 확장자와 분리하고, 파일명 추가편집 
    filedot = List_Filename[1]                # 확장자 변수지정 : 확장자를 파일명과 분리
    Re_abs_name = os.path.join(dirpath,filename+filedot)        # 절대경로 재편집 : 기존 절대경로 + 편집 파일명
    wb.SaveAs(Re_abs_name)
    print(os.path.basename(i)+' 완료')

    wb.Close()
    
