#문자와 숫자가 섞인 데이터 정렬하기
import random

def getnum(strdata) : #문자열 중 숫자만 추출하는 함수
    numStr = ''
    for word in strdata :
        if word.isdigit() : #숫자인 부분만 카운트
            numStr += word

    return int(numStr) #카운트된 숫자만 반환


data= []
i, k = 0, 0


if __name__ == '__main__' :
    for i in range(0,10) :
        tmp = hex(random.randrange(0, 100)) #16진수 랜덤 생성
        data.append(tmp)    #data에 tmp추가
#2019038054 김경민
    print("정렬 전 데이터 : ", end =' ')
    [print(num, end =' ') for num in data]

    for i in range(0, len(data) - 1) :
        for k in range(i+1, len(data)) :
            if getnum(data[i]) > getnum(data[k]) :    #스왑
                tmp = data[i]
                data[i] = data[k]
                data[k] = tmp
    print('')            
    print("정렬 후 데이터 : ", end =' ')
    [print(num, end =' ') for num in data]
