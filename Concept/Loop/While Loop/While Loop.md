# While Loop
## Comparison of for loop and while loop
### for loop 
```
for variable in rainge(start value, end value + 1, increment value)
```
```py
for i in range(0, 3, 1):
    print('%d : This is for loop' % i)
```
```
0 : This is for loop
1 : This is for loop
2 : This is for loop
```

### while loop 
```
variable = start value
while variable value < end value
 repeat this part
 variable = variable + increment value
```
```py
i = 0
while i < 3:
    print('%d : This is while loop' % i)
    i = i + 1
```
```
0 : This is while loop
1 : This is while loop
2 : This is while loop
```
The while loop checks the conditional expression inside the while loop and executes the ‘statement’ if the value is true. Repeat as long as conditional expression is true

### Exercise
- Sum from 1 to 10 using while statement
```py
i = 1
sum = 0
while i < 11:
    sum = sum + i
    i = i + 1

print('Sum from 1 to 10: %d' % sum)
```
```
Sum from 1 to 10: 55
```

## while loop for an infinite loop
To apply an infinite loop, set the conditional expression of ‘while conditional expression:’ to True
```py
while True:
    print('lol', end = " ")
```
```
lol lol lol lol lol lol lol lol lol lol lol lol lol lol lol lol lol lol lol  ~~~ infinite loop
```

### Exercise
- Repeatedly calculates the sum of two numbers entered
```py
sum = 0
while True:
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    sum = num1 + num2
    print('%d + %d = %d' % (num1, num2, sum))
    print()
```
```
Enter the first number: 24
Enter the second number: 32
24 + 32 = 56

Enter the first number: 15
Enter the second number: 63
15 + 63 = 78

Enter the first number: 
~~~
```

- Addition, subtraction, multiplication, division, finding remainder
```py
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
```
```
Type a fist number: 10
Type a second number: 4
Type a mark, +, -, *, /, //, %, **: %
10 % 4 = 2
Type a fist number: 53
Type a second number: 32
Type a mark, +, -, *, /, //, %, **: /
53 / 32 =  1.66
Type a fist number: 
~~~
```
