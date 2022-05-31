def add(x, y, z):
    return x + y + z

result = add(10, 30, 50)
print(result)

result = add(5, 7, 11)
print(result)

result = add(1, 3, 4)
print("{}\n".format(result))


def subtract(x, y):
    return x - y

result1 = subtract(20, 10)
print(result1)

result1 = subtract(35, 22)
print("{}\n".format(result1))


def multiply(x, y, w, z):
    return x * y * w * z

result2 = multiply(2, 3, 4, 5)
print(result2)

result2 = multiply(10, 20, 30, 40)
print("{}\n".format(result2))

# upper case
a = "Good morning, man"
upper = a.upper()
count = a.count('m')
change = a.swapcase()   # change upper to lower, lower to upper
print(upper)
print(count)
print(change + '\n')

# lower case
b = "GOOD MORNING MAN"
lower = b.lower()
print(b + '\n')

# replace
c = "Life is too short"
replace = c.replace("Life", "Your height")
print(replace + '\n')

# split
d = "I regret what I did to you"
split = d.split()
print(split)

e = "home,mother,sweet"
splits = e.split(',')
print(splits)
