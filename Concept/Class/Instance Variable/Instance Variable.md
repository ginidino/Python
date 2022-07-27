# Difference Between Instance Variable and Class Variable

## Instance Variable
- Instance variables can only be used when an instance is created -> In other words, color and speed variables are not allocated to real memory before creation.

      class Car:
        color = "" # field: instance variable
        speed = 0  # field: instance variable
      
- Creating an instance in the main code part using a class -> Since the instance is created, color and speed variables are allocated in memory

      myCar1 = Car()
      myCar2 = Car()

- When an instance is created, it allocates a separate memory for the instance variable -> `myCar1.color` and `myCar2.color` are different

## Class Variable
- Variables with space allocated within the class
- Therefore, even if an instance is created, it is added separately
- Without allocating memory, the class's own memory is shared between instances
- When accessing a class variable, the space already created in the class can be shared by accessing it in the `class name.class variable name` or `instance.class variable name` method.
```py
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
```
```
Car1's current speed is 30km, and the number of cars produced is 1.
Car2's current speed is 60km, and the number of cars produced is 2.
```
- Line 4: Declare the class variable `count` and initialize it to 0
- Lines 6~8: In order to access the class variable in the constructor, `classname.count` is incremented by 1. That is, when the constructor works, when creating instances in lines 10 and 14, the total number of cars produced is increased by 1.
- **_Both `Car.count` and `myCar2.count` can be used to use class variables in the main code part_**. i.e. both access the class variable
