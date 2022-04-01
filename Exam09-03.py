#10진수를 2/8/16진수로 변환

def base2(n) : 
    if n//2 ==0 : #2로 나눈 몫이 0일 때
        return str(n%2)  #나머지값 반환
    return base2(n//2)+str(n%2) #나눈 몫과 나머지값 재귀호출

def base8(n) :  
    if n//8 ==0 :
        return str(n%8)
    return base8(n//8)+str(n%8)

def base16(n) :
    if n//16 ==0 :
        return str(n%16)
    return base16(n//16)+str(n%16)

#전역변수
bina, octa, hexa = 0, 0, 0 #2진수,8진수,16진수 변수

#메인함수
if __name__ == '__main__' :
    #2019038054 김경민
    n = int(input("10진수 입력 >> "))
    bina = base2(n)
    octa = base8(n)
    hexa = base16(n)
    print('2진수 : ',bina)
    print('8진수 : ',octa)
    print('16진수 : ',hexa)
