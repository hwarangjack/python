import datetime
import pyautogui as pyg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os, re, time, json



def getValue(JsonKey):
    dirName = os.path.dirname(__file__)
    fileName = 'customInfo.json'
    absFile = os.path.join(dirName, fileName)
    with open(absFile, "rb") as f:
        loadedJson = json.loads(f.read())
    return loadedJson[JsonKey]    

def id(value):
    return value.성명[0]+value.주민등록번호[0:6]

def targetData():
    abs_path = getValue('path')
    df = pd.read_excel(abs_path)
    df = df[
        (df['contract1']=='유지')&
        (df['contract4']!='제외')&
        (df['pay3']!='법률자문')
    ]
    df['company3'] = df['company3'].apply(lambda x: x.replace('-',''))
    List = df['company3'].values.tolist()

    # 그린푸드 사업자등록번호 != 사업자관리번호 바꾸기
    targetData = {
        '92229218731':'13286333830',
    }

    for i in targetData.keys():
        indexNum = List.index(i)
        List[indexNum] = targetData[i]


    return List

def targetDataDict():
    abs_path = getValue('path')
    df = pd.read_excel(abs_path)
    df = df[
        (df['contract1']=='유지')&
        (df['contract4']!='제외')&
        (df['pay3']!='법률자문')
    ]
    name = df['company1'].values.tolist()
    num = targetData()
    dictData = dict(zip(num,name))
    return dictData

def NHIS_download(yyyymm, time_interval, certifiedIndexNum):
    pyg.confirm('프로그램을 실행합니다.')

    # 대상 사업장
    a = targetData()


    # 제외 사업장
    except_list = [
    ]

    # 셀레니움
    url = 'https://edi.nhis.or.kr'
    # driver = webdriver.Chrome()
    driver = webdriver.Edge()
    driver.get(url)
    driver.maximize_window()

    time.sleep(50)

    #로그인
    driver.find_element_by_css_selector('#pre_login > a:nth-child(1) > img').click()
    time.sleep(2*time_interval)

    #범용인증서 클릭 & 암호칸 입력

    for i in range(int(certifiedIndexNum)-1):
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
    pyg.typewrite(getValue('password'))
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


    index = 0
    success = 0
    fail = 0
    for i in a:
        
        print(f'총진행:{index}/{len(a)}  , 성공:{success} , 실패:{fail}')

        if i in except_list:
            pass

        else:
            try:
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(2*time_interval)
                
                #사업장리스트 클릭
                driver.find_element_by_css_selector('#loginAfter_box > dd.suim > img').click()
                time.sleep(1*time_interval)


                # #사업장명 입력
                driver.switch_to.window(driver.window_handles[-1])

                driver.find_element_by_css_selector('#srchType').click()
                driver.find_element_by_css_selector('#srchType').send_keys(Keys.DOWN)
                driver.find_element_by_css_selector('#srchType').send_keys(Keys.ENTER)
                driver.find_element_by_css_selector('#srchType').send_keys(Keys.TAB)
                pyg.typewrite(str(i))
                pyg.press('enter')
                driver.find_element_by_css_selector('#contents > table > tbody > tr:nth-child(2) > td:nth-child(3) > a').click()
            
                driver.switch_to.window(driver.window_handles[0])
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
                time.sleep(2*time_interval)

                #개인별내역보기 클릭
                pyg.click(five[0],five[1])
                time.sleep(2*time_interval)




                '''
                CHROME용
                '''

                # #다른이름저장
                # filename=yyyymm+" "+str(i)+' rjsrkd'
                # pyg.typewrite('filename')
                # time.sleep(0.5*time_interval)
                # pyg.press('enter')

                # #현재창 종료
                # pyg.click(six[0],six[1])
                # pyg.keyDown('alt')
                # time.sleep(0.1*time_interval)
                # pyg.press('f4')
                # time.sleep(0.1*time_interval)
                # pyg.keyUp('alt')
                # time.sleep(0.1*time_interval)

                # #로그인 사업장 돌아가기
                # pyg.click(seven[0],seven[1])
                # time.sleep(1.5*time_interval)

                # # 이름변경targetDataDict()[i]
                # path = os.path.dirname(getValue('path'))
                # beforeName = os.path.join(path, f'{filename}.xls')
                # afterName = os. path.join(path, f'{yyyymm} {targetDataDict()[i]} 건강.xls')
                # if os.path.exists(beforeName):
                    
                #     os.rename(beforeName, afterName)
                #     print(f'{beforeName}파일을 {afterName}으로 변경했습니다.')




                '''
                EDGE용
                '''
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

                # 이름변경targetDataDict()[i]
                path = os.path.dirname(getValue('path'))
                beforeName = os.path.join(path, f'보험료_고지(산출)_내역서_{datetime.datetime.today().strftime("%Y%m%d")}.xls')
                afterName = os.path.join(path, f'{yyyymm} {targetDataDict()[i]} 건강.xls')
                if os.path.exists(beforeName):
                    
                    os.rename(beforeName, afterName)
                    print(f'{beforeName}파일을 {afterName}으로 변경했습니다.')
                    success += 1
                

            except:
                print(targetDataDict()[i]+' 을 진행하던 중 오류가 발생했습니다')
                fail += 1
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
            
            index += 1

    print('오류사항을 제외하고 작업이 정상적으로 완료되었습니다.')

