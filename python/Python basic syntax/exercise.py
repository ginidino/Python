# test 1
# 변수 a에 숫자 10을 넣고 출력
a = 10
print(a)
print()

# 변수 city에 문자 seoul을 넣고 출력
city = 'seoul'
print(city)
print()

# 변수 c에 20, 변수 d에 30을 넣고 둘을 더해보세요
c = 20
d = 30
sum = c + d
print(sum)
print()

# 홀수만 5개 있는 리스트를 만들어서 출력
odd_number = [1, 3, 5, 7, 9]
print(odd_number)
print()

# 도시 이름을 3개 넣은 리스트를 만들어서 출력
city = ['seoul', 'london', 'birmingham']
print(city)
print()

# 과일(fruit) 사전을 만들어보세요. 키는 color, size
fruit = {}
fruit['color'] = 'red'
fruit['size'] = 10

print(fruit)
print(fruit.get('color'))
print(fruit['size'])
print()

fruits = {'color' : 'Red', 'size' : 10}
print(fruits.get('color'))
print(fruits.get('size'))
print()

dicFruit = {'color' : 'red'}
dicFruit['size'] = 10
print(dicFruit)
print()

# For문을 써서 1부터 10까지의 합을 구한 뒤 출력
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in num:
    sum += i
print(sum)
print()

total = 0
for i in range(1, 10):
    total += i
print(total)
print()

# For문과 If 문을 써서 홀수만 출력 until 20
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
print()

# 삼각형의 넓이를 구하는 함수
def triangle(width, height):
    return (width * height) / 2

triangleArea = triangle(20, 10)
print(triangleArea)
print()

# 원의 넓이를 구하는 함수
def circle(radius):
    return 3.14 * radius * radius

circleArea = circle(5)
print(circleArea)