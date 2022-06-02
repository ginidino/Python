while True:
    word = str(input('Type a mark, , -, *, /: '))

    if word == 'exit':
        break

    num1 = int(input('Type a fist number: '))
    num2 = int(input('Type a second number: '))

    if word == '+':
        sum = num1 + num2
        print(num1, '+', num2, '=', sum, '\n')
    elif word == '-':
        subtraction = num1 - num2
        print(num1, '-', num2, '=', subtraction, '\n')
    elif word == '*':
        multiply = num1 * num2
        print(num1, '*', num2, '=', multiply, '\n')
    elif word == '/':
        division = num1 * num2
        print(num1, '/', num2, '=', division, '\n')
    else:
        print('"{}" Invalid input'.format(word), '\n')

