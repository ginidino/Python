# Task1
import random

ranNum = random.random()
print(ranNum)
print()

# Task2
flip = random.random()
print(flip)
if flip > 0.5:
    print('True')
else:
    print('False')
print()

# Task3
p = float(input('Enter probability of the flip : '))
flip = random.random()
print(flip)

if p >= flip:
    print('Head')
else:
    print('Tail')
print()

# Task 4
ranNum = random.randint(1, 100)

num = int(input('Enter the number: '))

if num > ranNum:
    print('too big')
elif num < ranNum:
    print('too small')
else:
    print('correct')
print()

# Task 5
grade = int(input('Enter your grade: '))
if grade < 0 or grade > 100:
    print('invalid output')
elif grade >= 80:
    print('A')
elif 70 <= grade < 80:
    print('B')
elif 60 <= grade < 70:
    print('C')
elif 50 <= grade < 60:
    print('D')
else:
    print('F')
print()

# Task 6
num1 = int(input('Enter an even number between 10 to 50: '))

if num < 10 or num > 50:
    print('invalid output')
else:
    ranNum = random.randint(10, 100)
    print(ranNum)

    result = 0
    if ranNum % 7 == 0 and num1 >= ranNum:
        result = num1 + ranNum
        print("The sum of the number you have entered, %d and the generated number, %d is: %d" % (num, ranNum, result))
    else:
        result = num1 * ranNum
        print("The product of the number you have entered, %d and the generated number, %d is: %d" % (num, ranNum, result))