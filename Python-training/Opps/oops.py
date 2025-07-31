

class Class1:
    xyz = 15

obj1 = Class1()
print(obj1.xyz)


class Car:
    len = 2
    wid = 15
    noOfSeats = 5

volvo = Car()
print(volvo.len, volvo.noOfSeats)

bmw = Car()
print(bmw.len, bmw.wid)


class Cars:
    def __init__(self, colour, model):
        self.colour = colour
        self.model = model

benz = Cars("black", 2025)
print(benz.model, benz.colour)

hyndai = Cars("white", 2020)
print(hyndai.model)


class Fruits:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def printNameOfFruit(self):
        return self.name

    def printColourOfFruit(self):
        return self.colour

apple = Fruits("apple", "red")
print("name:", apple.printNameOfFruit())
print("color:", apple.printColourOfFruit())

# 1. class, 2.object

# 3. Inheritance:

# Base class/Parent class
class Person:
    def __init__(self, FName, LName):
        self.FName = FName
        self.LName = LName

    def printName(self):
        print(self.FName, self.LName)

p1 = Person("John", "Cena")
p1.printName()


# Child class/Derived class
class Child(Person):
    # def __init__(self, name):
    #     self.name = name

    def PrintNameAndParentName(self):
        print(self.FName, self.LName)


# p1 = Person("John", "one")
c1 = Child("John", "one")
c1.PrintNameAndParentName()



class Base:
    def __init__(self, FName, LName):
        self.FName = FName
        self.LName = LName

    def printName(self):
        print(self.FName, self.LName)

p1 = Person("John", "Cena")
p1.printName()


# Child class/Derived class
class Derived(Base):
    def __init__(self, FName, LName):
        Base.__init__(self, FName, LName)

    def PrintNameAndParentName(self):
        print(self.FName, self.LName)


d = Derived("Arushi", "Sharma")
d.PrintNameAndParentName()




class Base1:
    def __init__(self, FName, LName):
        self.FName = FName
        self.LName = LName

    def printName(self):
        print(self.FName, self.LName)

p1 = Person("John", "Cena")
p1.printName()


# Child class/Derived class
class Derived1(Base1):
    def __init__(self, FName, LName, year):
        super().__init__(FName, LName)
        self.year = year

    def PrintNameAndParentName(self):
        print(self.FName, self.LName, self.year)

    def printYear(self):
        print(self.year)


d1 = Derived1("Arushi", "Sharma", 2025)
d1.PrintNameAndParentName()
d1.printYear()


# Polymorphism:

num1 = 3
num2 = 4
print(num2+num1)

s1 = "arushi "
s2 = "sharma"
print(s1+s2)


class A:
    def __init__(self, brand, col):
        self.brand = brand
        self.col = col

    def move(self):
        print("Drive!!!!!")


class B:
    def __init__(self, brand, col):
        self.brand = brand
        self.col = col

    def move(self):
        print("Stop!!!!!")


c1 = A("Ford", "White")
b1 = B("Benz", "black")

for obj in [c1, b1]:
    obj.move()


# Scope


x = 5 #Global var

def print1():

    x = 10
    y = 6 # local variable -> can be accessed only withing a function
    print(x, y)



print1()
print(x)


def f1():

    z = 67
    def innerFun():
        z = 69
        print(z)
    innerFun()


f1()

