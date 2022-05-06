class Car :
    color = ""
    speed = 0

    def upSpeed(self, value) :
        self.speed += value

        print("현재 속도(수퍼클래스) : %d" % self.speed)

class Sedan(Car) :
    def upSpeed(self, value) :
        self.speed += value
        if (self.speed >=150) :
            self.speed = 150

        print("현재 속도(서브클래스) : %d" % self.speed)

class Sonata(Sedan) :
    pass

class Truck(Car) :
    pass
            
sedan1, truck1, sonata1 = None, None, None

truck1 = Truck()
sedan1 = Sedan()
sonata1 = Sonata()

truck1.upSpeed(200)
sedan1.upSpeed(200)
sonata1.upSpeed(200)
