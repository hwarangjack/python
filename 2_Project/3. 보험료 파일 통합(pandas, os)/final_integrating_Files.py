import os
import pandas as pd
import re

yyyymm=input('yyyymm을 입력하시오 : ')

def id(value):
    return value.성명[0]+value.주민등록번호[0:6]


path = '.'
surfix = ' (종합).xlsx'
cp1 = re.compile('.+[.]x+')
cp2 = re.compile(surfix)
object_list=[] 
for i in os.listdir(path):
    if i.startswith(yyyymm) and cp1.match(i):
        j = os.path.splitext(i)[0]
        k=j[7:len(j)-3]

        if k not in object_list:
            object_list.append(k)



# 건강보험료와 연금보험료 파일을 하나로 연결
for name in object_list:
    try:
        #표준파일 생성
        standard_name=yyyymm+' '+name
        standard=pd.ExcelWriter(standard_name+surfix, engine='xlsxwriter')
        
        #건강보험 작업
        filename=standard_name+' 건강.xls'
        if os.path.isfile(filename):
            n4=pd.read_excel(filename, sheet_name=0)
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
        if os.path.isfile(filename1):
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
        standard.close()


    except:
        print('통합파일 생성에 실패했습니다')


