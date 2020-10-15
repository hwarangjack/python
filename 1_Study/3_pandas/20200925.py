import pandas as pd

df=pd.read_excel('./exmple.xlsx', sheet_name=0)


print(df.iloc[list(filter(lambda x: x%3==0, range(df.shape[0]))),:])
print(df.iloc[range(1,df.shape[0],3),:])

# print(range(100))
# print(range(0,100))
# print(range(0,100,3))