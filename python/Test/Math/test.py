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
