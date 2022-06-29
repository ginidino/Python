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