def NPS_download(yyyymm, time_interval):

    # 대상 사업장
    a = targetData()

    # 제외 사업장
    except_object =[
        61605986810, # 시온관리
    ]

    # 조정계수
    plusX = 0
    plusY = 0
    # plusY = 30


    #------------- 사업장 변환하며 시작되는 반복구문

    for i in a:
        
        if i in except_object:
            pass

        else:    
            # 화면전환시간
            time.sleep(2*time_interval)

            # 파일저장이름 준비
            file_name=f'{yyyymm} {i} dusrma'

            #사업장전환 클릭
            pyg.click(1758,87+plusY) 
            time.sleep(2*time_interval) 

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
            time.sleep(1*time_interval)

            #개별사업장 클릭
            pyg.click(971,330+plusY,2) 
            time.sleep(7*time_interval)

            #보험료결정내역 클릭
            pyg.click(97,533+plusY) 
            time.sleep(1*time_interval)
            pyg.click(97,569+plusY) 
            time.sleep(2*time_interval)

            #최신 보험료내역 클릭
            pyg.click(828,368+plusY,2) 
            time.sleep(2.5*time_interval)

            # 직권상실 안내창 뜰 경우 클릭
            pyg.click(960,630+plusY,2) 
            time.sleep(1*time_interval)

            #통합저장
            pyg.click(1848,366+plusY) 
            time.sleep(5*time_interval)

            #파일이름 입력
            pyg.typewrite(str(file_name))
            time.sleep(1*time_interval)
            pyg.press('enter')
            time.sleep(1*time_interval)

            #크롬 하단 다운로드 표시 X 클릭
            pyg.click(1900,1009) 
            time.sleep(1*time_interval)

            # 이름변경targetDataDict()[i]
            path = os.path.dirname(getValue('path'))
            beforeName = os.path.join(path, f'{file_name}.xlsx')
            afterName = os. path.join(path, f'{yyyymm} {targetDataDict()[i]} 연금.xlsx')
            if os.path.exists(beforeName):
                os.rename(beforeName, afterName)
                print(f'{beforeName}파일을 {afterName}으로 변경했습니다.')
            else:
                print(beforeName, afterName)
                print('파일이름을 찾지 못했습니다')


    pyg.confirm('프로그램을 모두 완료하엿습니다.')

