# For Statement

## concept of for statement
```py
for i in range(0, 3, 1):
    print('This is for loop')
```
```
This is for loop
This is for loop
This is for loop
```

## for statement operation

### The range( ) function returns a value in a specified range.

      form:
      for variable in range(start value, end value + 1, increment value):
          repeat this part

### range(0, 3, 1) equals [0, 1, 2]
```py
for i in range(0, 3, 1):
    print('This is for loop')
```
```py
for i in [0, 1, 2]:
    print('This is for loop')
```

    1st time: After substituting 0 for i, print() is output.
    2nd time: After substituting 1 for i, print() is printed.
    3rd time: Substitute 2 for i and print()

### Print() uses the value of i to print the first number
```py
for i in range(0, 3, 1):
    print('%d : This is for loop' % i)
```
```
0 : This is for loop
1 : This is for loop
2 : This is for loop
```
### A program that executes the print() function three times with the starting value of the range() function set to 2 and decreasing the i value by 1 (until it becomes 0)
```py
for i in range(2, -1, -1):
    print('%d : This is for loop' % i)
```
```
2 : This is for loop
1 : This is for loop
0 : This is for loop
```
### Print the numbers from 1 to 5 in sequence.
```py
for i in range(0, 6, 1):
    print('%d' % i, end=" ")
```
```
0 1 2 3 4 5 
```
- The reason the output is on one line is because end=“ ” is written at the end of the print() function.

## Finding the sum using the For statement
form:

    Prepare a variable to change from 1 to 10 (i)

    The for variable (i) starts at 1 and increases by 1 until 10.
      add i to sum

    print the value of sum
```py
i = 0

for i in range(1, 11, 1):
    sum = sum + i
print('Sum from 1 to 10: %d' % sum)
```
```
Traceback (most recent call last):
  File "/Users/injaelee/PycharmProjects/Test/PythonTest/For Loop.py", line 4, in <module>
    sum = sum + i
TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'int'
```
→ Error Occur : because variable sum is not declared
```py
i = 0
sum = 0
for i in range(1, 11, 1):
    sum = sum + i
print('Sum from 1 to 10: %d' % sum)
```
```
Sum from 1 to 10: 55
```

### Program to find the sum of odd numbers between 500 and 1000
```py
sum = 0
for i in range(500, 1001, 1):
    if i % 2 != 0:
        sum = sum + i
print('Sum of odd numbers between 500 and 1000: %d' % sum)

# Another way
total = 0
for i in range(501, 1001, 2):
    total = total + i
print('Sum of odd numbers between 500 and 1000: %d' % sum)
```
```
Sum of odd numbers between 500 and 1000: 187500
Sum of odd numbers between 500 and 1000: 187500
```

### Sum up to the entered value with the for statement
* A program that calculates the sum from 1 to the number entered by the user by inputting the desired value.
```py
num = int(input('Enter the number: '))
sum = 0
for i in range(1, num + 1, 1):
    sum = sum + i
print('Sum from 1 to %d: %d' % (num, sum))
```
```
Enter the number: 100
Sum from 1 to 100: 5050
```
* The start value, end value, and increment value are all input from the user and calculated
```py
startValue = int(input('Enter the start value: '))
endValue = int(input('Enter the end value: '))
increase = int(input('Enter the increment value: '))

sum = 0

for i in range(startValue, endValue, increase):
    sum = sum + i
print('Sum of values from %d to %d in %d increments: %d' % (startValue, endValue, increase, sum))
```
```
Enter the start value: 2
Enter the end value: 300
Enter the increment value: 3
Sum of values from 2 to 300 in 3 increments: 15050
```
* A program that prints the multiplication table of an input number
```py
table = int(input('What table ? '))

for i in range(1, 10, 1):
    print(' %d X %d = %2d' %(table, i, table * i))
```
```
7 X 1 = 7
 7 X 2 = 14
 7 X 3 = 21
 7 X 4 = 28
 7 X 5 = 35
 7 X 6 = 42
 7 X 7 = 49
 7 X 8 = 56
 7 X 9 = 63
```

## The concept of nested for statements
A nested for statement has another for statement inside the for statement
```py
for i in range(0, 3, 1):
    for j in range(0, 2, 1):
        print('This is python (i: %d, j: %d)' % (i, j))
```
```
This is python (i: 0, j: 0)
This is python (i: 0, j: 1)
This is python (i: 1, j: 0)
This is python (i: 1, j: 1)
This is python (i: 2, j: 0)
This is python (i: 2, j: 1)
```

### The number of executions of the nested for statement is ‘the number of repetitions of the outer for statement × the number of repetitions of the inner for statement’

order in which they are processed: 

    ⑴ External for statement 1 time: substitute 0 for i
        Internal for statement 1 time: insert 0 into j and run print()
        Internal for statement 2 times: insert 1 into j and run print()

    ⑵ External for statement 2 times: substitute 1 for i
        Internal for statement 1 time: insert 0 into j and run print()
        Internal for statement 2 times: insert 1 into j and run print()

    ⑶ External for statement 3 times: substitute 2 for i
        Internal for statement 1 time: insert 0 into j and run print()
        Internal for statement 2 times: insert 1 into j and run print()

