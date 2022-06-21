# Conditional Expression
## Basic if statement
    if conditional expression: If the conditional expression is true, the statement to be executed is processed,
                               if false, the program is terminated without executing anything
### Determining true and false with the if statement
```py
num = int(input('Enter the number: '))
if num < 100:
    print('The number, %d is less than 100' % num)
```
```
Enter the number: 98
The number, 98 is less than 100
```

```py
a = 200

if a < 100:
    print('Less than 100')
print('Since it is false, you can not see this sentence, right?')

print('Done')
```
```
Since it is false, you can not see this sentence, right?
Done
```
- It runs until print('Since it is false, you can not see this sentence, right?'), which shouldn't be executed because of no indentation.
- Run it by modifying the line breaks like this:
```py
a = 200

if a < 100:
    print('Less than 100')
    print('Since it is false, you can not see this sentence, right?')

print('Done')
```
```
Done
```

- error occurs due to incorrect indentation
```py
if a < 100:
        print('Less than 100')
    print('Since it is false, you can not see this sentence, right?')
```

### if-else
It is used when the statement executed when true and the statement executed when false are different.

```py
a = 200

if a < 100:
    print('Less than 100')
else:
    print('Greater than 100')
```
```
Greater than 100
```

```py
a = 200

if a < 100:
    print('Less than 100')
    print('If true, would you see this sentence?')
else:
    print('Greater than 100')
    print('If false, would you see this sentence?')

print('program done')
```
```
Greater than 100
If false, would you see this sentence?
program done
```

#### Exercise
Program to count whether an input number is even or odd
```py
num = int(input('Enter the number: '))

if num % 2 == 0:
    print('This number, %d is even number' % num)
else:
    print('This number, %d is odd number' % num)
```

```
Enter the number: 43
This number, 43 is odd number
```

## if statement inside if statement
### if ~ else ~ if ~ else 
structure

    if conditional expression 1:
        if conditional expression 2:
            statement to be executed 1
        else:
            statement to be executed
    else:
        statement to run 3 

#### Exercise
- Greater or Less
```py
a = 75

if a > 50:
    if a < 100:
        print('Greater than 50 and less than 100')
    else:
        print('Greater than 100')
else:
    print('Less than 50')
```
```
Greater than 50 and less than 100
```
- Grade 
- use if-else
```py
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
```
```
Enter the score: 78
C
Grade
```
- use if ~ elif ~ else문
```py
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
```
```
Enter the score: 78
C
```
- simple calculator
```py
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
```
```
Type a fist number: 3
Type a mark: +
Type a second number: 2
3 + 2 = 5
```

### use with List
List : A list is a collection of several items in one place.
```py
fruit = ['Apple', 'Pear', 'Strawberry', 'Grape']
print(fruit)
```
```
['Apple', 'Pear', 'Strawberry', 'Grape']
```
'listname.append(item)’ function
```py
fruit.append('Orange')
print(fruit)
```
```
['Apple', 'Pear', 'Strawberry', 'Grape', 'Orange']
```
To check the list, use the if statement
```py
if 'Strawberry' in fruit:
    print('There is a Strawberry in list')
```
```
There is a Strawberry in list
```
- ‘if item in list:’ returns True if there is an item in the list
