# Question1
num1 = int(input('Enter the frist number: '))
num2 = int(input('Enter the second number: '))
sum = num1 + num2
if sum % 3 == 0 and sum % 7 == 0:
    print('The sum %d of %d and %d is divisible by 3 and 7' % (sum, num1, num2))
else:
    print('The sum %d of %d and %d is not divisible by 3 and 7' % (sum, num1, num2))
print()

# Qustion2
import math

degree = float(input('Enter the angle in degrees: '))
radians = degree * (math.pi / 180)
print(radians)
print()

# Question3
num = int(input('Enter the number: '))
if num > 0:
    print('%d is positive number.' % num)
elif num < 0:
    print('%d is negative number.' % num)
else:
    print('%d is neither positive nor negative.' % num)
print()