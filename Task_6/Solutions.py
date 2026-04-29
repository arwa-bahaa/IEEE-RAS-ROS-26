# Problem 1
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof! My name is", self.name)


d1 = Dog("Max", "Husky")
d1.bark()

# Problem 2
class Calculator:

    def add(self, a, b):
        print(a + b)

    def subtract(self, a, b):
        print(a - b)

    def multiply(self, a, b):
        print(a * b)

c = Calculator()

c.add(5, 3)
c.subtract(8, 2)
c.multiply(4, 6)

# Problem 3
class BankAccount:
    balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Balance =", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Balance =", self.balance)


acc = BankAccount()

acc.deposit(500)
acc.withdraw(200)

# Problem 4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


r1 = Rectangle(5, 4)

print("Area =", r1.get_area())

# Problem 5
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow_book(self):
        if self.is_available == True:
            self.is_available = False
            print("Book borrowed")
        else:
            print("Already out")

b = Book("Harry Potter", "Arwa")

b.borrow_book()
b.borrow_book()









