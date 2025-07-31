

# var1 == var2
# var1 != var2  2 != 3 -> true 2 != 2 -> False
# var1 > var2
# var1 < var2
# var1 >= var2
# var1 <= var2

a = 34
b = 45

if b > a:
    print("b greater than a")
else:
    print("a > b")

side1 = 5
side2 = 5

if side1 != side2:
    print("Area of rect:", side1*side2)
elif side1 == side2:
    print("Area of square:", side1*side1)
else:
    print("Default values")

if side1>=side2: print("side1 > side2")


############################################################

# and keyword

a = 100
b = 200
c = 300

if b > a and c > a:
    print("b and c are greater than a")
else:
    print("b and c are not greater than a")


#####################################
a = 250
b = 200
c = 300

if b > a and c > a:
    print("b and c are greater than a")
else:
    print("b and c are not greater than a")

# ----------------------------------------------------------
# or condition

a = 250
b = 200
c = 300

if b > a or c > a:
    print("b and c are greater than a")
else:
    print("b and c are not greater than a")

# ---------------------------------------------------------------------
a = 350
b = 200
c = 300

if b > a or c > a:
    print("b and c are greater than a")
else:
    print("b and c are not greater than a")

#-------------------------------------------------------------

# not keyword

a = 100
b = 200

if not b > a:
    print("Hello")
else:
    print("hi")

a = 300
b = 200

if not b > a:
    print("Hello!!!!")
else:
    print("hii!!!")


# nested if

n = 100


if n > 10:
    print("n is", n)

    if n +10 < 1000:
        print("Hey Yes!!")
    else:
        print("NO")

# n is always a +ve integer, if not print -1
# if n is even, then perform n*n
# if n is ood, perform n+n

n = 15

if n < 1:
    print(-1)
else:
    if n % 2 == 0:
        print(n,"*",n, "is:", n*n)
    else:
        print(n, "+", n, "is:", n+n)

#####

# syntax:

# /*
# match exp:
#     case "A":
#         print("a")
#     case "B":
#         print("b")
#     case "C":
#         print("c")
#     case "D":
#         print("d")
#
# */


day = 6

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wed")
    case 4:
        print("Thur")
    case 5:
        print("Fri")
    case _:
        print("Weekend")


##### while

i = 1

while i < 5:
    print(i+1)
    i+=1

# 1 < 5 -> True -> print(1+1) -> 2
# 2 < 5 -> True -> print(2+1) -> 3
# 3 < 5 -> T -> 4
# 4 < 5 -> T -> 5
# 5 < 5 -> False


# break, continue

i = 1

while i < 10:
    print(i)
    if i == 5:
        break
    i += 1 # i = i + 1

# 1 < 10 -> True -> 1
# 2 < 10 -> T -> 2
# 3 < 10 -> T -> 3
# 4 < 10 -> T -> 4
# 5 < 10 -> T -> 5  -> 5 == 5 -> True -> Break the while loop

print("######################## continue #####################################")
i = 1

while i < 10:
    i += 1
    if i == 5:
        print("i is->", i)
        continue


    print(i)


# 1 < 10 -> True -> 2
# 2 < 10 -> T -> 3
# 3 < 10 -> T -> 4
# 4 < 10 -> T -> 5
# 5 < 10 -> T -> 5  -> 5 == 5 -> True




