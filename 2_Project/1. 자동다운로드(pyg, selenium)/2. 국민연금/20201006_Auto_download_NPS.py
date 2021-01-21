import pyautogui as pyg
import pandas as pd
import time
import clipboard

# pyg.displayMousePosition()
yyyymm=pyg.prompt('yyyymm을 입력하세요 : ',title='대상연도(yyyy)와 월(mm)지정')
time_interval=float(pyg.prompt('프로그램의 실행속도를 입력하세요 (기본속도 1): ',title='Time Interval', default=1))
pw=pyg.password('공인인증서의 비밀번호를 입력하세요 : ', title='공인인증서')
pyg.confirm('프로그램을 실행합니다.')


#공통데이터에서 자료 추출하기
abs_path=r'D:\\NaverCloud\\화랑\\매출(자문).xlsm'
read_df1=pd.read_excel(abs_path, sheet_name='2021', skiprows=6)
df=pd.DataFrame(read_df1)
read_df2=df.iloc[:,[0,1,3,4,12]]                                      # 1차 가공) 일부 데이터만 사용하기
df2=pd.DataFrame(read_df2)                                                  # 가공데이터 DF로 배정하기 (자동완선기능 사용)
df2_1=df2[df2['계약유지']!='해지']
df2_2=df2_1[df2_1['급여지급일']!='법률자문']
df3=df2_2.dropna(thresh=3)
df3.set_index('구분', inplace=True)
df3.sort_values(by='사업장명',ascending=True, inplace=True)
df3.사업장관리번호=df3.사업장관리번호.apply(lambda x: int(x))
a=df3.사업장관리번호.tolist()

#------------- 최초 1회 로그인
    #국민연금 초기 홈페이지에서는 보안때문에 pyg.Screenshot 또는 pyg.typewriter가 작동하지 않음

#------------- 사업장 변환하며 시작되는 반복구문
for i in a:
    #100% 자동화가 안되어, 파일이름 먼저 따놓기
    file_name=yyyymm+' '+str(i)+' 연금'
    clipboard.copy(file_name)

    #사업장리스트 클릭
    pyg.click(1305,560)
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
    pyg.click(550,383,2)
    time.sleep(3*time_interval)
    pyg.click(807,314)
    time.sleep(3*time_interval)
    pyg.press('enter')
    time.sleep(2*time_interval)
    pyg.click(842,318)
    time.sleep(2*time_interval)
    pyg.click(1115,371)
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

    pyg.click(1440,150)
    time.sleep(1*time_interval)

pyg.confirm('프로그램을 모두 완료하엿습니다.')