## Use of nested for statements
Output from 2nd to 9th stage of multiplication table
```py
for i in range(2, 10):
    for j in range(1, 10):
        print(' %d X %d = %2d' % (i, j, i * j))
    print("-------------")
```
```
2 X 1 =  2
 2 X 2 =  4
 2 X 3 =  6
 2 X 4 =  8
 2 X 5 = 10
 2 X 6 = 12
 2 X 7 = 14
 2 X 8 = 16
 2 X 9 = 18
-------------
 3 X 1 =  3
 3 X 2 =  6
 3 X 3 =  9
 3 X 4 = 12
 3 X 5 = 15
 3 X 6 = 18
 3 X 7 = 21
 3 X 8 = 24
 3 X 9 = 27
-------------
 4 X 1 =  4
 4 X 2 =  8
 4 X 3 = 12
 4 X 4 = 16
 4 X 5 = 20
 4 X 6 = 24
 4 X 7 = 28
 4 X 8 = 32
 4 X 9 = 36
-------------
 5 X 1 =  5
 5 X 2 = 10
 5 X 3 = 15
 5 X 4 = 20
 5 X 5 = 25
 5 X 6 = 30
 5 X 7 = 35
 5 X 8 = 40
 5 X 9 = 45
-------------
 6 X 1 =  6
 6 X 2 = 12
 6 X 3 = 18
 6 X 4 = 24
 6 X 5 = 30
 6 X 6 = 36
 6 X 7 = 42
 6 X 8 = 48
 6 X 9 = 54
-------------
 7 X 1 =  7
 7 X 2 = 14
 7 X 3 = 21
 7 X 4 = 28
 7 X 5 = 35
 7 X 6 = 42
 7 X 7 = 49
 7 X 8 = 56
 7 X 9 = 63
-------------
 8 X 1 =  8
 8 X 2 = 16
 8 X 3 = 24
 8 X 4 = 32
 8 X 5 = 40
 8 X 6 = 48
 8 X 7 = 56
 8 X 8 = 64
 8 X 9 = 72
-------------
 9 X 1 =  9
 9 X 2 = 18
 9 X 3 = 27
 9 X 4 = 36
 9 X 5 = 45
 9 X 6 = 54
 9 X 7 = 63
 9 X 8 = 72
 9 X 9 = 81
-------------
```

### Completion of multiplication table printing program
Existing multiplication table results are printed vertically, so you have to scroll to see the results.   
Modify the program to show the multiplication table result in the right margin

```py
line = ""
for i in range(2, 10):
    line = line + (" # Table%d # " % i)

print(line)

for i in range(1, 10):
    line = ""
    for j in range(2, 10):
        line = line + str("%2d X %2d = %2d" % (j, i, j * i))
    print(line)
```
```
# Table2 #  # Table3 #  # Table4 #  # Table5 #  # Table6 #  # Table7 #  # Table8 #  # Table9 # 
 2 X  1 =  2 3 X  1 =  3 4 X  1 =  4 5 X  1 =  5 6 X  1 =  6 7 X  1 =  7 8 X  1 =  8 9 X  1 =  9
 2 X  2 =  4 3 X  2 =  6 4 X  2 =  8 5 X  2 = 10 6 X  2 = 12 7 X  2 = 14 8 X  2 = 16 9 X  2 = 18
 2 X  3 =  6 3 X  3 =  9 4 X  3 = 12 5 X  3 = 15 6 X  3 = 18 7 X  3 = 21 8 X  3 = 24 9 X  3 = 27
 2 X  4 =  8 3 X  4 = 12 4 X  4 = 16 5 X  4 = 20 6 X  4 = 24 7 X  4 = 28 8 X  4 = 32 9 X  4 = 36
 2 X  5 = 10 3 X  5 = 15 4 X  5 = 20 5 X  5 = 25 6 X  5 = 30 7 X  5 = 35 8 X  5 = 40 9 X  5 = 45
 2 X  6 = 12 3 X  6 = 18 4 X  6 = 24 5 X  6 = 30 6 X  6 = 36 7 X  6 = 42 8 X  6 = 48 9 X  6 = 54
 2 X  7 = 14 3 X  7 = 21 4 X  7 = 28 5 X  7 = 35 6 X  7 = 42 7 X  7 = 49 8 X  7 = 56 9 X  7 = 63
 2 X  8 = 16 3 X  8 = 24 4 X  8 = 32 5 X  8 = 40 6 X  8 = 48 7 X  8 = 56 8 X  8 = 64 9 X  8 = 72
 2 X  9 = 18 3 X  9 = 27 4 X  9 = 36 5 X  9 = 45 6 X  9 = 54 7 X  9 = 63 8 X  9 = 72 9 X  9 = 81
```
