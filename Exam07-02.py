import operator

trainTuple = [("토마스",5), ("헨리",8), ("에드웓", 9), ("에밀리", 5), ("토마스",4), ("헨리", 7), ("토마스",3), ("에밀리",8), ("퍼시",5), ("고든", 13)]
trainDic, trainList = {}, []
tTuple = None
topRank, tmpRank = 1, 1 
#2019038054 김경
if __name__ == '__main__' :
    for tTuple in trainTuple :   
        tName = tTuple[0]       #이름
        tWeight = tTuple[1]     #무게
        if tName in trainDic :      #튜플을 딕셔너리로 변경
            trainDic[tName] += tWeight    #기차의 이름이 존재 할 때 무게 누적
        else :
            trainDic[tName] = tWeight      #기차의 이름을 처음 등록 할 때

    print('기차 수송량 목록 >>', trainTuple)
    print('-------------------------------------')
    trainList = sorted(trainDic.items(), key = operator.itemgetter(1), reverse = True)
    #리스트 정렬 무게순
    print('기차\t총 수송량 순위')
    print('-------------------------------------')
    print(trainList[0][0], '\t', trainList[0][1], '\t', tmpRank) #첫 번째 기차
    for i in range(1, len(trainList)) :
        topRank += 1
        if trainList[i][1] == trainList[i-1][1] :  #앞선 기차와 무게가 같을 시
            pass                                        #순위를 올리지 않음
        else :
            tmpRank = topRank
        print(trainList[i][0], '\t', trainList[i][1], '\t', tmpRank)
        
