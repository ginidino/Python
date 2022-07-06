from Func import *

function1()
function2()
function3()
print()

import sys
print('standard modules')
print(sys.builtin_module_names)
print()

import math
print('math modules')
dir(math)
print(dir(math))
print()

# Completion of calculator program using module
print('calculator program using module')

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
