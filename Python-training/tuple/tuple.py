

t = (1, 2, 3)
print(type(t))
print(t)

l = list(t)
print(type(l))
print(l)

l[1] = "hello"
t = tuple(l)
print(type(t))
print(t)

# t[0] = "Hey"
# print(type(t))
# print(t)

print(len(t))
print(t[1])

print("last item in a tuple", t[-1])

print(t[2])
print(t[:2]) # t[leftbound:rightbound]

# leftbound -> 0
# rightbound -> len(t)

t1 = (1, 2, 3, 4, 5, 6)

if 4 in t1:
    print("found")

