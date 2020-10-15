import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



# 수신자 목록을 별도분리(데이터화하여 추후 For 구문 사용)
df=pd.read_excel('Email_list.xlsx', sheet_name=0)
to_list=df.values.tolist()

# 발송제목 및 내용을 별도분리
df1=pd.read_excel('Email_list.xlsx', sheet_name=1)
head=df1.text[0]
contents=df1.text[1]

#메일발송의 기본사항 입력
id=input('이메일을 발송할 네이버 이메일을 입력하세요(yyyyy@naver.com) : ')
pw=input('이메일의 비밀번호를 입력하세요 : ')
name=input('이메일을 수신할 사업장의 명칭을 입력하세요 : ')

success=0
fail=0

# 조건발송 / 반복발송
for i in to_list:
    if i[1] == 1:
        success=success+1
        print(f'\n----------{i[2]}----------')

        # 받는사람, 메일제목, 메일내용 변수정의
        to=i[3]
        From =id
        subject=f'{head} ({i[2]})'

        # 복합객체 신설, 변수할당
        message = MIMEMultipart()

        # message Part 1 ([발송자, 받는자, 주제, 글내용] 삽입)
        message["from"] = From
        message['to']= to
        message['subject']=f'[화랑][{name}] {subject}'
        message.attach(MIMEText(contents))

        # message Part 2 ([첨부파일] 삽입)
        try:
            file_name=f'{subject}.pdf'
            part = MIMEBase('application','octet-stream') #고정값인듯?
            part.set_payload(open(file_name,'rb').read()) #파일을 읽어서 MIMEBase에 업로드하고
            encoders.encode_base64(part) #디코딩해라
            part.add_header('content-disposition','attachment', filename=file_name)  #고정값인듯
            message.attach(part)

        except:
            print(f'    {subject}파일이 존재하지 않아, 메일에 파일첨부가 실패했습니다.')
            pass

        # SMTP 메일발송 기초사항 설정
        # SSL인증방식에서는 포트번호 465를 사용하고, TLS인증방법에서는 587을 사용(하고, starttls()함수 호출 필요)한다
        smtp = smtplib.SMTP('smtp.naver.com',587)
        smtp.ehlo
        smtp.starttls()
        smtp.login(id,pw)
        smtp.sendmail(From, to, message.as_string())

        print(f'>>>{i[2]}님의 {i[3]}주소로 메일이 발송되었습니다.')
        smtp.quit()

    else:
        fail=fail+1
        print(f'\n----------{i[2]}----------')
        print(f'>>> 메일이 거부되었습니다.')

print('')
print('')
print('--------------[결과알림]------------------')
print(f'정상적으로 발송한 총 메일 수는 {success}개 입니다')
print(f'발송을 거부한 총 메일 수는 {fail}개 입니다')