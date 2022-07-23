# A class that stores the name of each student and their Korean, English, and math scores as a constructor
# Method that returns the sum and average of students' scores from the previous exercise
print('student score')
class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

    def getSum(self):
        sum = self.korean + self.english + self.math
        return sum

    def getAvg(self):
        avg = self.getSum() / 3
        return avg

students = [Student("Anthoy", 65, 70, 95),
            Student("David", 55, 45, 70),
            Student("Paul", 90, 70, 85),
            Student("James", 85, 60, 80)
            ]

for student in students:
    print(student.name, student.korean, student.english, student.math)
    print('Total score: ', student.getSum())
    print('Average: ', student.getAvg())
print()

# A class that manages incoming and outgoing inventory with the name, price, and inventory of the product as the creator.
print('stationery inventory management')
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = 0

    def storing(self, amount):
        self.stock += amount

    def unstoring(self, amount):
        self.stock -= amount

    def getPrice(self):
        return self.price

    def getStock(self):
        return self.stock

pencil = Product("pencil", 1000)
eraser = Product("eraser", 500)
ruler = Product("ruler", 1500)
note = Product("note", 2000)

pencil.storing(100)
eraser.storing(20)
ruler.storing(50)
pencil.unstoring(70)
eraser.unstoring(10)

print('pencil price: ', pencil.getPrice())
print('eraser price: ', eraser.getPrice())
print('ruler price: ', ruler.getPrice())
print('note price: ', note.getPrice())
print()

print('pencil stock: ', pencil.getStock())
print('eraser stock: ', eraser.getStock())
print('ruler stock: ', ruler.getStock())
print('note stock: ', note.getStock())