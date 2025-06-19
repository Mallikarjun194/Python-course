

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


t1 = (1, 2, 3)
t2 = (6,7,1, 1, 8, "hi")

t3 = t1 + t2 + ("How", "are", "you?")
print("Resulted tuple", t3)

print(t3.count(1))
print(t3.index("are"))
print(t3.index(1))
print(t2.index(1))

isPresent= False
l2 = list(t2)
for key, item in enumerate(t2):
    if item == 1:
        print("yes found at:", key)
        isPresent = True
        break

if not isPresent:
    print("Not found:", 0)

