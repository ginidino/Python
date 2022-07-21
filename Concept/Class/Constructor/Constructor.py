class Car1:
    color = ""
    speed = 0

    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

myCar1 = Car1("red", 30)
myCar2 = Car1("blue", 60)

print('The color of car1 is %s and its current speed is %dkm.' % (myCar1.color, myCar1.speed))
print('The color of car2 is %s and its current speed is %dkm.' % (myCar2.color, myCar2.speed))
print()

class Car2:
    name = ""
    speed = 0

    # Constructor
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    # method
    def getName(self):
        return self.name

    # method
    def getSpeed(self):
        return self.speed

car1 = Car2("Audi", 30)
car2 = Car2("Mercedes", 60)

print('Current speed of %s is %dkm' % (car1.getName(), car1.getSpeed()))
print('Current speed of %s is %dkm' % (car2.getName(), car2.getSpeed()))