#날짜 세기 및 요일 구하기
from time import *
from datetime import *

def countday(d1, d2) : # 날짜 수 세는 함수
    returnday = 0
    
    year, month, day = d1.split('/') # / 을 기점으로 연 월 일 대입
    day1 = date(int(year),int(month),int(day))
    year, month, day = d2.split('/')
    day2 = date(int(year),int(month),int(day))
    diffday=day2-day1 # 두 날짜의 일수 차이 구하기
    returnday = diffday.days
    
    return returnday

def getday(time) : #요일 구하는 함수
    week = ['월','화','수','목','금','토','일']
    return week[time.tm_wday]
#2019038054 김경민
startDate, searchDate, t = '', '', None

if __name__ == '__main__' :
    startDate = input('시작 날짜입력(연/월/일) >> ')
    t = localtime() #현재 날짜를 받는다
    searchDate = str(t.tm_year)+'/'+str(t.tm_mon)+'/'+str(t.tm_mday)

    print(startDate, '부터 오늘(', searchDate, ')까지는 ', countday(startDate, searchDate), '일이 지났습니다')
    print('그리고 오늘은 ', getday(t), '요일 입니다')
