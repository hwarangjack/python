file=open('C:/Users/user/Desktop/Naver 동기화/NaverCloud/화랑/○ 자기개발/1. 파이썬/새파일.txt','a')
for i in range(1,5):
    data='%d번쨰 줄을 추가했습니다\n'%i
    file.write(data)
file.close()