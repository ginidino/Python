print('break statement')
for i in range(1, 100):
    print('for loop used %d times' % i)
    break
print()

sum = 0
while True:
    num1 = int(input('Enter the first number: '))

    if num1 == 0:
        break

    num2 = int(input('Enter the second number: '))
    sum = num1 + num2
    print('%d + %d = %d' % (num1, num2, sum))
    print()
print('Enter 0 to escape the loop.')
print()

sum = 0
for i in range(1, 101):
    sum += i

    if sum >= 1000:
        break
print('The first position over 1000 in the sum of 1 to 100 : %d' % i)
print()

print('continue statement')
print('Sum of numbers from 1 to 100 but exclude multiples of 3 like 1 +2 +4 +5 +7 +8 +10 +...')
sum = 0
for i in range(1, 101):
    if i % 3 == 0:
        continue

    sum += i

print('Sum from 1 to 100 (excluding multiples of 3):', sum)
print()

# ♥ Output program
print('♥ Output program')
numStr = input('Enter multiple numbers: ')
print()

i = 0
ch = numStr[i]
while True:
    heartNum = int(ch)

    heartStr = ""

    for k in range(0, heartNum):
        heartStr += "\u2665"

    print(heartStr)

    i += 1
    if i > len(numStr) - 1:
        break

    ch = numStr[i]
