from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import sleep
import pandas as pd
import pyautogui as pyg



interval=1

def repeat_Tab(num):
    standard=0
    while standard < num:
        pyg.press('tab')
        sleep(0.05*interval)
        standard = standard + 1


numm=input('신고대상 사업장관리번호 입력 :')
yymmdd='870112'
id_num='1066912'

url='http://total.kcomwel.or.kr/main.do'
driver=webdriver.Ie()
driver.get(url)
driver.maximize_window()

#로그인 직전까지 진입

driver.find_elements_by_css_selector('.utilmenu ul > li')[0].click()
driver.find_element_by_css_selector('#t3').click()
driver.find_element_by_css_selector('#u_group_fg_5').click()
driver.find_element_by_css_selector('#rgno3_1').send_keys(yymmdd)
driver.find_element_by_css_selector('#rgno3_2').click()
driver.find_element_by_css_selector('#rgno3_2').send_keys(id_num)
driver.implicitly_wait(10*interval)


# 공인인증서 로그인 -> ID/PW 입력

pyg.press('tab')
sleep(0.2*interval)

pyg.press('enter')
sleep(2*interval)

repeat_Tab(7)
sleep(0.2*interval)

pyg.press('down')
sleep(0.2*interval)

repeat_Tab(4)
pyg.typewrite('wlffjt87{}')
sleep(0.2*interval)

pyg.press('enter')

sleep(5*interval)


# 로그인 후 발생하는 팝업창 제거
if len(driver.window_handles) > 1:
    try:
        for i in len(driver.window_handles):
            i=i-1
            if i > 0:
                driver.switch_to_window(driver.window_handles[i])
                driver.close()
    except:
        pass

driver.implicitly_wait(10*interval)

# 민원접수/신고 진입 -> 자격관리 진입 -> 상실신고 진입
driver.find_element_by_css_selector('.depthBox6.m2 > ul > li > ul > li > a').click()
driver.find_element_by_css_selector('#10001011_head > a').click()
driver.find_elements_by_css_selector('#10001011 > li')[1].click()
driver.implicitly_wait(12*interval)
sleep(5)

# 객체 사업자등록번호 진입 // +++ 판다스와 for 구문으로 객체 사업장관리번호 돌리기
pyg.click(1155,516)
sleep(0.2*interval)
repeat_Tab(8)
sleep(0.2*interval)

pyg.typewrite(numm)
sleep(5*interval)



# 개별대상자 입력                       

repeat_Tab(15)
sleep(0.2*interval)

df=pd.read_excel('상실리스트.xlsx')
lets_list=df.values.tolist()

start=0
while start < len(lets_list):
    id_num=str(lets_list[start][3]) #주민등록번호
    year_money=str(lets_list[start][9]) #당해년도 보수총액
    year_month=str(lets_list[start][10]) #당해년도 근무개월수
    quit_date=str(lets_list[start][8]) #상실일자
    quit_reason=lets_list[start][6] #상실사유 ※ Down 이동횟수
    quit_explain=lets_list[start][7] # 상실 상세사유

    # 주민등록번호 입력
    pyg.typewrite(id_num)
    sleep(0.2*interval)
    pyg.press('enter')
    sleep(4*interval)

    repeat_Tab(4)
    pyg.typewrite(quit_date)

    pyg.press('tab')
    sleep(0.2*interval)

    pyg.typewrite(year_money)
    sleep(0.2*interval)

    repeat_Tab(2)
    while quit_reason > 0:
        pyg.press('down')
        sleep(0.2*interval)
        quit_reason=quit_reason-1

    pyg.press('tab')
    pyg.typewrite(quit_explain)
    sleep(0.2*interval)

    repeat_Tab(5)
    pyg.press('down')
    sleep(0.2*interval)
    pyg.press('down')
    sleep(0.2*interval)

    repeat_Tab(3)
    pyg.press('down')
    sleep(0.2*interval)

    pyg.press('tab')
    sleep(0.2*interval)
    pyg.typewrite(year_money)
    sleep(0.2*interval)         
    
    pyg.press('tab')
    sleep(0.2*interval)
    pyg.typewrite(year_month)
    sleep(0.2*interval)

    pyg.press('tab')
    sleep(0.2*interval)
    pyg.typewrite('0')
    sleep(0.2*interval)

    pyg.press('tab')
    sleep(0.2*interval)
    pyg.typewrite('0')
    sleep(0.2*interval)

    repeat_Tab(2)
    pyg.press('enter')

    pyg.keyDown('shift')
    sleep(0.5*interval)
    repeat_Tab(25)
    pyg.keyUp('shift')
    sleep(0.5*interval)

    start=start+1                       


print('명령어가 종료됬습니다')



sleep(100)

driver.close()