def transFileName(yyyymm):
    dictData = targetDataDict()
    baseDir = os.path.dirname(getValue('path'))

    for i in os.listdir(baseDir):
        if '(종합)' in i.split():
            pass

        else:
            if i.startswith(str(yyyymm)) and\
                (i.endswith('.xls') or i.endswith('.xlsx')):
                j=i.split(' ')
                k=i.replace(j[1],dictData[j[1]])

                if k in os.listdir(baseDir):
                    print(k+'의 파일이 이미 존재합니다')

                else:
                    os.rename(os.path.join(baseDir,i),os.path.join(baseDir,k))
                    print(k,'로 변경했습니다')
        

    for i in os.listdir(baseDir):
                # # Last Name 수정
        if '(종합)' in i.split():
            pass

        else:
            if i.startswith(str(yyyymm)) and\
                (i.endswith('rjsrkd.xls') or i.endswith('rjsrkd.xlsx')):

                j=i.replace('rjsrkd','건강')
                if j in os.listdir(baseDir):
                    print(j+'의 파일이 이미 존재합니다.')
                else:
                    os.rename(os.path.join(baseDir,i),os.path.join(baseDir,j))
                    print(j)



            if i.startswith(str(yyyymm)) and\
                (i.endswith('dusrma.xls') or i.endswith('dusrma.xlsx')):

                j=i.replace('dusrma','연금')
                if j in os.listdir('.'):
                    print('j[1]', j[1] , type(j[1]))
                    print('dictData[j[1]]', dictData[j[1]], type(dictData[j[1]]))
                    print(j+'의 파일이 이미 존재합니다.')
                else:
                    os.rename(os.path.join(baseDir,i),os.path.join(baseDir,j))
                    print(j)

def integrating(yyyymm):
    baseDir = os.path.dirname(getValue('path'))
    surfix = ' (종합).xlsx'
    cp1 = re.compile('.+[.]x+')
    cp2 = re.compile(surfix)
    object_list=[] 
    for i in os.listdir(baseDir):
        if i.startswith(str(yyyymm)) and cp1.match(i):
            j = os.path.splitext(i)[0]
            k=j[7:len(j)-3]

            if k not in object_list:
                object_list.append(k)

    # 건강보험료와 연금보험료 파일을 하나로 연결
    for name in object_list:
        print(name)
        #표준파일 생성
        standard_name=str(yyyymm)+' '+name
        standard=pd.ExcelWriter(standard_name+surfix, engine='xlsxwriter')
        
        #건강보험 작업
        filename=standard_name+' 건강.xls'
        if os.path.isfile(os.path.join(baseDir, filename)):
            n4=pd.read_excel(os.path.join(baseDir, filename), sheet_name=0)
            n2=n4
            n2['id']=n2.apply(id, axis=1)
            n2=n2.set_index('id')
            n2=n2.reindex(columns=['성명','주민등록번호','취득일','상실일','보수월액','산출보험료','요양산출보험료','정산사유','정산금액','요양정산사유코드','요양정산보험료','연말정산','요양연말정산보험료','시작월','종료월','요양시작월','요양종료월'])
        else:
            n2=pd.DataFrame(range(0,2))
            n4=n2
            print('----> '+name+'의 건강보험 파일이 존재하지 않습니다.')

        #연금보험 작업
        filename1=standard_name+' 연금.xlsx'
        if os.path.isfile(os.path.join(baseDir, filename1)):
            n5=pd.read_excel(os.path.join(baseDir, filename1), sheet_name=0)
            n3=n5        
            n3['id']=n3.apply(id, axis=1)
            n3=n3.set_index('id')
            n3=n3.reindex(columns=['성명','주민등록번호','취득일','상실일','당월분_기준소득월액','당월분_(본인기여금)','소급분_해당기간','소급분_(본인기여금)','자격변동 신고사항_(본인기여금)','취득월   납부여부'])
            
            n3['당월분_(본인기여금)'] = n3['당월분_(본인기여금)'].apply(pd.to_numeric)
            n3['당월분_기준소득월액'] = n3['당월분_기준소득월액'].apply(pd.to_numeric)
            n3['자격변동 신고사항_(본인기여금)'] = n3['자격변동 신고사항_(본인기여금)'].fillna('0')
            n3['자격변동 신고사항_(본인기여금)'] = n3['자격변동 신고사항_(본인기여금)'].apply(pd.to_numeric)

        else:
            n3=pd.DataFrame(range(0,2))
            n5=n3
            print('----> '+name+'의 연금보험 파일이 존재하지 않습니다.')


        #건강과 연금파일 합치기 // 2개 파일의 index  기준으로 합치려면, left_index=true, right_index=true 형식으로 작성
        n1=pd.merge(n2,n3, left_index=True, right_index=True, how='outer')
        n1=n1.reindex(columns=['성명_x','주민등록번호_x','취득일_x','상실일_x','산출보험료','요양산출보험료','정산사유','정산금액','요양정산사유코드','요양정산보험료','연말정산','요양연말정산보험료','당월분_(본인기여금)','자격변동 신고사항_(본인기여금)'])
        n1.loc['합계']=n1[['산출보험료','요양산출보험료','정산금액','요양정산보험료','당월분_(본인기여금)','자격변동 신고사항_(본인기여금)']].sum(axis=0)
        n1.sort_values(by=['산출보험료'], axis=0, ascending=True, inplace=True)
        n1.sort_values(by=['정산사유'], axis=0, ascending=False, inplace=True)


        # 각각의 데이터 시트에 삽입
        n1.to_excel(standard,sheet_name='요약')
        n2.to_excel(standard,sheet_name='가공(건강)')
        n3.to_excel(standard,sheet_name='가공(연금)')
        n4.to_excel(standard,sheet_name='Raw(건강)')
        n5.to_excel(standard,sheet_name='Raw(연금)')

        # 서식 변경 1단계 - excelwriter 객체 할당
        workbook = standard.book
        worksheet = standard.sheets['요약']

        # 서식 변경 2단계 - 포맷 설정
        format1 = workbook.add_format({
            'num_format':'#,###'
        })

        
        # 서식 변경 3단계 - 포맷 적용
        worksheet.set_column('C:C', 10)
        worksheet.set_column('F:F', 10, format1)
        worksheet.set_column('G:G', 10, format1)
        worksheet.set_column('I:I', 10, format1)
        worksheet.set_column('K:K', 10, format1)
        worksheet.set_column('L:L', 10, format1)
        worksheet.set_column('M:M', 10, format1)
        worksheet.set_column('N:N', 10, format1)
        worksheet.set_column('O:O', 10, format1)

        standard.save()

        # standard.close()

