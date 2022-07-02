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
