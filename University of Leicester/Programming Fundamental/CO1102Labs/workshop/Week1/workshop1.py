# Task1
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
print()

# Task2
input1 = int(input("Input: "))
input2 = int(input("Input: "))

result = input1 + input2
print(result)
print()

input1 = int(input("Input: "))
input2 = input("Input: ")

result = input1 * input2
print(result)
print()

input1 = int(input("Input: "))
input2 = input("Input: ")

result = input1 + input2
print(result)
#This is error because input1 is int and input2 is string
#+ mark can only be connected between strings
print()

input1 = input("Input: ")
input2 = input("Input: ")

result = input1 + input2
print(result)
print()

# Task3
fahrenheit = int(input('Give the temperature in Fahrenheit? '))
celsius = (fahrenheit - 32.0) * 5/9
print('The conversion of',fahrenheit, 'degrees Fahrenheit is ', celsius, 'degrees Celsius')
print()

# Task4
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