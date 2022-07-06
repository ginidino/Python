coffee = int(input('What kind of coffee would you like? (1. Regular, 2. Sugar, 3. Black): '))
print()

print('1. hot water preparation')
print('2. paper cup ready')

if coffee == 1:
    print('3. make regular coffee')
elif coffee == 2:
    print('3. make sugar coffee')
elif coffee == 3:
    print('3. make black coffee')
else:
    print('3. make anything')

print('4. Pour water')
print('5. Stir with a spoon to dissolve')
print()
print('coffee ready')
print()

def coffee_machine(coffee):
    print()
    print('1. hot water preparation')
    print('2. paper cup ready')

    if coffee == 1:
        print('3. make regular coffee')
    elif coffee == 2:
        print('3. make sugar coffee')
    elif coffee == 3:
        print('3. make black coffee')
    else:
        print('3. make anything')
    print('4. Pour water')
    print('5. Stir with a spoon to dissolve')
    print()

coffee = int(input('A: What kind of coffee would you like? (1. Regular, 2. Sugar, 3. Black): '))
coffee_machine(coffee)
print('A: coffee ready')
print()

coffee = int(input('B: What kind of coffee would you like? (1. Regular, 2. Sugar, 3. Black): '))
coffee_machine(coffee)
print('B: coffee ready')

# Create a function plus() that takes two integers as input and returns the sum of two integers
print('sum of two integers')
def plus(num1, num2):
    result = num1 + num2
    return result

sum = 0
sum = plus(100, 200)
print('The pulse() function result of 100 and 200 is', sum)

# Calculator function that adds, subtracts, multiplies, and divides two entered numbers
print('Calculator function that adds, subtracts, multiplies, and divides two entered numbers')
def calculate(num1, num2, mark):
    result = 0
    if mark == '+':
        result = num1 + num2
    elif mark == '-':
        result = num1 - num2
    elif mark == '*':
        result = num1 * num2
    elif mark == '/':
        result = num1 / num2

    return result

mark = input('calculation input(+, -, *, /); ')
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

result = calculate(num1, num2, mark)

print('calculator: %d %s %d = %d' % (num1, mark, num2, result))
print()

def func1():
    a = 10
    print('value of a in func1() : %d' % a)

def func2():
    print('value of a in func1() : %d' % a)

a = 20   # a is global variable
func1()
func2()
print()

def function1():
    result = 100
    return result

def function2():
    print('Executing a function with no return value')

sum = 0
sum = function1()
print('The value returned by function1(): %d' % sum)
function2()
print()

# How to set the number of parameters
print('How to set the number of parameters')
def para2_func(num1, num2):
    result = num1 + num2
    return  result

def para3_func(num1, num2, num3):
    result = num1 + num2 + num3
    return result

sum = 0
sum = para2_func(10, 20)
print('Result of function call with 2 parameters: %d' % sum)

sum = para3_func(10, 20, 30)
print('Result of function call with 2 parameters: %d' % sum)
print()

# How to set default values for parameters
print('How to set default values for parameters')
def para_func(num1, num2, num3 = 0):
    result = num1 + num2 + num3
    return result

sum = 0
sum = para_func(10, 20)
print('Result of function call with 2 parameters: %d' % sum)

sum = para_func(10, 20, 30)
print('Result of function call with 2 parameters: %d' % sum)
print()

# A method of not specifying the number of parameters - Arbitrary Argument List method
print('Arbitrary Argument List method')
def para_function(*para):
    result = 0
    for num in para:
        result += num

    return result

sum = 0
sum = para_function(10, 20)
print('Result of function call with 2 parameters: %d' % sum)

sum = para_function(10, 20, 30)
print('Result of function call with 2 parameters: %d' % sum)
print()

#dictionary format
print('dictionary format')
def dic_func(**para):
    for i in para.keys():
        print('%s --> %d people' % (i, para[i]))

dic_func(bigbang = 4, blackpink = 4, IDLE = 5, WJSN = 10)
print()

# lottery number draw program
import random

print('lottery number draw program')

def getNum():
    return random.randrange(1, 46)

lotto = []

print('**** Lotto draw begins **** \n')

while True:
    num = getNum()

    if lotto.count(num) == 0:
        lotto.append(num)

    if len(lotto) >= 6:
        break

print('lottery numbers drawn: ', end=' ')
lotto.sort()
for i in range(0, 6):
    print("%d " % lotto[i], end='')
