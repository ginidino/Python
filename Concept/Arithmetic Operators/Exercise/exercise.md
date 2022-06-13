# exercise code and output
1. code
```py
# coin exchange program
print('coin exchange program')
c500 = 0
c100 = 0
c50 = 0
c10 = 0

money = int(input('How much money to exchange? '))
c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print('500₩: %d '% c500)
print('100₩: %d '% c100)
print('50₩: %d '% c50)
print('10₩: %d '% c10)
print('remaining change %d ₩ \n' % money)
print()

# Program to find the sum of sales in the first quarter
print('sum of sales in the first quarter')
JanuarySales = int(input('January sales: '))
FebruarySales = int(input('February sales: '))
MarchSales = int(input('March sales: '))

sumOfSales = JanuarySales + FebruarySales + MarchSales
print('sum of sales in the first quarter : {:0,}₩'.format(sumOfSales))
print('sum of sales in the first quarter :', sumOfSales, '₩')
print()

# Calculate the revenue for the first quarter
print('Calculate the revenue for the first quarter')
sales = int(input('Sales in the first quarter: '))
purchases = int(input('Purchases in the first quarter: '))
revenue = sales - purchases

print('Revenue : {:0}₩'.format(revenue))
print('Revenue :', revenue, '₩')
print()

# program that calculates your body mass index (BMI) by entering your weight and height
# BMI = BMI = Weight (kg) / Height squared (m^2)
print('BMI')
weight = float(input('Enter the Weight(kg): '))
height = float(input('Enter the Height(m): '))

BMI = int(weight / pow(height, 2))
print('BMI:', BMI)
print()

# Program to find the quotient and remainder by dividing
print('quotient and remainder')
num1 = int(input('divisible number: '))
num2 = int(input('divisor: '))

division = num1 / num2
quotient = num1 // num2
remainder = num1 % num2

print('Result of dividing %d by %d' % (num1, num2))
print('division:',division)
print('quotient:', quotient)
print('remainder:', remainder)
print()

'''
When the number of bacteria after N hours is as follows,
the code to output the number of bacteria after 24 hours of 100 bacteria
# Number of bacteria after N hours = (initial number) × 2^N
'''
print('the code to output the number of bacteria after 24 hours of 100 bacteria')
numOfBacteria = 100
time = 24
result = numOfBacteria * pow(2, time)
result1 = numOfBacteria * (2 ** time)

print('Count of %d bacteria after %d hours = %d' % (numOfBacteria, time, result))
print('Count of', numOfBacteria, 'bacteria after', time,'hours =', result1)
print()

'''
code that prints the number of pencils that can be purchased and change 
after inputting the amount to purchase 400 won pencils each.
'''
print('Number of pencils you can buy and change')
money1 = int(input('Enter the amount in ₩ '))
priceOfPencil = 400
numOfPencils = money1 // priceOfPencil
change = money1 % priceOfPencil

print('number of pencils:', numOfPencils)
print('charge:', change,'₩')
print()

'''
program that takes as input the number of pizza plates and the number of people, 
and calculates how many slices each person eats and how many slices are left
'''
print('calculates how many slices each person eats and how many piece are left')
people = int(input('Enter the number of people '))
order = int(input('Pizza order quantity: '))
piece = int(input('Number of pizza piece: '))

result = (order * piece) // people
remain = (order * piece) % people

print('available eat %d pieces, and %d pieces are left' % (result, remain))

'''
If you put 5 million won in a term deposit with an annual interest rate of 2% and compound interest
calculate the total amount you will receive after 3 years
'''
print('compounding calculation')
myMoney = 5000000
rate = 0.02

myMoney += myMoney * rate   # after 1 year
myMoney += myMoney * rate   # after 2 year
myMoney += myMoney * rate   # after 3 year

print('Total amount received after 3 years', int(myMoney), '₩')
print()

# Program to find the area of a circle by inputting the radius of a circle to the decimal point
print('area of circle')
radius = float(input('radius of a circle: '))
area = 3.14 * radius * radius

print('The area of a circle of', radius, 'is', area)
```
2. output
```
coin exchange program
How much money to exchange? 5235
500₩: 10 
100₩: 2 
50₩: 0 
10₩: 3 
remaining change 5 ₩ 


sum of sales in the first quarter
January sales: 543400
February sales: 234100
March sales: 425300
sum of sales in the first quarter : 1,202,800₩
sum of sales in the first quarter : 1202800 ₩

Calculate the revenue for the first quarter
Sales in the first quarter: 6231000
Purchases in the first quarter: 3147000
Revenue : 3084000₩
Revenue : 3084000 ₩

BMI
Enter the Weight(kg): 70
Enter the Height(m): 1.73
BMI: 23

quotient and remainder
divisible number: 200
divisor: 65
Result of dividing 200 by 65
division: 3.076923076923077
quotient: 3
remainder: 5

the code to output the number of bacteria after 24 hours of 100 bacteria
Count of 100 bacteria after 24 hours = 1677721600
Count of 100 bacteria after 24 hours = 1677721600

Number of pencils you can buy and change
Enter the amount in ₩ 2100
number of pencils: 5
charge: 100 ₩

calculates how many slices each person eats and how many piece are left
Enter the number of people 6
Pizza order quantity: 2
Number of pizza piece: 8
available eat 2 pieces, and 4 pieces are left
compounding calculation
Total amount received after 3 years 5306040 ₩

area of circle
radius of a circle: 6.65
The area of a circle of 6.65 is 138.85865
```
