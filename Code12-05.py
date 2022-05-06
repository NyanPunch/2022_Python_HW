class Car :
    color = ""
    speed = 0

    def __init__(self, name, speed) :
        self.name = name
        self.speed = speed

    def getName(self) :
        return self.name
            
    def getSpeed(self) :
        return self.speed 

car1, car2 = None, None

car1 = Car('아우디', 0)
car2 = Car('포르쉐', 120)

print("%s 현재 속도 %d." % (car1.getName(), car1.getSpeed()))

print("%s 현재 속도 %d." % (car2.getName(), car2.getSpeed()))