def NHIS_transFileName(yyyymm, baseString):
    path = os.path.dirname(getValue('path'))
    companyNumDict = targetDataDict()
    companyNumList = targetData()
    
    for i in range(len(companyNumList)):

        if i == 0:
            beforeName = os.path.join(path, f'{baseString}.xls')

        else:
            beforeName = os.path.join(path, f'{baseString} ({i}).xls')

        afterName = os. path.join(path, f'{yyyymm} {targetDataDict()[companyNumList[i]]} 건강.xls')
        if os.path.exists(beforeName):
            os.rename(beforeName, afterName)
        
        print(f'{beforeName}파일을 {afterName}으로 변경했습니다.')




speed = 1
certifiedIndexNum = 2             # 사무실 2    # 집 4
this = 202206



## 1 ## (공통) company.xls : 홈페이지에서 준비된 명단은 company.xls로 변경하여 바탕화면에 둘 것
## 2 ## (공통) custominfo에서 사무실/집/노트북 별 바탕화면의 경로 재지정 할 것

#############건강보험 다운로드##################################
        # (20210922) Chrome 다운로드안되는 문제 발생 >> Edge로 변경 >> 정상작동
        ## 상세 ## NHIS_transFileName : 건강보험 Default로 저장된 파일이름 변경을 위해, Default Files은 Company.xls가 위치한 바탕화면에 둘것
        # 20211020) Edge에서도 다운로드 문제 발생함
           # >> 해결방법 : 1. 설정 -> 다운로드 -> 다운로드 폴더 -> 바탕화명으로 변경
           # >> 해결방법 : 2. 홈페이지 주소 자물쇠 클릭 -> 권한 클릭 -> 안전하지 않은 컨텐츠 허용으로 변경

# NHIS_download(this, speed, certifiedIndexNum)
        # NHIS_transFileName(this, '보험료_고지(산출)_내역서_20210923')  #20211020 기준 사용안함. # 건강보험 다른이름 저장이 막혀서 Default File Name으로 저장되어 파일이름 변경하는 프로그램


#############국민연금 다운로드##################################
# NPS_download(this, speed)



#############파일이름 변경##################################
    ## 상세 ## 바탕화면에 있는 파일들의 이름을 변경함
    ## 20211020부터 미사용... 다운로드 자체에서 파일이름 변경까지 진행예정
# transFileName(this)


#############파일 통합##################################
    ## 상세 ## 기초자료는 바탕화면에 있어야 하고, (종합)파일은 현재 작업폴더로 저장됨
# integrating(this)
