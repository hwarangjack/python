import pyautogui as pyg
import pandas as pd
import time
import clipboard

# pyg.displayMousePosition()
yyyymm=pyg.prompt('yyyymm을 입력하세요 : ',title='대상연도(yyyy)와 월(mm)지정')
time_interval=float(pyg.prompt('프로그램의 실행속도를 입력하세요 (기본속도 1): ',title='Time Interval', default=1))
pw=pyg.password('공인인증서의 비밀번호를 입력하세요 : ', title='공인인증서')
pyg.confirm('프로그램을 실행합니다.')

# For 매크로 활용할 기초데이터 (개별사업장 클릭할 때 사용)
list=pd.read_excel('list.xlsx')
a=list.사업장관리번호.tolist()


#------------- 최초 1회 로그인
    #국민연금 초기 홈페이지에서는 보안때문에 pyg.Screenshot 또는 pyg.typewriter가 작동하지 않음

#------------- 사업장 변환하며 시작되는 반복구문
for i in a:
    #100% 자동화가 안되어, 파일이름 먼저 따놓기
    file_name=yyyymm+' '+str(i)+' 연금'
    clipboard.copy(file_name)

    #사업장리스트 클릭
    pyg.click(1303,603)
    time.sleep(3*time_interval) 

    #개별사업장 조회 및 결정        
    pyg.press('tab')
    time.sleep(0.2*time_interval)
    pyg.press('down')
    time.sleep(0.2*time_interval)
    pyg.press('enter')
    time.sleep(0.2*time_interval)
    pyg.press('tab')
    time.sleep(0.2*time_interval)
    pyg.typewrite(str(i))
    time.sleep(0.2*time_interval)
    pyg.press('enter')
    time.sleep(1.5*time_interval)
    pyg.press('tab')
    time.sleep(0.3*time_interval)
    pyg.press('tab')
    time.sleep(0.3*time_interval)
    pyg.press('tab')
    time.sleep(0.3*time_interval)
    pyg.press('tab')
    time.sleep(0.3*time_interval)
    pyg.press('tab')
    time.sleep(0.3*time_interval)
    pyg.press('enter')
    time.sleep(8*time_interval)

    #보험료결정내역 클릭
    pyg.click(525,380,2)
    time.sleep(3*time_interval)
    pyg.click(714,310)
    time.sleep(3*time_interval)
    pyg.press('enter')
    time.sleep(2*time_interval)
    pyg.click(832,308)
    time.sleep(2*time_interval)
    pyg.click(1115,370)
    time.sleep(2*time_interval)
    pyg.press('tab')
    time.sleep(0.2*time_interval)
    pyg.press('down')
    time.sleep(0.2*time_interval)
    pyg.press('down')
    time.sleep(0.2*time_interval)
    pyg.press('tab')
    time.sleep(0.2*time_interval)
    pyg.press('tab')
    time.sleep(0.2*time_interval)
    pyg.press('tab')
    time.sleep(0.2*time_interval)
    pyg.press('tab')
    time.sleep(0.2*time_interval)
    pyg.press('tab')
    time.sleep(0.2*time_interval)
    pyg.typewrite(pw)
    time.sleep(0.2*time_interval)
    pyg.press('enter')
    time.sleep(4*time_interval)

    # 파일저장이 나오는 칸에서 오류가 나옴 '''pyg.typewrite(yyyymm+' '+str(i)+' dusrma') / time.sleep(0.2*time_interval)''' 임시방편으로 clipboard 모듈 사용하여 붙여넣기 수작업을 추가하도록 함
    pyg.confirm('다음 사업장을 진행하시겠습니까?')

    pyg.click(1464,129)
    time.sleep(1*time_interval)

pyg.confirm('프로그램을 모두 완료하엿습니다.')