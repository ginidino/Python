a = 10
print(a)

b = 20
print(b)

sum = a + b
print(sum)

c = 50
d = 40
diff = c - d
print(diff)

e = 50
f = 40

result = e / f
print(result)

result = e // f
print(result)

result = e % f
print(result)


user = {}
user['age'] = 25
user['city'] = 'seoul'

print(user)
print(user['age'])
print(user.get('age'))

user['age'] = 30
print(user.get('age'))

live_in_seoul = True
if live_in_seoul:
    print('Living in seoul')

# not working
live_in_london = False
if live_in_london:
    print('not living in london')

name = 'Paul'
if name == 'Paul':
    print('My name is Paul')
else:
    print('My name is not Paul')

age = 25
if age > 20:
    print('older than 20')
else:
    print('younger than 20')

odd_num = [1, 3, 5, 7, 9, 11, 13, 15]
for num in odd_num:
    print(odd_num)

num = [1, 2, 3, 4, 5, 6, 7]
for i in num:
    if i % 2 == 0:
        print(i)

ages = [10, 21, 25, 33, 44, 55, 66]
for index in ages:
    if index > 30:
        print(index)
        break

