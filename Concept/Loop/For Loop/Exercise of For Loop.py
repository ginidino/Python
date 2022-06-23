# A factorial is a value obtained by multiplying a number from 1 to a specific number in sequence.
# Input an integer to find factorial, and output the calculated result
print('Factorial')
num = int(input('Enter the integer: '))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print('%d! = %d' % (num, factorial))
print()
# Draw a star shape as shown in the picture using the turtle graphic
# In this case, make the code simple by using the loop
print('Draw a star using for loop')
import turtle

turtle.shape('arrow')
for _ in range(5):      # in for _ in range(5): '_' means no index required
    turtle.forward(100)
    turtle.right(144)

# Draw a circle
# Use a for loop to repeat from 1 to 100 with an increasing radius of 5 increments.
turtle.shape('arrow')

for i in range(1, 101, 5):
    turtle.circle(i)
print()

# multiplication table
print('multiplication table')
for i in range(2, 10):
    for j in range(1, 10):
        print(' %d X %d = %2d' % (i, j, i * j))
    print("-------------")
print()

line = ""
for i in range(2, 10):
    line = line + (" # Table%d # " % i)

print(line)

for i in range(1, 10):
    line = ""
    for j in range(2, 10):
        line = line + str("%2d X %2d = %2d" % (j, i, j * i))
    print(line)
