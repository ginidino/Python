# Tutorial2

## Question1
Write a program to add two numbers and display a message if the output is divisible by 3 and 7.

Code
```py
num1 = int(input('Enter the frist number: '))
num2 = int(input('Enter the second number: '))
sum = num1 + num2
if sum % 3 == 0 and sum % 7 == 0:
    print('The sum %d of %d and %d is divisible by 3 and 7' % (sum, num1, num2))
else:
    print('The sum %d of %d and %d is not divisible by 3 and 7' % (sum, num1, num2))
```
Output
```
Enter the frist number: 6
Enter the second number: 8
The sum 14 of 6 and 8 is not divisible by 3 and 7
```

## Question2
Input a decimal number (requesting degrees) and convert this to radians

Code
```py
import math

degree = float(input('Enter the angle in degrees: '))
radians = degree * (math.pi / 180)
print(radians)
```
Output
```
Enter the angle in degrees: 23.5
0.41015237421866746
```

## Question3
Figure out if a number is positive or negative

Code
```py
num = int(input('Enter the number: '))
if num > 0:
    print('%d is positive number.' % num)
elif num < 0:
    print('%d is negative number.' % num)
else:
    print('%d is neither positive nor negative.' % num)
print()
```
Output
```
Enter the number: 4
4 is positive number.
```
