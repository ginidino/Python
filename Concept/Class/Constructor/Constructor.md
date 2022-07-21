# Constructor
## Meaning of Constructor
A constructor is a method that is called unconditionally when an instance is created.
```py
myCar1 = Car()
myCar1.color = "red"
myCar1.speed = 0
```
After the instance was created in line 1, it was initialized separately in lines 2 and 3, but field values can be initialized at the same time as the instance is created in line 1 itself.
This function is called a constructor

## Basics of Constructor
The constructor is named _ _init_ _()

        class nameOfClass:
            def __init__(self):
                // Enter the code to initialize in this part

```py
class Car:
    color = ""
    speed = 0

    def __init__(self):
        self.color = "red"
        self.speed = 0
```
- Now, only one row from row 1 to row 3 is needed. That is, when an instance is created, the constructor is automatically called.
```py
myCar1 = Car()
myCar1.color = "red"
myCar1.speed = 0
```
↓
```py
myCar1 = Car()
```
## Default Constructor - Constructor with only self parameter
```py
class Car:
    color = ""
    speed = 0

    def __init__(self):
        self.color = "red"
        self.speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

myCar1 = Car()
myCar2 = Car()

print('The color of car1 is %s and its current speed is %dkm.' % (myCar1.color, myCar1.speed))
print()

print('The color of car2 is %s and its current speed is %dkm.' % (myCar2.color, myCar2.speed))
```
```
The color of car1 is red and its current speed is 0km.

The color of car2 is red and its current speed is 0km.
```

## Constructor with Parameters
- Modify the above code to try using a generator with parameters
- Try passing an initial value as a parameter when creating an instance
- At this time, there is a disadvantage that the initial value is fixed.
- Is it not possible to set the initial value as desired when creating an instance?
```py
class Car:
    color = ""
    speed = 0

    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

myCar1 = Car("red", 30)
myCar2 = Car("blue", 60)

print('The color of car1 is %s and its current speed is %dkm.' % (myCar1.color, myCar1.speed))
print()

print('The color of car2 is %s and its current speed is %dkm.' % (myCar2.color, myCar2.speed))
```
```
The color of car1 is red and its current speed is 30km.

The color of car2 is blue and its current speed is 60km.
```
## Object-oriented basic program completion
```py
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

print('Current speed of %s is %dkm.' % (car1.getName(), car1.getSpeed()))
print('Current speed of %s is %dkm' % (car2.getName(), car2.getSpeed()))
```
```
Current speed of Audi is 30km
Current speed of Mercedes is 60km
```
- line 11, line 15: Create the getName( ) and getSpeed( ) methods and return the car's name and current speed
- line 21, line 22: Get the value using the getName( ) and getSpeed( ) methods without using the name or speed fields
