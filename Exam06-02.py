import turtle
import math
import random

##전역 변수 
t1 ,t2 ,t3 = [None] *3    #거북이 함수 3개 선언
t1X ,t1Y ,t2X ,t2Y ,t3X ,t3Y = [0]*6    #거북이 좌표
swidth, sheight = 500, 500

##메인
if __name__ == "__main__" :
    turtle.title("거북이 만나기")
    turtle.setup(width = swidth +50,height = sheight + 50)
    turtle.screensize(swidth, sheight)

    t1 = turtle.Turtle('turtle')    #거북이 별로 색 및 위치 선정
    t1.color('red')
    t1.penup()
    t1.goto(200,20)

    t2 = turtle.Turtle('turtle')
    t2.color('blue')
    t2.penup()
    t2.goto(-20,-100)

    t3 = turtle.Turtle('turtle')
    t3.color('green')
    t3.penup()
    t3.goto(0,-20)
    #2019038054 김경민 
    while True :
        angle = random.randrange(0,360) #거북이가 움직일 방향과 거리를 랜덤하게 무한 루프
        dist = random.randrange(1,50)
        t1.left(angle)
        t1.forward(dist)
        angle = random.randrange(0,360)
        dist = random.randrange(1,50)
        t2.left(angle)
        t2.forward(dist)
        angle = random.randrange(0,360)
        dist = random.randrange(1,50)
        t3.left(angle)
        t3.forward(dist)

        t1X = t1.xcor(); t1Y = t1.ycor()
        t2X = t2.xcor(); t2Y = t2.ycor()
        t3X = t3.xcor(); t3Y = t3.ycor()
        #거북이들의 거리가 20 미만 일 시 반복문 탈출 및 종료
        if math.sqrt(((t1X - t2X)*(t1X - t2X)) + ((t1Y - t2Y) * (t1Y - t2Y))) <= 20 or \
           math.sqrt(((t1X - t3X)*(t1X - t3X)) + ((t1Y - t3Y) * (t1Y -t3Y))) <= 20 or \
           math.sqrt(((t2X - t3X)*(t2X - t3X)) + ((t2Y - t3Y) * (t2Y - t3Y))) <= 20 :
            t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3)
            break
turtle.done()
