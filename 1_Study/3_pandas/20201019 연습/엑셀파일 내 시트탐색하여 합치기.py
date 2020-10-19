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

standard_df=pd.DataFrame({
    '예시':[1,2,3],
    '예시1':[1,2,3],
    '예시2':[1,2,3]
})

for i in target_list[0:3]:
    for j in range(1,9):
        df=pd.read_excel(i, sheet_name=f'20200{j}', skiprows=16)
        pd.DataFrame(df)
        df.dropna(thresh=40, inplace=True)
        standard_df=standard_df.append(df)
        standard_df=standard_df[standard_df['주민등록번호']!='NaN']
        standard_df.주민등록번호=standard_df.dropna()

standard_df.drop(['예시','예시1','예시2'],axis=1, inplace=True)   
print(standard_df.shape)
            
