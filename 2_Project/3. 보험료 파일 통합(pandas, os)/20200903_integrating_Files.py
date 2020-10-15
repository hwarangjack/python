import os
import pandas as pd

yyyymm=input('yyyymm을 입력하시오 : ')


def id(value):
    return value.성명[0]+value.주민등록번호[0:6]


# 현재 폴더이 있는 Raw 보험료 파일을 리스트화하여 엑셀파일 생성      ??? 리스트형식의 데이터가 만들어졌는데, -> 이를 엑셀파일로 만든다음 -> 엑셀파일을 다시 리스트로 가져올 이유가 있나??? 

path='./'
file_list=os.listdir(path)
list=[]

for i in file_list:
    try:
        item=i.split()
        name=item[item.index(yyyymm)+1]
        if name not in list:
            list.append(name)

        else:
            pass

    except:
        pass

df=pd.DataFrame(list)
df.columns=['사업장명']
df.to_excel('폴더내_파일_List.xlsx')

lists=pd.read_excel('폴더내_파일_List.xlsx',sheet_name=0)
lists2=lists.사업장명



# 건강보험료와 연금보험료 파일을 하나로 연결

for name in lists2:
    try:
        #표준파일 생성
        standard_name=yyyymm+' '+name
        standard=pd.ExcelWriter(standard_name+'(PY).xlsx', engine='openpyxl')

        #건강보험 작업
        filename=standard_name+' 건강.xls'
        if os.path.isfile(path+filename):
            n4=pd.read_excel(filename, sheet_name=0)
            n2=n4
            n2['id']=n2.apply(id, axis=1)
            n2=n2.set_index('id')
            n2=n2.reindex(columns=['성명','주민등록번호','취득일','상실일','보수월액','산출보험료','요양산출보험료','정산사유','정산금액','요양정산사유코드','요양정산보험료','시작월','종료월','요양시작월','요양종료월'])
        else:
            n2=pd.DataFrame(range(0,2))
            n4=n2
            print('----> '+name+'의 건강보험 파일이 존재하지 않습니다.')

        #연금보험 작업
        filename1=standard_name+' 연금.xls'
        if os.path.isfile(path+filename1):
            n5=pd.read_excel(filename1, sheet_name=0)
            n3=n5        
            n3['id']=n3.apply(id, axis=1)
            n3=n3.set_index('id')
            n3=n3.reindex(columns=['성명','주민등록번호','취득일','상실일','당월분_기준소득월액','당월분_(본인기여금)','소급분_해당기간','소급분_(본인기여금)','자격변동 신고사항_(본인기여금)','취득월   납부여부'])
        else:
            n3=pd.DataFrame(range(0,2))
            n5=n3
            print('----> '+name+'의 연금보험 파일이 존재하지 않습니다.')


        #건강과 연금파일 합치기 // 2개 파일의 index  기준으로 합치려면, left_index=true, right_index=true 형식으로 작성
        n1=pd.merge(n2,n3, left_index=True, right_index=True, how='outer')
        n1=n1.reindex(columns=['성명_x','주민등록번호_x','취득일_x','상실일_x','산출보험료','요양산출보험료','정산사유','정산금액','요양정산사유코드','요양정산보험료','당월분_(본인기여금)','자격변동 신고사항_(본인기여금)'])

        # 각각의 데이터 시트에 삽입
        n1.to_excel(standard,sheet_name='요약')
        n2.to_excel(standard,sheet_name='가공(건강)')
        n3.to_excel(standard,sheet_name='가공(연금)')
        n4.to_excel(standard,sheet_name='Raw(건강)')
        n5.to_excel(standard,sheet_name='Raw(연금)')

        standard.save()
        
    except:
        print('통합파일 생성에 실패했습니다')


