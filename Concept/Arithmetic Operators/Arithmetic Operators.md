# Arithmetic Operators

### Arithmetic Operators
|Arithmetic Operators|Explanation|Usage Example|Example Description|
|-----|-----|-----|-----|
|=|assignment operator|a = 5|Substitute the integer 5 into a|
|+| add |a + b|Substitute the sum of 5 and 3 into a|
|-| subtract|a - bSubtract 5 and 3 and substitute in a|
|*| multiply |a * b|Substitute the value multiplied by 5 and 3 into a|
|/| division |a / b|Substitute 5 divided by 3 into a|
|//|Divide (quotient)|a // b|Divide 5 by 3 and substitute the quotient of the division into a|
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
print('Divide (quotient): ', a // b)
print('Remainder: ', a % b)
print('squared: ', a ** b)
```
```
add:  8
subtract: 2
multiply:  15
division:  1.6666666666666667
Divide (quotient):  1
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

### Interconversion of strings and numbers
- String is converted to integer by int() function and real number by float() function
```py
s1 = "100"
s2 = "100.12"
s3 = "999999999999"
int1 = int(s1)
fl = float(s2)
int2 = int(s3)
print(int1 + 1,', ', fl + 1,', ', int2 + 1)
```
```
101 ,  101.12 ,  1000000000000
```
- To convert a number to a string, use the str() function
```py
a = 100
b = 100.123
str1 = str(a)
str2 = str(b)
print(str1 + '1', ', ', str2 + '1')
```
```
1001 ,  100.1231
```

### Types of assignment operators
|assignment operators|Usage Example|Example Description|
|---|---|---|
|+=|a += 3|Equal to a = a + 3|
|-=|a -= 3|Equal to a = a - 3|
|*=|a *= 3|Equal to a = a * 3|
|/=|a /= 3|Equal to a = a / 3|
|//=|a //= 3|Equal to a = a // 3|
|%=|a %= 3|Equal to a = a % 3|
|**=|a **= 3|Equal to a = a ** 3|

- a starts at 10 and accumulates as the program progresses
```py
a = 10
a += 5
print(a)
a -= 5
print(a)
a *= 5
print(a)
a /= 5
print(a)
a //= 5
print(a)
a %= 5
print(a)
a **= 5
print(a)
```
```
15
10
50
10.0
2.0
2.0
32.0
```
