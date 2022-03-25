import turtle
import random

swidth, sheight = 500, 500
myTurtle, tX, tY, tSize, tColor, tAngle = [None]*6 
Turtles= []

if __name__ == '__main__' :
    turtle.title('거북이 정렬')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    #2019038054 김경민
    for i in range(0, 5) :  #거북이 5마리 생성
        myTurtle = turtle.Turtle('turtle')
        tX = random.randrange(-swidth / 2, swidth / 2)
        tY = random.randrange(-sheight / 2, sheight / 2)      
        r = random.random(); g=random.random(); b= random.random()
        tSize = (random.randrange(1, 100)/10)
        tAngle = random.randrange(0, 360)
        Turtles.append([myTurtle, tX, tY, tSize, r, g, b, tAngle])
        #[거북이, X, Y, 크기, R, G, B, 각도]
    sortedTurtles = sorted(Turtles, key=lambda turtles : turtles[3])

    for index, tList in enumerate(sortedTurtles[0: ]) :
        myTurtle = tList[0] 
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.penup()
        myTurtle.left(tList[7])
        if index == 0 :
            myTurtle.goto(tList[1], tList[2])
            continue
        myTurtle.goto(sortedTurtles[index-1][1], sortedTurtles[index-1][2])

        myTurtle.pendown()
        myTurtle.goto(tList[1], tList[2])
        
    turtle.done()
