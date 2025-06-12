# Text type: str
# Numeric : int, float, complex (3+4i)
# Seq Type: List, Tuple, range
# Map Type: Dict
# Set Type: set, frozenset
# Boolean: bool

x = 10
print(x)
print(type(x))

x = "Hey!!"
x = 20456
x = 20.00
# x = 5+6j // complex
# y = 4j

x = ["Maths", "Social", "CS", "DSA"]  # list
x = ("l1", "l2", "l3")  # tuple

x = range(100, 120)

MyMap = {"Name": "Arushi", "Age": 22}  # dict

se = {"Maths", "Social", "CS", "DSA"}  # set

x = True  # Boolean
x = False

x = str(2)
x = int(78)
x = float(4)
x = complex(6j)
x = list([1, 2, 3, 4])
x = tuple((1, 2, 3, 4))

x = dict({"Name": "ZaynMalik"})
s = set({"Maths", "Social", "CS", "DSA"})

# ------------------------------------------
# Type of var
# a
# print(dtype(a))
# print(a.type))
# print(type(a))
# print(a.dtype())

# x = 5.6, 5.0. 6.856575

# x = float(5) -> 5.0

f = 5.78654323289007778797865432328900777879
print(f)  # 15 numbers after decimal

x = -3456677
print(x)

f = -2345.7899
print(f)

f1 = 68e2
print(f1)
print(type(f1))

f2 = 10E4
print(f2)
print(type(f2))

f3 = -65.5e5
print(f3)
print(type(f3))

com = (3 + 5j) + (4 + 5j)
print(com)
print(type(com))

num = 567
c = complex(num)
print(c)  # (567+0j)
print(type(c))

f = float(3.0000)
print(f)
f = float("7")
print(f)

s = str("Hi")
print(s)
s = str(6.0001)  # str
print(s)

# Random numbers

import random

print(random.random())

#  0  1  2  3   4    5       n - 1 -> indexes
# [1, 2, 3, 4, "a", "b" ..... "n"  ] -> array/list -> list1

# list1[0], list1[1], list1[2], ...... list1[len(list1) - 1]

s1 = "hey arushi!!"  # list
print(s1[1])
print(s1[4])
print(len(s1))  # len() -> length of string/list/tuple
print(s1[len(s1) - 1])
print(s1[len(s1) - 2])
print(s1[len(s1) - 3])

ss = "hey arushi!!"

for item in ss:
    if item == 'a':
        print("Yes I found a!!")
    # print(item)
    print(item, end="\n")

# len() -> Total number of items.

# Check if
# asscii a - 49, b-50,
# A - 75, B-76

text = "Hey, How yOU doing..?"
text = text.upper()
if "YOU" in text:
    print("yes found!")
else:
    print("not found")

s = "I  am from Bangalore!!"

print("I  " in s)

print(""""#####""")
txt = "I am studying computer science..!"
# key word-> not in

if "studiy" not in txt:
    print("Yesss!!!")

# Slicing:

s1 = "Hey, Welcome to my world!"

print(s1[1:])  # -> stringName[startIndex:endIndex+1] \
# default values of startIndex -> 0
# default value of lastIndex -> len(string)-1


s2 = "Hello, world!"
print(s2[-4:])

#
# "Hello world"
# d -> -1
# l -> -2
# r -> -3
# ...

s3 = "Hello, world!"
print(s3[::])

# Reverse a string in python!!
input = "Hi How are you?"

output = input[::-1]
print(output)

s1 = "HI, HOW are you?"
s2 = "Hi, how are you?"

print(s1.lower())
print(s1.upper())

t1 = "   Hello,How are you?   "
print(t1)
t1 = t1.strip()  # remove white spaces from leading and tailing end.

print(t1.replace("Howw", "WW"))


# Split:

s5 = "Hey, Welcome to my youtube channel"
print(s5.split(","))

# Formatting a string:

Age = 24
Name = "Arushi"

txt = "My name is Arushi and My Age is 23"
outputTxt = f'My name is {Name} and my age is {Age}'

areaOfRect = ""

print(outputTxt)
print("Name is", Name, "and", "My age is", Age)

price = 34.6738
priceOut = f'Final price is {price:.3f}'
print(priceOut)


# Escape char:
 # \' -> Single quote
 # \\ => Backslash
 # \n -> New Line
 # \r -> Carriage return
 # \t -> tab space
 # \b -> Backspace


print("Hello \n How are you?")
print("hi")


# upper(), lower(), split(), Strip(), replace()
# capitalise()

s = "Hiiijkkk"
print(s.capitalize())

print(s.count("i"))

print(s.find("j"))
print(s.index("j"))

s1 = "Hi345"
print(s1.isalnum())

a, b = 2, 0

print("Addition:", a+b)
print("Sub:", a-b)
if b != 0:
    print("Div ", a/b)
else:
    print("Denom shouldn't be zero!!!")
print("mul ", a*b)
print("Exp ", a**b)

# Comparsion ops

a = b = 3

if a != b:
    print("Not equal")

if a == b:
    print("Equal ops")
if 4 > 3:
     print()

if 2 < 5:
    print()

if 2 >=1:
    print()

if 1 <= 5:
    print()


# Logical oper

# AND, OR, NOT

a, b, c = 1, 2, 3

if a < b and a < c and a > 0:
    print("Heyyy!!!")
else:
    print("Noope")

# OR ops
a, b, c = 1, 2, 0

if a < b or a < c or a > 5:
    print("Heyyy-orrr!!!")
else:
    print("Noope")

# NOT

a, b = 1, 2

if not(a > b):
    print("Heyy!!")
else:
    print("Nope")


# Identity ops

# is, is not

a, b = 1, 2
if a is not b:
    print("Yes")
else:
    print("No")


# 2 * (3+5) = 16
# 2 * 3 + 5 = 11

# List
 #       0       1      2   3
l1 = ["maths", "cs", "DSA", "cs"]
print(l1)
print(type(l1))
print(l1[0])
print(l1[2])

print(len(l1))
print(l1[len(l1)-1])

l2 = [1, 2, 3, 4]
l3 = [True, False, True]
l4 = ["hi", 4, True]

# tuple
t1 = ("t1", "t2", "t3")
print(type(t1))

# converting tuple to list
l5 = list(t1)
 # ["t1", "t2", "t3"]
print(type(l5))

l5[0] = "t10"
print(l5)
print(type(l5))


t5 = tuple(l5)
print(t5)
print(type(t5))



