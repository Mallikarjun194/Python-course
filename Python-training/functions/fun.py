

def AreaOfSquare(side):
    area = side * side
    print("Area of square is :", area)

def AreaOfRect(l, b):
    print("Area of rect:", l*b)

def GreetFun():
    print("Hello, HRU?")


def SumOfList(l):
    s = 0
    for item in l:
        s += item
    print("Sum of list", s)



AreaOfSquare(2)
AreaOfSquare(5)
AreaOfRect(2, 3)
GreetFun()
SumOfList([1, 2, 3, 4, 5])


# return function

def multiply(x):
    return x*x


m = multiply(4)
print("multiply of num",4 ," is:",m)


print("multiply result:", multiply(5))


