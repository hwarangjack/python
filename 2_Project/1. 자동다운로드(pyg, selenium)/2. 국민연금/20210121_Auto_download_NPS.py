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
#------------- 사업장 변환하며 시작되는 반복구문

for i in a:
    
    # 화면전환시간
    time.sleep(2*time_interval)

    # 파일저장이름 준비
    file_name=yyyymm+' '+str(i)+' dusrma'

    #사업장전환 클릭
    pyg.click(1758,87) 
    time.sleep(4*time_interval)

    #사업장관리번호 입력
    pyg.press('tab')
    time.sleep(0.5*time_interval)
    pyg.press('up')
    time.sleep(0.5*time_interval)
    pyg.press('tab')
    time.sleep(0.5*time_interval)
    pyg.typewrite(str(i))
    time.sleep(1*time_interval)
    pyg.press('enter')
    time.sleep(1.5*time_interval)

    #개별사업장 클릭
    pyg.click(971,335,2) 
    time.sleep(10*time_interval)

    #보험료결정내역 클릭
    pyg.click(97,533) 
    time.sleep(1*time_interval)
    pyg.click(97,569) 
    time.sleep(2*time_interval)

    #최신 보험료내역 클릭
    pyg.click(828,368,2) 
    time.sleep(2.5*time_interval)

    #통합저장
    pyg.click(1848,366) 
    time.sleep(5*time_interval)

    #파일이름 입력
    pyg.typewrite(str(file_name))
    time.sleep(1*time_interval)
    pyg.press('enter')
    time.sleep(1*time_interval)

    #크롬 하단 다운로드 표시 X 클릭
    ppyg.click(1900,1009) 
    time.sleep(1*time_interval)

    print(file_name+' 완료')


pyg.confirm('프로그램을 모두 완료하엿습니다.')
