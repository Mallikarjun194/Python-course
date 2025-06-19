

s1 = { "s1", "s2", "s3", "s1", "s5"}
print(s1)

s2 = { "a", "b", "c", True, 1 , 2, 0, False}
# 1 -> True
# 0 -> False
print(s2)

l = len(s2)
print(l)
print(type(s2))

l = [1, 2, 3, 1, 2, 5, 6, 7, 5]
print(len(l))
print(type(l))

s3 = set(l)
print(len(s3))
print(s3) # {1, 2, 3, 5, 6, 7}

print(list(s3))

for item in s2:
    print(item)

#check if soething present in a set

print("b1" in s2)
print(1 in l)
# if 2 < 6 ->


s5 = {1, 2, 3, 4}
s5.add("yu")
s5.add(1)
print(s5)

s11 = {1, 2, 3}
s22 = {2, 6, 7}
s11.update(s22)
print(s11)
print(s22)

# {1, 2, 3, 6, 7}
s22.update(s11)
print(s22)

s22.remove(1)
print(s22)

s22.discard(2)
print(s22)

print(s22.pop())
print(s22)

s22.clear()
print(s22)

del s22
# print(s22)

# Join

s1 = {1, 2, 3, "b"}
s2 = {"a", "b", "c", 1, 2}

s3 = s1.union(s2)
print(s3)

s4 = s1.intersection(s2)
print(s4)

# s7 = s4 + [678]
# give error
s8 = s4.union([678])
# print(s7)
print(s8)

ss1 = {1, 2, 3, 4}
ss2 = {3, 4, 5}

ss3 = ss1 & ss2
print(ss3)

# ss4 = ss1 & [3, 4, 5]
# print(ss4)

ss4 = ss1.intersection([3, 4, 5])
print(ss4)


ssd1 = {"a", "b", "c"}
ssd2 = {"g", "m", "a"}

ssd3 = ssd1.difference(ssd2)
print(ssd3)

ssd4 = ssd2.difference(ssd1)
print(ssd4)

# try achiveing set diff using - operator.







