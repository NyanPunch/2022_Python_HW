#거북이로 나선그리며 글쓰기 
import turtle
import random
from  tkinter.simpledialog import *
import math

inStr = ''
swidth, sheight = 500, 500
tX, tY, txtSize = [0] * 3
radian, radius, angle = 0, 200, 0 #라디안, 반지름, 각도

turtle.title('거북이로 글쓰며 나선형 그리기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()
#2019038054 김경민
inStr = askstring('insert string', 'writing for turtle')
angle = 360*2 / len(inStr) #문자열 개수로 각도 설정

for ch in inStr :
    radian = 3.14*angle/180 #라디안 구하기
    
    tX = radius*math.cos(radian) #좌표 설정
    tY = radius*math.sin(radian)
    r = random.random(); g = random.random(); b = random.random()
    txtSize = 20 #글자크기 20 고정

    turtle.goto(tX, tY)
    turtle.pencolor((r,g,b))
    turtle.write(ch, font=('맑은고딕',txtSize, 'bold'))

    angle += 360 / len(inStr) #각도만큼 회전
    radius -= len(ch) #반지름을 글자마다 줄여가며 나선형을 만든다

turtle.done()
