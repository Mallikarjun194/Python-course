


# list, tuple, sets and dict

d1 = {
    "Name": "Arushi",
    "Age": 24,
    "Class": "2nd sem"
}

print(d1)
print(type(d1))

print(d1["Name"])

d1["Age"] = 25
print(d1)

d2 = {
    "Name": "abc",
    "year": 2025,
    "year": 2026
}
print(d2)
d2["year"] = 2
print(d2)

print(len(d2))

d2["marks"] = 35
print(d2)
print(len(d2))

d3 = {
    "Name": "xyz",
    "isAvailable": False,
    "year": 2022,
    "marks": [35, 67, 89]
}

print(d3)

# Constructor
# list(), tuple(), dict()

d5 = dict(empID = 123, empName = "xyz")
print(d5)
print(type(d5))

print(d5["empID"])
print(d5.get("empID"))

d4 = {"x": 1, "y": 2, "z": 3, "a": 7, "b": 9}

print(d4.keys())
print(d4.values())

print(d4.items())
print(d4.items().mapping)

if "y1" in d4:
    print("yes")
else:
    print("not")

d4["z"] = 30
print(d4)

d4.update({"z": 100, "z2": 4})
print(d4)
print(d4.pop("z2")) # value of z2 it returns

print(d4)

d4.popitem() # deletes last item from dict
print(d4)

d4.popitem()
print(d4)

d4.popitem()
print(d4)

d11 = {
    1: 1, 2: 3, 3: 5, 5: 6
}

d11["hello"] = 5
# {
#     1: 1, 2: 3, 3: 5, 5: 6, "hello": 5
# }
d11["hi"] = "hru?"
# {
#     1: 1, 2: 3, 3: 5, 5: 6, "hello": 5, "hi":"hru?"
# }

d11.update({"hello": 23, "g": 67})
# {
#     1: 1, 2: 3, 3: 5, 5: 6, "hello": 23, "hi":"hru?", "g" 67
# }
d11.popitem()
# {
#     1: 1, 2: 3, 3: 5, 5: 6, "hello": 23, "hi":"hru?"
# }
d11.popitem()
# {
#     1: 1, 2: 3, 3: 5, 5: 6, "hello": 23,
# }

d11.pop(1)
# {
#    2: 3, 3: 5, 5: 6, "hello": 23
# }

# del -> delete a whole dict
# clear()
print(d11)

# Loop over dict:


dl = {"Name": "xyz", "Age": 25, "marks": 88, "Rno": 234}

for item in dl:
    print(item, ":", dl[item])

for item in dl.keys():
    print(item)

for item in dl.values():
    print(item)

for keys, _ in dl.items():
    print(keys)

for keys, values in dl.items():
    print(keys, values)

# Copying

newD = dl.copy()
print(newD)

newDd = dict(dl)
print(newDd)



data = {
    "std1": { "Name": "Arun", "Age": 25, "marks": 67},
    "std2": {"Name": "Arushi", "Age": 25, "marks": 68},
    "std3": {"Name": "Harshitha", "Age": 25, "marks": 60}
}

print(len(data))
print(type(data))
print(data)

data["std1"]["marks"] = 65
print(data)

data["std1"]["english marks"] = 65
print(data)

print(data["std2"]["Name"])
print(data["std2"])

for key, d in data.items():
    print("Student #####", key)
    for k, v in d.items():
        print(k, v)


# Methods -> keys(). values(), copy(), items(), dict(), pop(), popitem(), get(), update()

