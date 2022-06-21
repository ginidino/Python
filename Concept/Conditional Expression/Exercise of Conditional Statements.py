# Program to count whether an input number is even or odd
print('even number or odd number')
num = int(input('Enter the number: '))

if num % 2 == 0:
    print('This number, %d is even number' % num)
else:
    print('This number, %d is odd number' % num)
print()

# program to determine whether an input number is a multiple of 3
print('determine whether an input number is a multiple of 3')
num = int(input('Enter the number: '))

if num % 3 == 0:
    print('The number, %d is multiple of 3' % num)
else:
    print('The number, %d is not multiple of 3' % num)
print()

# If you enter household members, the estimated disaster assistance you will receive is printed out
# The national disaster subsidy can be received by up to 4 people at a rate of 250,000 won per household member
print('National Disaster Assistance Support')

member = int(input('Enter the number of family members: '))
support = member * 250000

if member == 1:
    print('The estimated subsidy is', support, '₩')
elif member == 2:
    print('The estimated subsidy is', support, '₩')
elif member == 3:
    print('The estimated subsidy is', support, '₩')
elif member == 4:
    print('The estimated subsidy is', support, '₩')
print()

# Calculate age by year of birth
# If you are over 15 and under 20, print “You are a teenager.”
print('Calculate age by year of birth')
year = int(input('Enter the year: '))
yearOfBirth = int(input('Enter the year of birth: '))

age = year - yearOfBirth

if 15 < age < 20:
    print('You are a teenager')
else:
    print('You are not a teenager')
print('You are %d this year' % age)
print()

# Grade (use if-else)
score = int(input('Enter the score: '))
if score >= 90:
    print('A')
else:
    if score >= 80:
        print('B')
    else:
        if score >= 70:
            print('C')
        else:
            if score >= 60:
                print('D')
            else:
                print('F')
print('Grade')
print()

# Grade (use if ~ elif ~ else)
print('Grade')
score = int(input('Enter the score: '))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
print()

# simple calculator
print('simple calculator')
num1 = int(input('Type a fist number: '))
word = input('Type a mark: ')
num2 = int(input('Type a second number: '))

if word == '+':
    print("%d + %d = %d" % (num1, num2, num1 + num2))
elif word == '-':
    print("%d - %d = %d" % (num1, num2, num1 - num2))
elif word == '*':
    print("%d * %d = %d" % (num1, num2, num1 * num2))
elif word == '/':
    print("%d / %d = %d" % (num1, num2, num1 / num2))
elif word == '%':
    print("%d % %d = %d" % (num1, num2, num1 % num2))
elif word == '//':
    print("%d // %d = %d" % (num1, num2, num1 // num2))
elif word == '**':
    print("%d ** %d = %d" % (num1, num2, num1 ** num2))
else:
    print('"{}" Invalid input'.format(word))
print()

# Program to find numbers from 0 to 9 that are not in a list
import random

print('Find the numbers')
numbers = []
for num in range(0, 10):
    numbers.append(random.randrange(0, 10))

print('creation list', numbers)

for num in range(0, 10):
    if num not in numbers:
        print('%d is not in the list' % num)
print()

# Comprehensive calculator
print('Comprehensive calculator')
select = int(input("1. formula calculator   2. sum between two numbers: "))

if select == 1:
    numStr = input('Enter the formula: ')
    answer = eval(numStr)
    print('Result of %s is %5.1f' % (numStr, answer))
elif select == 2:
    num1 = int(input('Type a fist number: '))
    num2 = int(input('Type a second number: '))
    for i in range(num1, num2 + 1):
        answer = answer + i
    print('%d + ... + %d is %d' % (num1, num2, answer))
else:
    print('Only 1 or 2 must be entered.')