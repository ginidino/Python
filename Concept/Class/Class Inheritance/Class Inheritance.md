# Class Inheritance

## Concept of inheritance
- Creating a new class that inherits the fields and methods of the existing class.

      class Sedan:
          field - color, speed, number of seats
          method - UpSpeed(), downSpeed(), numberOfSeats()

      class Truck:
          field - color, speed, capacity
          method - UpSpeed(), downSpeed(), Capacity()

- There are many things that the existing two classes have in common. In other words, it will be efficient if the common characteristics are made into a class called ‘car’, and sedan and trucks inherit the class characteristics and add only necessary fields and methods to each.

      class Car: (Common Content)
          field - color, speed
          method - UpSpeed(), downSpeed()

                      inheritance
                          ↓

      class Sedan: inherit Car
          field - Car field, number of seats
          method - Car method, numberOfSeats()

      class Truck: inherit Car
          field - Car field, capacity
          method - Car method, Capacity()

- The superclass car class is called 'superclass' or 'parent class', and the subclass sedan and truck class is called 'subclass' or 'child class'

      class subclass(superclass):
          // Enter subclass content

## Completion of object-oriented application program
After creating car class, sedan class and truck class inherit from car class
```py
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
```
```
The speed of the sedan is 100km and the number of seats is 5.
The speed of the truck is 80km and the gross weight is 50t.
```

## method Overriding
- Overriding a method in a parent class in a subclass.
- Trucks have no speed limit, but it is assumed that sedans should be limited to a maximum speed of 150 km/h for safety reasons.
    - Subclasses (sedans, trucks) that inherited from superclass (car) inherited the upSpeed() method, but In the case of a sedan, the contents of upSpeed( ) of a car need to be different because the speed limit is required, so upSpeed( ) is re-created and used in the sedan class.

          class Car: (Common Content)
              method - upSpeed()

                  inheritance
                       ↓

          class Sedan(Car):
              method - overriding upSpeed()

          class Truck(Car):


```py
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
```
```
Sedan --> Current speed: 150
Truck --> Current speed: 200
```
