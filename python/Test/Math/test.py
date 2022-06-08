import math

# square: using pow function
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
print()

# There is a farm that raises chickens, pigs, and cows. How many total legs
chicken = int(input('Number of chickens: '))
pig = int(input('Number of pigs: '))
cow = int(input('Number of cows: '))

sumOfLegs = (chicken * 2) + (pig * 4) + (cow * 4)
print('Total legs is ', sumOfLegs, '\n')

# Takes hours and minutes as input and converts them to seconds
hour = int(input('Enter the hour: '))
min = int(input('Enter the minutes: '))

seconds = (hour * 3600) + (min * 60)

print(hour, 'hour', min, 'minutes is ', seconds, 'second', '\n')

# Takes the coordinates of two points and calculates the distance between them
# pow(𝑎,𝑏)=𝑎^𝑏  𝑎∗∗0.5= √𝑎   Distance= √(𝑥1 −𝑥2)^2 + (𝑦1 −𝑦2)^2
x1 = int(input('x1: '))
x2 = int(input('x2: '))
y1 = int(input('y1: '))
y2 = int(input('y2: '))

distance = (pow((x1 - x2), 2) + pow((y1 - y2), 2)) ** 0.5
dis = math.sqrt((pow((x1 - x2), 2) + pow((y1 - y2), 2)))  # uisng math function
print('distance between two points: ', distance)
print('distance between two points: ', dis, '\n')

# Convert Fahrenheit temperature to Celsius temperature
# 𝐶 = (𝑓−32.0) * 5/9
fahrenheit = int(input('Enter the temperature in degrees Fahrenheit: '))
celsius = (fahrenheit - 32.0) * 5/9
print(fahrenheit, ' degrees Fahrenheit is ', celsius, 'degrees Celsius')
