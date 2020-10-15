import pandas as pd


#공통데이터에서 자료 추출하기
abs_path=r'D:\\NaverCloud\\화랑\\매출(자문).xlsm'
read_df1=pd.read_excel(abs_path, sheet_name='2020 New', skiprows=6)
df=pd.DataFrame(read_df1)
read_df2=df.iloc[:,[0,1,3,4]]                                      # 1차 가공) 일부 데이터만 사용하기
df2=pd.DataFrame(read_df2)                                                  # 가공데이터 DF로 배정하기 (자동완선기능 사용)
df2.계약유지=df2.계약유지.fillna('대상사업장')                       # 2차 가공) 계약유지 열에서 누락값은 대상사업장으로 전환
df2 = pd.DataFrame(df2.dropna())                                   # 3차 가공) 사업장명, 사업자관리번호도 없는 누락값(잔여값)은 삭제
df2.사업장관리번호 = df2.사업장관리번호.apply(lambda x: int(x))       # 4차 가공) 사업자관리번호의 데이터를 int로 변환
print(df2)
final_df=df2[df2['계약유지']!='해지']                               # 5차 가공) 특정 열 기준으로 필터기능 사용(해지사업장 제외)
print(final_df)