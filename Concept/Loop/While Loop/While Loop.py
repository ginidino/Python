i = 0
while i < 3:
    print('%d : This is while loop' % i)
    i = i + 1

i = 1
sum = 0
while i < 11:
    sum = sum + i
    i = i + 1

print('Sum from 1 to 10: %d' % sum)

while True:
    print('lol', end = " ")

sum = 0
while True:
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    sum = num1 + num2
    print('%d + %d = %d' % (num1, num2, sum))
    print()

while True:
    num1 = int(input('Type a fist number: '))
    num2 = int(input('Type a second number: '))
    word = input('Type a mark, +, -, *, /, //, %, **: ')

    if word == '+':
        print("%d + %d = %d" % (num1, num2, num1 + num2))
    elif word == '-':
        print("%d - %d = %d" % (num1, num2, num1 - num2))
    elif word == '*':
        print("%d * %d = %d" % (num1, num2, num1 * num2))
    elif word == '/':
        print("%d / %d = %5.2f" % (num1, num2, num1 / num2))
    elif word == '%':
        print("%d %% %d = %d" % (num1, num2, num1 % num2))
    elif word == '//':
        print("%d // %d = %d" % (num1, num2, num1 // num2))
    elif word == '**':
        print("%d ** %d = %d" % (num1, num2, num1 ** num2))
    else:
        print('"{}" Invalid input'.format(word))