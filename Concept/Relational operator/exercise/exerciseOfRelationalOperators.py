'''
Alcohol cannot be sold to minors.
A program that determines whether alcohol can be purchased by entering an age
'''
print('alcohol purchase age')
age = int(input('Enter your age: '))
print('Whether alcohol is available for purchase:', age > 20)
print()

# A program that takes an integer as input and determines if it is a multiple of 3
print('multiple of 3')
num = int(input('Enter an integer: '))
print('Is it a multiple of 3?:', num % 3 == 0)
print()

# program that receives word,'university' and checks whether they are entered correctly
print('check the word, "university"')
word = input('Enter the university: ')
print(word == 'university')