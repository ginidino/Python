# Arithmetic Operators

### Arithmetic Operators
|Arithmetic Operators|Explanation|Usage Example|Example Description|
|-----|-----|-----|-----|
|=|assignment operator|a = 5|Substitute the integer 5 into a|
|+| add |a + b|Substitute the sum of 5 and 3 into a|
|-| subtract|a - bSubtract 5 and 3 and substitute in a|
|*| multiply |a * b|Substitute the value multiplied by 5 and 3 into a|
|/| division |a / b|Substitute 5 divided by 3 into a|
|//|Divide (share)|a // b|Divide 5 by 3 and substitute the share of the division into a|
|%|Remainder|a % b|Divide 5 by 3 and substitute the remainder into a|
|**|squared(power)|a ** b|Substitute 5 to the 3rd power of a|

code
```py
a = 5
b = 3
print('add: ', a + b)
print('subtract:', a - b)
print('multiply: ', a * b)
print('division: ', a / b)
print('Divide (share): ', a // b)
print('Remainder: ', a % b)
print('squared: ', a ** b)
```
```
add:  8
subtract: 2
multiply:  15
division:  1.6666666666666667
Divide (share):  1
Remainder:  2
squared:  125
```

### Priority
- The priority of the arithmetic operator is given by parentheses first, multiplication (or division), and addition (or subtraction) last.
- When addition (or subtraction) occurs or multiplication (or division) occurs, the calculation proceeds from left to right

```py
num1 = 2
num2 = 3
num3 = 4
print('num1 + num2 - num3 = ', num1 + num2 - num3)
print('num1 + num2 * num3 = ', num1 + num2 * num3)
print('num1 * num2 / num3 = ', num1 * num2 / num3)
```
```
num1 + num2 - num3 =  1
num1 + num2 * num3 =  14
num1 * num2 / num3 =  1.5
```
