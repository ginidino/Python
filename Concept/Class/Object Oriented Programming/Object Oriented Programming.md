# Object Oriented Programming
- A program design methodology and a kind of concept
- A method of dividing a program into basic units called numerous 'objects' and describing their interactions, rather than simply dividing the program into data and processing methods.
- An object is a group of 'methods and variables (data)' that perform a single role.
- Advantages:
    * Easy to reuse code: You can import and use a class created by others, and extend it through inheritance
    * Easy maintenance: You don't need to find and modify the code one by one, just modify the inside of the class that needs to be modified
    * Suitable for large projects: It can be developed in a modular class unit, so it is easy to share tasks

- Disadvantage:
    * Relatively slow processing speed
    * If there are many objects, the capacity increases.
    * Requires a lot of time and effort for design

## Class and objects
### basic programming
```py
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))
```
```
3
7
3
10
```
> Need to define add functions one by one -> More is more difficult

### object oriented programming
```py
class Calculator:        # class
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()         # cal1 and cal2 -> object
cal2 = Calculator()
# cal1, cal2 is an instance of an object or Calculator()
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
```
```
3
7
3
10
```
> Declare and reuse Calculator class
