

d1 = {"a": 10, "b": 20}
d2 = {"b": 30, "c": 20, 'e': 45}

# o/p: {"a": 10, "b": 50, "c": 20, 'e': 45}

d3 = {}

for key, value in d1.items():
    if key in d2:
        d3[key] = d1[key] + d2[key] # d3[b] = 20 + 30 = 50 -> d3  = {a: 10, b: 50}
    else:
        d3[key] = value # d3 = {a: 10}

print(d3)

for key, value in d2.items():
    if key not in d3:
        d3[key] = value # d3 -> {a: 10, b: 50, c" 20}, d3 -> {a: 10, b: 50, c:20, e:45}

print(d3)

# student

std = {"a1": -395, "b1": 67, "c1": 89, "d1": 86}
maxMarks = 0
studentName = ""

for key, value in std.items():
    if value > maxMarks:
        maxMarks = value
        studentName = key
        # a1, -395 > 0 -> false
        # b1, 67 > 0 -> true -> maxMarks=67, studentName=b1
        # c1, 89 > 67 -> true -> maxMarks = 89, studentName = c1
        # d1, 86 > 89 -> false


print("Student name ", studentName, "whose marks is", maxMarks)
