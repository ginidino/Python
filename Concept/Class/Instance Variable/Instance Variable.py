class Car:
    color = ""  # instance variable
    speed = 0   # instance variable
    count = 0   # class variable

    def __init__(self):
        self.speed = 0
        Car.count += 1  # Note that this is not self.count!!

myCar1 = Car()
myCar1.speed = 30
print("Car1's current speed is %dkm, and the number of cars produced is %d." % (myCar1.speed, Car.count))

myCar2 = Car()
myCar2.speed = 60
print("Car2's current speed is %dkm, and the number of cars produced is %d." % (myCar2.speed, Car.count))