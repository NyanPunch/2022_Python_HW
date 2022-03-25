import random

data= []
i, j = 0, 0

if __name__ == '__main__' :
    for i in range(0,10) :
        tmp = hex(random.randrange(0, 100)) #16진수 랜덤 생성
        data.append(tmp)    #data에 tmp추가
#2019038054 김경민
    print("정렬 전 데이터 : ", end =' ')
    [print(num, end =' ') for num in data]

    for i in range(0, len(data) - 1) :
        for k in range(i+1, len(data)) :
            if int(data[i], 16) > int(data[k], 16) :    #스왑
                tmp = data[i]
                data[i] = data[k]
                data[k] = tmp
    print('')            
    print("정렬 후 데이터 : ", end =' ')
    [print(num, end =' ') for num in data]
