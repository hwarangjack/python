import pyautogui as pyg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# now=pyg.position()
# pyg.screenshot('step5.png',region=(now.x,now.y,120,30))

# 향후 파일이름 생성시 변수 생성
user=pyg.prompt('집에서 작업하면 1, 사무실이면 2', title='공인인증서 횟수 선택')
yyyymm=pyg.prompt('yyyymm을 입력하세요 : ',title='대상연도(yyyy)와 월(mm)지정')
time_interval=float(pyg.prompt('프로그램의 실행속도를 입력하세요 (기본속도 1): ',title='Time Interval', default=1))
pw=pyg.password('공인인증서의 비밀번호를 입력하세요 : ', title='공인인증서')
pyg.confirm('프로그램을 실행합니다.')

# For 매크로 활용할 기초데이터 (개별사업장 클릭할 때 사용)
list=pd.read_excel('list.xlsx')
a=list.사업장관리번호.tolist()

# 셀레니움
url = 'https://edi.nhis.or.kr'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

#로그인
driver.find_element_by_css_selector('#pre_login > a:nth-child(1) > img').click()
time.sleep(2*time_interval)

#범용인증서 클릭 & 암호칸 입력
if user == 1:
    pyg.press('down')
    time.sleep(0.1*time_interval)
else:
    pass
pyg.press('down')
time.sleep(0.1*time_interval)
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

for i in a:
    try:
        #사업장리스트 클릭
            # four=pyg.locateCenterOnScreen('step4.png')
            # pyg.click(four.x,four.y,2)
            # time.sleep(2*time_interval)
        driver.find_element_by_css_selector('#loginAfter_box > dd.suim > img').click()
        
        # # 사업장 객체 클릭
            # five=pyg.locateCenterOnScreen('step5.png')
            # pyg.click(five.x-80,five.y-50)
            # time.sleep(0.5*time_interval)
            # pyg.press('down')
            # pyg.press('enter')
            # pyg.doubleClick(five.x,five.y-45)
            # pyg.press('delete')

        # #사업장명 입력

            # time.sleep(1*time_interval)
            # pyg.click(five.x-220,five.y+30,2)
            # time.sleep(1.5*time_interval)
        driver.switch_to_window(driver.window_handles[-1])
        driver.find_element_by_css_selector('#srchType').click()
        driver.find_element_by_css_selector('#srchType').send_keys(Keys.DOWN)
        driver.find_element_by_css_selector('#srchType').send_keys(Keys.ENTER)
        driver.find_element_by_css_selector('#srchType').send_keys(Keys.TAB)
        pyg.typewrite(str(i))
        pyg.press('enter')
        pyg.press('tab')
        time.sleep(0.1*time_interval)
        pyg.press('tab')
        time.sleep(0.1*time_interval)
        pyg.press('tab')
        time.sleep(0.1*time_interval)
        pyg.press('tab')
        time.sleep(0.1*time_interval)
        pyg.press('tab')
        time.sleep(0.1*time_interval)
        pyg.press('tab')
        time.sleep(0.1*time_interval)
        pyg.press('tab')
        time.sleep(0.1*time_interval)
        pyg.press('enter')
        time.sleep(2*time_interval)
        driver.switch_to_window(driver.window_handles[0])
        
        #받은문서 클릭
            # six=pyg.locateCenterOnScreen('step6.png')
            # pyg.click(six.x+630,six.y-15)
            # time.sleep(6*time_interval)
        driver.find_element_by_css_selector('#loginAfter_layout_right > div:nth-child(15) > div > a > img').click()

        #고지서 클릭
        seven=pyg.locateCenterOnScreen('step7-1.png')
        pyg.click(seven.x+80,seven.y)
        time.sleep(0.5*time_interval)
        pyg.press('down')
        pyg.press('down')
        pyg.press('enter')
        time.sleep(0.2*time_interval)
        pyg.click(seven.x+334,seven.y)
        time.sleep(0.7*time_interval)
        pyg.doubleClick(seven.x,seven.y+105)
        time.sleep(1.7*time_interval)

        #파일변환 클릭
        ten=pyg.locateCenterOnScreen('step10.png')
        pyg.click(ten.x-30,ten.y-40)
        time.sleep(1*time_interval)

        #개인별내역보기 클릭
        elev=pyg.locateCenterOnScreen('step11.png')
        pyg.click(elev.x+25,elev.y+250)
        time.sleep(2*time_interval)

        # 파일저장
        try:
            twv=pyg.locateCenterOnScreen('step12-1.png')
            pyg.click(twv.x+265,twv.y)
            time.sleep(1*time_interval)

        except:
            twv=pyg.locateCenterOnScreen('step12-2.png')
            pyg.click(twv.x+47,twv.y+75)
            time.sleep(1*time_interval)

        #다른이름저장
        pyg.typewrite('a')
        time.sleep(1.5*time_interval)
        filename=yyyymm+" "+str(i)+' rjsrkd'
        pyg.typewrite(filename)
        time.sleep(0.5*time_interval)
        pyg.press('enter')

        #현재창 종료
        fourt=pyg.locateCenterOnScreen('step14.png')
        pyg.click(fourt.x,fourt.y)
        pyg.keyDown('alt')
        time.sleep(0.1*time_interval)
        pyg.press('f4')
        time.sleep(0.1*time_interval)
        pyg.keyUp('alt')
        time.sleep(0.1*time_interval)

        #로그인 사업장 돌아가기
        thrt=pyg.locateCenterOnScreen('step13.png')
        pyg.click(thrt.x,thrt.y)
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
        thrt=pyg.locateCenterOnScreen('step13.png')
        pyg.click(thrt.x,thrt.y)
        time.sleep(1.5*time_interval)

print('오류사항을 제외하고 작업이 정상적으로 완료되었습니다.')