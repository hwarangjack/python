data='''
park 870112-1066912
jang 870208-2012923
'''

result=[]

for line in data.split('\n'):

    word_result=[]

    for name_num in line.split(' '):

        if len(name_num)==14 and name_num[:6].isdigit() and name_num[7:].isdigit():
            name_num = name_num[:6]+"-"+"*******"

        word_result.append(name_num)

    result.append(word_result)

result.pop(0)
result.pop(-1)
print(result)

