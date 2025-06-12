# var abc int = 5

x = 5
y = "john"  # str
print(y)
y = 15  # int
print(y)
y = False
print(x)
print(y)

# Casting

a = str("4")
print(a)

# two inputs: a, b int
# fun -> (a, b int)
# '2', '3'

# a = int(input1) = 2, b=int(input2) = 3

b = int(3)
z = float(3)  # decimal
print(b)
print(z)

# type

print(type(a))
print(type(b))
print(type(z))

a = int(a)
print(type(a))

xyz = "Hi Hello, How are you??"
abc = 'Hi-iii'
abcd = """How are you??"""
y = '''Hi'''

print(xyz)
print(abc)
print(abcd)
print(y)

print(type(xyz))
print(type(abc))
print(type(abcd))
print(type(y))

# Case sensitive:

S = "Hey Arushi, How are you?"
s = "Heyy, I'm Good!!"
S = 123
print(S, s)

# Rules of creating a variable:

# 1. Variable name must start with letter or an underscore.
# _Abc
# _abc
# _ABC
# _abc
# abc
# ABC
# Abc
# cAb

# 2. Variable name cannot start with number

A1b1c111 = "adf"
_1bc = "7575"

# 3. A variable name can only contain alphanumeric and under-score(A-z, 0-9, _)

S1_ = "adf"
_1F = "shd"
_abc_ = "sjhdj"

# abc$ = "wjhdhjd"  -> illegal

# 4. Variable names are case sensitive (xyz, Xyz, XYZ, xyZ are all treated as different variables)
S = "Hey Arushi, How are you?"
s = "Heyy, I'm Good!!"
S = 123
print(S, s)

# 5. Variable name cannot be keywords

# if, else, in, not -> keywords

# if = "234" -> illegal

# Multiple values to multiple variables
i, j, k = 2, 3, 4
print(i, j, k)

# single value to multiple variables
t = y = o = "Zayn!!"
print(t, y, o)

# Unpacking a list
subjects = ["maths", "Cs", "DSA", "SS"]

m, c, d, ss = subjects
print(m)
print(c)
print(d)
print(ss, m, c, d)

# concat string
st = "Random"
ft = "Number"

print(st + " " + ft)

n1 = 9
n2 = 6
n1 = str(n1)
n2 = str(n2)
print(n1 + n2)

xi = 45  # global variables

# xi -> 45

def fun123():
    jk = "34"
    xi = 5  # local variables # xi -> 45 -> 5
    print("My fun->", xi)
    print(jk)


print(xi)  # 45
fun123() # 5
print(xi)  # 45
# print(jk)
