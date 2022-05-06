class Car :
    color = ""
    speed = 0

    def upSpeed(self, value) :
        self.speed += value
        if (self.speed >=150) :
            self.speed = 150
            
    def downSpeed(self, value) :
        self.speed -= value

myCar1 = Car()
myCar1.color = "red"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "blue"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "yellow"
myCar3.speed = 0

myCar1.upSpeed(30)
print(myCar1.color, myCar1.speed)

myCar2.upSpeed(200)
print(myCar2.color, myCar2.speed)

myCar3.upSpeed(149)
print(myCar3.color, myCar3.speed)
