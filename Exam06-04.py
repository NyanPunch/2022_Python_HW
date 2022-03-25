import turtle

tX,tY=[0]*2
swidth, sheight = 800, 450
    #2019038054 김경민
if __name__ == '__main__' :
    turtle.title('거북 구구단')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth,sheight)
    turtle.penup()
    tX, tY = -500, 250
    turtle.goto(tX,tY)
    #가로 출력 반복문
    for i in range(1,10) :  #1부터 9까지 곱에 해당되는 변수
        for k in range(2,10) :  #2부터 9까지 단에 해당되는 변수
            turtle.goto(tX + 80 * k, tY - 40 * i)
            dan = str(k) + ' x ' + str(i) + ' = ' + str(k*i)
            turtle.write(dan,font = ('Arial',12,'bold'))
    turtle.done()
