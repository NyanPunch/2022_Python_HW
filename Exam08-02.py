#문자열에서 문자의 발생 빈도 세기
import operator

inStr = '가는말이 고와야 오는말이 곱다.'
countDic = {}
countlist = []

if __name__ == '__main__' :
    
    for word in inStr :
        if word>= 'ㄱ' and word <= '힣' : #한글 범위 처음부터 마지막까지
            if word in countDic :
                countDic[word] += 1 #저장된 문자 경우 추가 카운트
            else :
                countDic[word] = 1 #처음 등록된 문자
    #2019038054 김경민
    countlist = sorted(countDic.items(), key=operator.itemgetter(1), reverse=True)
                            #값을 기준으로 정렬해서 countlist 저장
    print("원문")
    print(inStr)
    print('================')
    print("문자          빈도수")
    print('================')
    for i in range(0, len(countlist) ) :
        print(countlist[i][0], '\t', countlist[i][1])
