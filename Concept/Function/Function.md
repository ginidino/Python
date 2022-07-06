# Function

## concept of function

Functions are provided by the Python program itself, but users can also create and use them themselves.

```py
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
```
```
What kind of coffee would you like? (1. Regular, 2. Sugar, 3. Black): 2

1. hot water preparation
2. paper cup ready
3. make sugar coffee
4. Pour water
5. Stir with a spoon to dissolve

coffee ready
```
```py
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

coffee = int(input('What kind of coffee would you like? (1. Regular, 2. Sugar, 3. Black): '))
coffee_machine(coffee)
print('coffee ready')
```
```
What kind of coffee would you like? (1. Regular, 2. Sugar, 3. Black): 2

1. hot water preparation
2. paper cup ready
3. make sugar coffee
4. Pour water
5. Stir with a spoon to dissolve

coffee ready
```
```py
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
```
```
A: What kind of coffee would you like? (1. Regular, 2. Sugar, 3. Black): 1

1. hot water preparation
2. paper cup ready
3. make regular coffee
4. Pour water
5. Stir with a spoon to dissolve

A: coffee ready

B: What kind of coffee would you like? (1. Regular, 2. Sugar, 3. Black): 2

1. hot water preparation
2. paper cup ready
3. make sugar coffee
4. Pour water
5. Stir with a spoon to dissolve

B: coffee ready
```

## use of functions
- A function receives a parameter and returns a return value after processing and processing the parameter.
```py
def plus(num1, num2):
    result = num1 + num2
    return result

sum = 0
sum = plus(100, 200)
print('The pulse() function result of 100 and 200 is', sum)
```
```
The pulse() function result of 100 and 200 is 300
```
The plus() function is defined in lines 1 to 3, but it is not executed first. When the function is called on line 6, it is executed then.

1. function call
    - When calling the plus() function, call it in the form plus(number 1, number 2)
2. function execution
    - After adding num1 and num2 and assigning it to the result, return to the place where this function was called (=line 6) by the return result statement
3. return result
    - The result value (300) obtained by executing the function is returned to the place where the plus() function was called.
4. Assign return value to sum
    - Assign the returned value 300 to the variable sum

- Calculator function that adds, subtracts, multiplies, and divides two entered numbers
```py
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
```
```
calculation input(+, -, *, /); +
Enter the first number: 2
Enter the second number: 3
calculator: 2 + 3 = 5
```

## Understanding local and global variables
A local variable is a variable that is used only in a limited local area, and a global variable is a variable that is used throughout the program

```py
def func1():
    a = 10
    print('value of a in func1() : %d' % a)

def func2():
    print('value of a in func1() : %d' % a)

a = 20   # a is global variable
func1()
func2()
```
```
value of a in func1() : 10
value of a in func1() : 20
```
a in line 2 is a local variable because it is declared inside the func1( ) function, and a in line 8 is a global variable because it is declared outside the function.

-> What would happen to line 6 without the global variable in line 8?
```
value of a in func1() : 10
Traceback (most recent call last):
  File "/Users/injaelee/PycharmProjects/Test/PythonTest/functionTest.py", line 10, in <module>
    func2()
  File "/Users/injaelee/PycharmProjects/Test/PythonTest/functionTest.py", line 6, in func2
    print('value of a in func1() : %d' % a)
NameError: name 'a' is not defined
```
* func1( ) has a, so it outputs fine. There is no a in func2( ), so an error occurs. As a result, func2( ) does not recognize whether a (local variable) of func1( ) exists.

## Classification of functions according to the presence or absence of a return value
function with no return value
• Omit the return statement. Or just write return without a return value.

```py
def function1():
    result = 100
    return result

def function2():
    print('Executing a function with no return value')

sum = 0
sum = function1()
print('The value returned by function1(): %d' % sum)
function2()
```
```
The value returned by function1(): 100
Executing a function with no return value
```

## How to pass parameters
How to set the number of parameters
```py
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
```
```
Result of function call with 2 parameters: 30
Result of function call with 2 parameters: 60
```

How to set default values for parameters
```py
def para_func(num1, num2, num3 = 0):
    result = num1 + num2 + num3
    return result

sum = 0
sum = para_func(10, 20)
print('Result of function call with 2 parameters: %d' % sum)

sum = para_func(10, 20, 30)
print('Result of function call with 2 parameters: %d' % sum)
```
```
Result of function call with 2 parameters: 30
Result of function call with 2 parameters: 60
```

