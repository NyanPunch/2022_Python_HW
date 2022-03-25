#변수 선언
heartnum = 0
numstr, ch, heartstr = "", "", "" #숫자입력받을 문자열, 숫자저장변수, 하트출력문자열

#메인 함수
if __name__ == "__main__" :
    numstr = input("숫자를 여러개 입력하세요: ")   #숫자를 문자열로 하나씩 받는다
    print("")
    i=0
    ch = numstr[i]  #첫 번째로 입력받은 숫자를 ch에 저장
    while True :    #마지막 열 까지 무한 반복
        heartnum = int(ch)
        #2019038054 김경민
        heartstr = ""
        for k in range(0,heartnum) :
            heartstr += "\u2665"    
            k+=1

        print(heartstr)

        i += 1    #다음 문자열을 출력하기 위해 증가
        if (i > len(numstr) -1) : #i가 입력받은 문자열보다 크면 반복문 종료
            break
        ch = numstr[i] #바뀐 i번째 문자열을 ch에 저장
