import os
import pandas as pd

yyyymm= input('변경하고자 하는 파일의 yyyymm을 입력하세요 : ')

#공통데이터에서 자료 추출하기
abs_path=r'D:\\NaverCloud\\화랑\\매출(자문).xlsm'
read_df1=pd.read_excel(abs_path, sheet_name='2021', skiprows=6)
df=pd.DataFrame(read_df1)
read_df2=df.iloc[:,[0,1,3,4]]                                      # 1차 가공) 일부 데이터만 사용하기
df2=pd.DataFrame(read_df2)                                                  # 가공데이터 DF로 배정하기 (자동완선기능 사용)
df2.set_index('구분', inplace=True)
df2.dropna(thresh=2, inplace=True)
df2.계약유지.fillna('대상사업장',inplace=True)
final_df=df2[df2.계약유지=='대상사업장']
final_df.사업장관리번호 = final_df.사업장관리번호.apply(lambda x: int(x))       # 4차 가공) 사업자관리번호의 데이터를 int로 변환
final_df.set_index('사업장관리번호',inplace=True)


# Middle Name 수정
for i in os.listdir('.'):
    if i.startswith(yyyymm) and i.endswith('.xls'):
        try:
            j=i.split(' ')
            k=i.replace(j[1],final_df.loc[int(j[1])].loc['사업장명'])
            if k in os.listdir('.'):
                print(k+'의 파일이 이미 존재합니다')
            else:
                os.rename(i,k)
        except:
            print(i+'파일은 변경내용이 없거나, 사업장관리번호가 존재하지 않습니다.')

print('------------------Middle name 변경 완료------------------')
print('------------------Middle name 변경 완료------------------')

# # Last Name 수정
for i in os.listdir('.'):
    if i.startswith(yyyymm) and i.endswith('rjsrkd.xls'):
        try:
            j=i.replace('rjsrkd','건강')
            if j in os.listdir('.'):
                print(j+'의 파일이 이미 존재합니다.')
            else:
                os.rename(i,j)
        except:
            print(i+'파일은 변경내용이 없습니다')

    if i.startswith(yyyymm) and i.endswith('dusrma.xls'):
        try:
            j=i.replace('rjsrkd','연금')
            if j in os.listdir('.'):
                print(j+'의 파일이 이미 존재합니다.')
            else:
                os.rename(i,j)
        except:
            print(i+'파일은 변경내용이 없습니다')
    