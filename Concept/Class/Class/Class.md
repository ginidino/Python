# Class
Class Concepts
- Python is a programming language to which object-oriented concepts can be applied.
- Appearance and creation of class

        class name of class:
            # Implement the relevant code in this part

example
- The properties of a car are called fields. Car functions are implemented in the form of functions. A function implemented in a class is called a method.

      class car:
        attribute (field)
        # field of cars
        colour = ""
        currentSpeed = 0
        
        function (method)
        # method of cars
        def upSpeed(increase_speed amount) :
          # code to speed up by an increment_rate from the current speed
        
        def downSpeed(Decrease_Speed amount)
          # code that slows down by an increase_rate from the current speed

```py
class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value
```
- Change the name of the field and the parameter of the method to the English variable name, and the method completes the source with the contents of changing the speed of the car.
- self refers to the class itself, self.speed in line 6 means speed in line 3. That is, it is interpreted as a speed variable in its own class.

## Creating an instance
```
# Car Blueprint (Class)
class Car:
    # car properties
      car color
      car speed
    # car function
      speed_up()
      speed_down()

# Car(instance)
car1 = Car()
car2 = Car()
car3 = Car()
```
- Implementing three car instance creation in code
```
myCar1 = Car()
myCar2 = Car()
myCar3 = Car()
```

- The three instances each have the `color` and `speed` fields of the car.

## substitute a value for a field
- Each instance has a separate field, each of which can be substituted with a separate value
```py
myCar1.color = "red"
myCar1.speed = 0
myCar2.color = "blue"
myCar2.speed = 0
myCar3.color = "yellow"
myCar3.speed = 0
```

## Calling Method
- In the Car class, there are two methods: upSpeed() and downSpeed()
```py
myCar1.upSpeed(30)
myCar2.upSpeed(60)
```

## Fully working coding of Class
```py
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
```
```
The color of car1 is red and its current speed is 30km.

The color of car2 is blue and its current speed is 60km.

The color of car3 is yellow and its current speed is 0km.
```

|step|work|form|example|
|---|---|---|---|
|step 1|class creation|class name of class:|class Car:|
|step 2|Creating an instance|instance = name of class()|myCar1 = Car()|
|step 3|Using fields or methods|instance.name of field = value|myCar1.color = "red"|
