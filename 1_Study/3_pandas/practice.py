import pandas as pd


#공통데이터에서 자료 추출하기
abs_path=r'D:\\NaverCloud\\화랑\\매출(자문).xlsm'
read_df1=pd.read_excel(abs_path, sheet_name='2020 New', skiprows=6)
df=pd.DataFrame(read_df1)
read_df2=df.iloc[:,[0,1,3,4]]                                      # 1차 가공) 일부 데이터만 사용하기
df2=pd.DataFrame(read_df2)                                                  # 가공데이터 DF로 배정하기 (자동완선기능 사용)
df2.set_index('구분', inplace=True)
df2.dropna(thresh=2, inplace=True)
df2.계약유지.fillna('대상사업장',inplace=True)
final_df=df2[df2.계약유지=='대상사업장']
final_df.사업장관리번호 = final_df.사업장관리번호.apply(lambda x: int(x))       # 4차 가공) 사업자관리번호의 데이터를 int로 변환
print(final_df)