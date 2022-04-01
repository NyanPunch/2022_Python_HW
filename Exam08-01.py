#대소문자 상호 변환하기
inStr, outStr = "", ""  #문자열 저장 변수
word = ""   #한 글자 저장 변수
count, i = 0, 0

inStr = input("문자열을 입력하세요 : ")
count = len(inStr)  #문자열 길이 저장
#2019038054 김경민

for i in range(0, count) : #문자열 길이 만큼 반복
    word = inStr[i] #i번째 문자 대소문자 구분 후 변경
    if (ord(word) >= ord('A') and ord(word) <= ord('Z')) :
        ch = word.lower()
    elif (ord(word) >= ord('a') and ord(word) <= ord('z')) :
        ch = word.upper()
    else : #영어가 아닐 때
        ch = word 

    outStr += ch

print("대소문자 변환 결과 >> %s" % outStr)
