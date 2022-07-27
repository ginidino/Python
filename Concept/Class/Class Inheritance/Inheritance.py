class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value


class Sedan(Car):
    numberOfSeats = 0

    def getSeatNum(self):
        return self.numberOfSeats

class Truck(Car):
    capacity = 0

    def getCapacity(self):
        return self.capacity

sedan1 = Sedan()
truck1 = Truck()

sedan1.upSpeed(100)
truck1.upSpeed(80)

sedan1.numberOfSeats = 5
truck1.capacity = 50

print('The speed of the sedan is %dkm and the number of seats is %d.' % (sedan1.speed, sedan1.numberOfSeats))
print('The speed of the truck is %dkm and the gross weight is %dt.' % (truck1.speed, truck1.capacity))
print()

class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed += value

        print('Current speed: %d' % self.speed)

class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value

        if self.speed > 150:
            self.speed = 150

        print('Current speed: %d' % self.speed)

class Truck(Car):
    pass

sedan2 = Sedan()
truck2 = Truck()

print('Sedan --> ', end="")
sedan2.upSpeed(200)

print('Truck --> ', end="")
truck2.upSpeed(200)
print()

# combine the above two
class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed += value

        print('Current speed: %d' % self.speed)

    def downSpeed(self, value):
        self.speed -= value

        print('Current speed: %d' % self.speed)


class Sedan(Car):
    numberOfSeats = 0

    def getSeatNum(self):
        return self.numberOfSeats

    def upSpeed(self, value):
        self.speed += value

        if self.speed > 150:
            self.speed = 150

        print('Current speed: %d' % self.speed)

class Truck(Car):
    capacity = 0

    def getCapacity(self):
        return self.capacity

sedan = Sedan()
truck = Truck()

print('Sedan --> ', end="")
sedan.upSpeed(200)

print('Truck --> ', end="")
truck.upSpeed(200)

sedan.numberOfSeats = 5
truck.capacity = 50

print('The speed of the sedan is %dkm and the number of seats is %d.' % (sedan.speed, sedan.numberOfSeats))
print('The speed of the truck is %dkm and the gross weight is %dt.' % (truck.speed, truck.capacity))