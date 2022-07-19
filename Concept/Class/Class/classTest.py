class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
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
print('The color of car1 is %s and its current speed is %dkm.' % (myCar1.color, myCar1.speed))
print()

myCar2.upSpeed(60)
print('The color of car2 is %s and its current speed is %dkm.' % (myCar2.color, myCar2.speed))
print()

myCar3.upSpeed(0)
print('The color of car3 is %s and its current speed is %dkm.' % (myCar3.color, myCar3.speed))