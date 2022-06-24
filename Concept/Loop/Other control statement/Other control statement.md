# Other control statement

## break statement to escape from the loop
### Example of break statement
```py
for i in range(1, 100):
    print('for loop used %d times' % i)
    break
```
```
for loop used 1 times
```
```py
sum = 0
while True:
    num1 = int(input('Enter the first number: '))

    if num1 == 0:
        break

    num2 = int(input('Enter the second number: '))
    sum = num1 + num2
    print('%d + %d = %d' % (num1, num2, sum))
    print()
print('Enter 0 to escape the loop.')
```
```
Enter the first number: 12
Enter the second number: 24
12 + 24 = 36

Enter the first number: 0
Enter 0 to escape the loop.
```

- Add from 1 to 100, but find the starting point where the cumulative sum is greater than or equal to 1000
```py
sum = 0
for i in range(1, 101):
    sum += i

    if sum >= 1000:
        break
print('The first position over 1000 in the sum of 1 to 100 : %d' % i)
```
```
The first position over 1000 in the sum of 1 to 100 : 45
```

## continue statement returning to the loop
When a continue statement is encountered, the remainder of the block is skipped unconditionally and returns to the beginning of the loop.

### Example of continue statement
- Program to find the sum of numbers from 1 to 100 but exclude multiples of 3 like 1 +2 +4 +5 +7 +8 +10 +...
```py
sum = 0
for i in range(1, 101):
    if i % 3 == 0:
        continue

    sum += i

print('Sum from 1 to 100 (excluding multiples of 3):', sum)
```
```
Sum from 1 to 100 (excluding multiples of 3): 3367
```
