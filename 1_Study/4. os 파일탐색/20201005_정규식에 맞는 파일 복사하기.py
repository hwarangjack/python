import os
import pandas as pd
import shutil
import re

path=input(r'파일을 가져올 폴더의 절대경로를 지정하세요.(Python의 경우 \\을 기재하는 것에 유의) : ')
how=input('정규식을 사용하여 조건을 설정하세요 :')

empty_list=[]

def checkfile(path, target):

    cp=re.compile(target)

    for i in os.listdir(path):
        abs_path = os.path.join(path,i)
        if os.path.isfile(abs_path):
            if cp.match(i):
                empty_list.append([path,abs_path,i])
        
        elif os.path.isdir(abs_path):
            checkfile(abs_path, target)


checkfile(path,how)
# checkfile('D:\\NaverCloud\\화랑\\☆ 자문\\(99일) 홍정양행 ■ 폐업','2020년\s\d+.*임금대장.*[^세무].[.]x+')
# checkfile('D:\\NaverCloud\\화랑\\☆ 자문','2020년\s*임금대장\s*.+[.]x+')

for i in empty_list:
    shutil.copy(i[1],os.path.join(os.getcwd(),i[2]))

