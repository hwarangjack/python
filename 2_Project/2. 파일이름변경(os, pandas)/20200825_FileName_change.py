import os
import pandas as pd

yyyymm= input('변경하고자 하는 파일의 yyyymm을 입력하세요 : ')

df2=pd.read_excel('list.xlsx')
df2.set_index('사업장관리번호',inplace=True)

# Middle Name 수정
for i in os.listdir('.'):
    if i.startswith(yyyymm) and i.endswith('.xls'):
        try:
            j=i.split(' ')
            k=i.replace(j[1],df2.loc[int(j[1])].loc['사업장명'])
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
    