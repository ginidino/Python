# square: using pow function
import math

base = int(input('Type a base: '))
power = int(input('Type a power: '))
result = pow(base, power)
print(base, '^', power, pow(base, power))
print()

# Area of triangle and Rectangle
width = int(input('Type a width: '))
height = int(input('Type a height: '))

triangle = width * height / 2   # triangle
Rectangle = width * height      # Square
print('Area of triangle = ', triangle)
print('Area of square = ', Rectangle)
print()

# A code that receives an integer N between 3 and 6 and outputs
# the sum of the interior angles of a regular N polygon and the size of one interior angle
num = int(input('Type a integer between 3 and 6: '))
sumAngle = 180 * (num - 2)          # The sum of the sizes of the n-square interior = 180° × (n - 2)
intAngle = (180 * (num - 2)) / num  # The size of one interior angle of a regular n-gon = {180° × (n - 2)} ÷ n
print('정',num, '각형의 내각의 합 = ', sumAngle,'°')
print('정',num, '각형의 한 내각의 크기 = ', intAngle,'°')
print()

# Code to find the area of a circle by inputting the radius of the circle
radius = int(input('Type a the radius of the circle: '))
PI = math.pi
print(PI)
area = radius * radius * 3.14
area1 = radius * radius * PI
print('The area of the circle with ', radius, '= ', area)
print('The area of the circle with ', radius, '= ', area1)
