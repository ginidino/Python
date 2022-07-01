# A function that divides and returns the quotient and remainder
# If 0 is entered as the divisor, it warns that it cannot be divided by 0 and exits the program.
print('quotient and remainder')
def division(divisor, divided):
    result = []

    if divisor == 0:
        print('cannot be divided by zero')
        exit()

    quotient = divisor // divided
    remainder = divisor % divided

    result.append(quotient)
    result.append(remainder)

    return result

num1 = int(input('Enter the divisor: '))
num2 = int(input('Enter the number to be divided: '))
result = division(num1, num2)
print(f'quotient of {num1} / {num2} is {result[0]}, and remainder is {result[1]}')
print()

# A function that takes an answer as input and returns the length of the answer(Write a short-form answer in 20 characters or more)
print('counting letters')
def count(answer):
    result = len(answer)
    return  result

answer = input('Enter the answer: ')
if count(answer) >= 20:
    print('The answer is %d characters. passed.' % (count(answer)))
else:
    print('Please re-write the answer')