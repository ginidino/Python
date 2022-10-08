# Workshop Week 1

## Task 1
Compute the other columns by creating a program that takes as input x and y and performs the operation. What does each of these operations do?

|Operator|X = 2, Y = 5|X = 5 , Y = 7|X = 8 , Y = 4|
|------|---|---|---|
|X + Y|||
|X * Y|||
|X – Y|||
|X / Y|||
|X // Y|||
|X % Y|||
|X ** Y|||

Code
```py
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

def plus(x, y):
    return x + y

def mult(x, y):
    return x * y

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def quo(x, y):
    return x // y

def mod(x, y):
    return x % y

def pow(x, y):
    return x ** y

print("x + y = %d" % plus(x, y))
print("x * y = %d" % mult(x, y))
print("x - y = %d" % sub(x, y))
print("x / y =", div(x, y))
print("x // y =", quo(x, y))
print("x % y =", mod(x, y))
print("x ** y =", pow(x, y))
```
Output
- x: 2, y: 5
```
Enter the first number: 2
Enter the second number: 5
x + y = 7
x * y = 10
x - y = -3
x / y = 0.4
x // y = 0
x % y = 2
x ** y = 32
```
- x: 5, y: 7
```
Enter the first number: 5
Enter the second number: 7
x + y = 12
x * y = 35
x - y = -2
x / y = 0.7142857142857143
x // y = 0
x % y = 5
x ** y = 78125
```
- x: 8, y: 4
```
Enter the first number: 8
Enter the second number: 4
x + y = 12
x * y = 32
x - y = 4
x / y = 2.0
x // y = 2
x % y = 0
x ** y = 4096
```

## Task2
Write a program to get 2 inputs from user based on the following and print the output for each one of the operation.

|Operator|Input 1|Input 2|
|------|---|---|
|+|5|7|
|*|3|“Python”|
|+|7|“Programming”|
|+|'7'|“Programming”|

Code

1)
```py
input1 = int(input("Input: "))
input2 = int(input("Input: "))

result = input1 + input2
print(result)
```
2)
```py
input1 = int(input("Input: "))
input2 = input("Input: ")

result = input1 * input2
print(result)
```
3)
```py
input1 = int(input("Input: "))
input2 = input("Input: ")

result = input1 + input2
print(result)

#This is error because input1 is int and input2 is string
#+ mark can only be connected between strings
```
4)
```py
input1 = input("Input: ")
input2 = input("Input: ")

result = input1 + input2
print(result)
```
Output

1)
```
Input: 5
Input: 7
12
```
2)
```
Input: 3
Input: Python
PythonPythonPython
```
3)
```
Input: 7
Input: programming
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In [7], line 4
      1 input1 = int(input("Input: "))
      2 input2 = input("Input: ")
----> 4 result = input1 + input2
      5 print(result)

TypeError: unsupported operand type(s) for +: 'int' and 'str'

```
4)
```
Input: 7
Input: programming
7programming
```

## Task3
Write a program that converts the temperature in Fahrenheit to the temperature in Celsius.   
Your program should prompt the user for the temperature and then print the following.   

For example:
Give the temperature in Fahrenheit? 100   
The conversion of 100 degrees Fahrenheit is 37.7777777778 degrees Celsius.  

Code
```py
fahrenheit = int(input('Give the temperature in Fahrenheit? '))
celsius = (fahrenheit - 32.0) * 5/9
print('The conversion of',fahrenheit, 'degrees Fahrenheit is ', celsius, 'degrees Celsius')
```
Output
```
Give the temperature in Fahrenheit? 100
The conversion of 100 degrees Fahrenheit is  37.77777777777778 degrees Celsius
```
## Task4
Write a program that takes an input as string representing a user’s name. Your program should output the length of the name and the number of times each vowel occurs in it.

> Hint: you may use the count() function. It is an inbuilt function in python programming language that returns the number of occurrences of a substring in the given string.

Code
```py
name = input("Enter your name: ")
vowel = 0
a = name.count('a')
e = name.count('e')
i = name.count('i')
o = name.count('o')
u = name.count('u')

vowel = a + e + i + o + u
name_len = len(name)
print("Your name", name,"length is", name_len)
print("There is ", vowel, "in you name" + "\n" + "a :", a, "e :", e, "i :", i, "o :", o, "u :", u)
```
Output
```
Enter your name: injae Lee
Your name injae Lee length is 9
There is  5 in you name
a : 1 e : 3 i : 1 o : 0 u : 0
```
