import pandas as pd
import os
import re


file_list = os.listdir('.')
target_list = []

target_str='2020년.*[.]x+'
compiled=re.compile(target_str)


for i in file_list:
    if os.path.isfile(i) and compiled.match(i):
        j=os.path.join(os.getcwd(),i)
        target_list.append(j)


standard = pd.DataFrame([])

for i in target_list:
    for k in list(map(str,range(202001,202012))):
        try:
            df_ = pd.read_excel(i, sheet_name=k)
            df_name=df_.iloc[11,0]
            df_month=df_.iloc[9,9]
            df = pd.read_excel(i, sheet_name=k, skiprows=16)
            df.insert(0,'사업장명',df_name)
            df.insert(1,'임금대장',df_month)
            df.set_index('구분', inplace=True)
            df.dropna(how='all',subset=['주민등록번호','성명'], inplace=True)
            standard = standard.append(df)
            print(standard)
        except:
            print('실패')
            pass



standard.sort_values(by='주민등록번호',ascending=True, inplace=True)
standard.to_excel('practice.xlsx')

