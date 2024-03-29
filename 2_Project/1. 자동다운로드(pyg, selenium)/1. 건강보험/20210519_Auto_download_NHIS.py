import pyautogui as pyg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


# 향후 파일이름 생성시 변수 생성
user=pyg.prompt('법인 공인인증서 위치', title='공인인증서 횟수 선택')
yyyymm=pyg.prompt('yyyymm을 입력하세요 : ',title='대상연도(yyyy)와 월(mm)지정')
time_interval=float(pyg.prompt('프로그램의 실행속도를 입력하세요 (기본속도 1): ',title='Time Interval', default=1))
pw=pyg.password('공인인증서의 비밀번호를 입력하세요 : ', title='공인인증서')
pyg.confirm('프로그램을 실행합니다.')

#공통데이터에서 자료 추출하기
abs_path=r'C:\\Users\\화랑\\Desktop\\1. 건강보험\\매출(자문).xlsm'
read_df1=pd.read_excel(abs_path, sheet_name='2021', skiprows=6)
df=pd.DataFrame(read_df1)
read_df2=df.iloc[:,[0,1,3,4,12]]                                      # 1차 가공) 일부 데이터만 사용하기
df2=pd.DataFrame(read_df2)                                                  # 가공데이터 DF로 배정하기 (자동완선기능 사용)
df2=df2[ (df2['계약유지']!='해지') & (df2['급여지급일']!='법률자문') ]
df3=df2.dropna(thresh=3)
df3.set_index('구분', inplace=True)
df3.sort_values(by='사업장명',ascending=True, inplace=True)
df3.사업장관리번호=df3.사업장관리번호.apply(lambda x: int(x))
a=df3.사업장관리번호.tolist()

# 셀레니움
url = 'https://edi.nhis.or.kr'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(20)

#로그인
driver.find_element_by_css_selector('#pre_login > a:nth-child(1) > img').click()
time.sleep(2*time_interval)

#범용인증서 클릭 & 암호칸 입력

for i in range(int(user)):
    pyg.press('down')
    time.sleep(0.1*time_interval)


pyg.press('enter')
time.sleep(0.1*time_interval)
pyg.press('tab')
time.sleep(0.1*time_interval)
pyg.press('tab')
time.sleep(0.1*time_interval)
pyg.press('tab')
time.sleep(0.1*time_interval)
pyg.press('tab')
time.sleep(0.1*time_interval)

#비밀번호 입력
pyg.typewrite(pw)
pyg.press('enter')
time.sleep(1.5*time_interval)


#  ------------- 사업장 변환하며 시작되는 반복구문
# locatecenteronscreen 함수 사용하지 않고 곧바로 클릭좌표 지정 >>> 고지서 클릭부터 Chrome 기준
one=[716,200]
two=[762,204]
three=[720,310]
four=[74,445]
five=[487,575]
six=[855,19]
seven=[604,399]

except_list = [
    79499005260,#더조은
    22087344060,#KSC
    20681735510,#천우토목
    21781177290,#현승이앤씨
    20481888200,#이엔에스
    11309683900,#조선시대
    # 65605013210,#삼곱식당
]

for i in a:

    if i in except_list:
        pass

    else:
        try:
            driver.switch_to_window(driver.window_handles[0])
            time.sleep(2*time_interval)
            
            #사업장리스트 클릭
            driver.find_element_by_css_selector('#loginAfter_box > dd.suim > img').click()
            time.sleep(1*time_interval)


            # #사업장명 입력
            driver.switch_to_window(driver.window_handles[-1])

            driver.find_element_by_css_selector('#srchType').click()
            driver.find_element_by_css_selector('#srchType').send_keys(Keys.DOWN)
            driver.find_element_by_css_selector('#srchType').send_keys(Keys.ENTER)
            driver.find_element_by_css_selector('#srchType').send_keys(Keys.TAB)
            pyg.typewrite(str(i))
            pyg.press('enter')
            driver.find_element_by_css_selector('#contents > table > tbody > tr:nth-child(2) > td:nth-child(3) > a').click()
           
            driver.switch_to_window(driver.window_handles[0])
            time.sleep(1*time_interval)
        
            
            #받은문서 클릭
            driver.find_element_by_css_selector('#loginAfter_layout_right > div:nth-child(15) > div > a > img').click()
            time.sleep(5*time_interval)

            #고지서 클릭
            pyg.click(one[0],one[1])
            time.sleep(0.5*time_interval)
            pyg.press('down')
            pyg.press('down')
            pyg.press('enter')
            
            time.sleep(1*time_interval)
            pyg.click(two[0],two[1])
            time.sleep(1*time_interval)
            pyg.doubleClick(three[0],three[1])
            time.sleep(1.7*time_interval)

            #파일변환 클릭
           
            pyg.click(four[0],four[1])
            time.sleep(1*time_interval)

            #개인별내역보기 클릭

            pyg.click(five[0],five[1])
            time.sleep(2*time_interval)


            #다른이름저장
            filename=yyyymm+" "+str(i)+' rjsrkd'
            pyg.typewrite(filename)
            time.sleep(0.5*time_interval)
            pyg.press('enter')

            #현재창 종료
            pyg.click(six[0],six[1])
            pyg.keyDown('alt')
            time.sleep(0.1*time_interval)
            pyg.press('f4')
            time.sleep(0.1*time_interval)
            pyg.keyUp('alt')
            time.sleep(0.1*time_interval)

            #로그인 사업장 돌아가기
            pyg.click(seven[0],seven[1])
            time.sleep(1.5*time_interval)

        except:
            print(str(i)+'사업장 작업을 진행하던 중 오류가 발생했습니다')
            #현재 오류창 닫기
            pyg.press('enter')
            pyg.press('esc')
            pyg.hotkey('alt','f4')
            time.sleep(0.1*time_interval)
            pyg.keyUp('alt')
            time.sleep(0.1*time_interval)

            #로그인 사업장으로 돌아가기
            pyg.click(seven[0],seven[1])
            time.sleep(1.5*time_interval)

print('오류사항을 제외하고 작업이 정상적으로 완료되었습니다.')