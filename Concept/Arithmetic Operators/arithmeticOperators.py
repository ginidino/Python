# Arithmetic Operators
a = 5
b = 3
print('add: ', a + b)
print('subtract:', a - b)
print('multiply: ', a * b)
print('division: ', a / b)
print('Divide (quotient): ', a // b)
print('Remainder: ', a % b)
print('squared: ', a ** b)
print()

# Priority
print('Calculation order')
num1 = 2
num2 = 3
num3 = 4
print('num1 + num2 - num3 = ', num1 + num2 - num3)
print('num1 + num2 * num3 = ', num1 + num2 * num3)
print('num1 * num2 / num3 = ', num1 * num2 / num3)
print()

# Interconversion of strings and numbers
print('Interconversion of strings and numbers')
print('String -> int, float')
s1 = "100"
s2 = "100.12"
s3 = "999999999999"
int1 = int(s1)
fl = float(s2)
int2 = int(s3)
print(int1 + 1,', ', fl + 1,', ', int2 + 1)
print()

print('int, float -> String')
a = 100
b = 100.123
str1 = str(a)
str2 = str(b)
print(str1 + '1', ', ', str2 + '1')
print()

# a starts at 10 and accumulates as the program progresses
print('"a" starts at 10 and accumulates as the program progresses')
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
