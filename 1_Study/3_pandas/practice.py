import pandas as pd
import os
import re



#연습 데이터프레임 불러오기
df=pd.read_excel('D:\\NaverCloud\\화랑\\학습방\\python\\practice.xlsx')
pd.DataFrame(df)
df.sort_values(by=['사업장명', '주민등록번호'], ascending=True, inplace = True)
df.set_index('사업장명', inplace=True)

#데이터 중 분석에 불필요한 행(Row)을 명칭(Label)으로 삭제하기
# df.drop(['119-96-01081'], axis=0, inplace=True)
# print(df.head(20))
# print(df.shape)

#데이터 중 분석에 불필요한 행(Row) 위치(Index)로 삭제하기
# df.drop(df.index[0], axis=0, inplace=True)
# print(df.head(20))
# print(df.shape)

#데이터 중 분석에 불필요한 열(columns)을 명칭(Label)으로 삭제하기
# df.drop(['구분','생년월일'], axis=1, inplace=True)
# print(df)

#데이터 중 분석에 불필요한 열(columns) 위치(Index)로 삭제하기
# df.drop(df.columns[0:6], axis=1, inplace=True)
# print(df)

# df.drop(df.columns[[0,1,2,3,4,5,6]], axis=1, inplace=True)
# print(df)

#데이터 유형 변경 1 (숫자로 변환하기 - df.columns.astype())
# df.주민등록번호 = df.주민등록번호.astype(str)
# print(df.head(15))
# print(df.dtypes)

#데이터 유형 변경 2 (숫자로 변환하기 - pd.to_numeric)
# pd.to_numeric(df.주민등록번호, errors='coerce', downcast=None)
# print(df.head(15))
# print(df.dtypes)

#데이터 유형 변경 3 (문자열 다루기)
# df.주민등록번호 = df.주민등록번호.fillna(0)
# df.주민등록번호 = df.주민등록번호.apply(int)
# df.주민등록번호 = df.주민등록번호.apply(str)
# df.주민등록번호 = df.주민등록번호.apply(lambda x: x[0:6]+'-'+x[6:])
# print(df.head(15))
# print(df.dtypes)
# print(df.info())

#데이터 유형 변경 4 (카테고리로 변환)
# df.임금대장 = df.임금대장.astype('category')
# print(df.head(15))
# print(df.dtypes)
# print(df.info())