A method of not specifying the number of parameters - Arbitrary Argument List method
```py
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
```
```
Result of function call with 2 parameters: 30
Result of function call with 2 parameters: 60
```
- line 2: Set parameters with *para
- line 10: The called parameter is (10, 20)
- line 13: Called parameters are passed as tuples of the form (10, 20, 30)
- The parameters received in line 4 are extracted one by one with the for statement and accumulated in the result in line 5. For example, if (10, 20, 30) is received as a parameter, lines 4 to 5 are repeated 3 times as follows.
    - 1st time: After storing 10 in num, result += +10 → 10 is stored in result
    - 2nd time: After storing 20 in num, result += 20 → 30 is stored in result
    - 3rd time: After saving 30 in num, result += 30 → 60 is stored in result

If you add ** in front of a function's parameter, it is passed as a dictionary rather than a tuple. When calling a function, a dictionary-type parameter is also used in the ‘story key=value’ format.
```py
def dic_func(**para):
    for i in para.keys():
        print('%s --> %d people' % (i, para[i]))

dic_func(bigbang = 4, blackpink = 4, IDLE = 5, WJSN = 10)
```
```
bigbang --> 4 people
blackpink --> 4 people
IDLE --> 5 people
WJSN --> 10 people
```

## Exercise
### lottery number draw program
```py
import random

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
```
```
**** Lotto draw begins ****

lottery numbers drawn:  11 19 34 38 41 45
```
- line 4: random.randrange(start, end + 1) function extracts one random number from ‘start number ~ end number’
- line 10 ~ line 17: infinite repetition. If the number already drawn in lines 13-14 is not in the lotto[ ] list, add the number to the lotto[ ] list with the lotto.append(num) function.
- The lotto.count(num) function counts the number of num numbers in the lotto[ ] list and exits when it becomes 6.

## Understanding the module
It is convenient to create a function that is frequently used and import the function when using the function in the program.

All files to be used as modules and files to be called are stored in the same folder.
```py
import Func

Func.function1()
Func.function2()
Func.function3()
```
-> modulesTest.py
```py
def function1():
    print('function1() in Func.py is called')

def function2():
    print('function2() in Func.py is called')

def function3():
    print('function3() in Func.py is called')
```
-> Func.py
```
function1() in Func.py is called
function2() in Func.py is called
function3() in Func.py is called
```

If you named the module in the form 'Func.function name ( )' when you call, but you want to omit the module name and use it as a function name alone, modify it as follows:

    from module name import function1, function2, function3
    or
    from module name *

```py
from Func import function1, function2, function3

function1()
function2()
function3()
```
```py
from Func import *

function1()
function2()
function3()
```

## Module type
A standard module is a module provided by Python, a user-defined module is a module that you create and use,
and a 3rd party module is a module provided by a company or organization other than Python

- List of standard modules provided by Python
```py
import sys
print(sys.builtin_module_names)
```
```
('_abc', '_ast', '_codecs', '_collections', '_functools', '_imp', '_io', '_locale', '_operator',
'_signal', '_sre', '_stat', '_string', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'atexit',
'builtins', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'posix', 'pwd', 'sys', 'time', 'xxsubtype')
```

- Functions provided for each module can be known with the dir() function. In other words, to see the list of functions provided by the math module, use the following command
```py
import math
dir(math)
print(dir(math))
```
```
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh',
'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees',
'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum',
'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp',
'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod',
'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
```

## Exercise
### Completion of calculator program using module
```py
from myCal import *

num1 = float(input('Enter the first number: '))
mark = input('Enter operators (+, -, *, /): ')
num2 = float(input('Type a second number: '))

print()
print('*** Result of calling calculator written as a module ***')
if mark == '+':
    print('%5.1f + %5.1f = %5.1f' % (num1, num2, addition(num1, num2)))
elif mark == '-':
    print('%5.1f - %5.1f = %5.1f' % (num1, num2, subtraction(num1, num2)))
elif mark == '*':
    print('%5.1f * %5.1f = %5.1f' % (num1, num2, multiplication(num1, num2)))
elif mark == '/':
    print('%5.1f / %5.1f = %5.1f' % (num1, num2, division(num1, num2)))
else:
    print('"{}" Invalid input'.format(mark))
```
```py
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        num1 / num2
    else:
        print('not divisible by 0')
        return -1
```
