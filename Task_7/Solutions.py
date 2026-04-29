# Problem 1
class Animal:
    def speak(self):
        print("sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

x = Dog()
x.speak()


# Problem 2
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def count_students(self):
        print(len(self.students))

c = Classroom()
c.add_student("Arwa")
c.add_student("Nassar")
c.count_students()


# Problem 3
class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self):
        self.passengers = []

    def add_passenger(self, p):
        self.passengers.append(p)

f = Flight()
f.add_passenger(Passenger("Arwa"))
f.add_passenger(Passenger("Nassar"))

print(len(f.passengers))


# Problem 4
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Team:
    def __init__(self):
        self.members = []

    def add_player(self, p):
        self.members.append(p)

t = Team()
t.add_player(Player("Arwa", 5))
t.add_player(Player("Nassar", 7))

print(len(t.members))


# Problem 5
class Shape:
    def area(self):
        pass

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Square:
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s * self.s

def print_area(x):
    print(x.area())

c = Circle(5)
s = Square(4)

print_area(c)
print_area(s)
