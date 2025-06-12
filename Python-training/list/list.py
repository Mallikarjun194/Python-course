l1 = [1, 2, 3, 4]
print(len(l1))
print(type(l1))

print(l1[0])

l1[0] = "Hey"
print(l1)

l1[1:3] = ["two", "three"]  # ['Hey', 'two', 'three', 4]

print(l1)

l1[1:2] = ["two", "three"]  # ['Hey', 'two', 'three', 3, 4]
print(l1)

list1 = ["Maths", "CS", "DSA"]
list1.insert(1, "OOPs")  # 1st index = 2nd position.
# ['Maths', 'OOPs', 'CS', 'DSA']
#   0          1    2      3
print(list1)

list1.insert(4, "Networking")
list1.insert(len(list1), "Xyz")
print(list1)
print(list1[len(list1) - 1])  # last item in a list

list1.append(12)  # Add item at last
print(list1)

# extend

list2 = ["abc", "xyz", "tyu"]
list3 = [2, 3]
list2.extend(list3)
print(list2)
print(list3)

listOne = [1, 2, 3, 4]
tupleOne = ("one", "two", "three")
listOne.extend(tupleOne)
print(listOne)

list2 = ["abc", "xyz", "tyu"]
list3 = [2, 3]
list2.extend(["fg", "bg"])
print(list2)

# Remove:

l1 = [1, 2, 3, 4]
print(len(l1))
l1.remove(3)
print(len(l1))
print(l1)

l1 = ["a", "b", "a", "c", "d"]
l1.remove("a")
print(l1)

l1.remove("a")
print(l1)

# l1.remove("5") # gives ValueError
# print(l1)

# pop() method

removeListItemFromSpecificIndex = ["a", "b", "a", "c", "d"]

removeListItemFromSpecificIndex.pop(3)  # removes item from 3rd index ie c
print(removeListItemFromSpecificIndex)

removeListItemFromSpecificIndex1 = ["a", "b", "a", "c", "d"]

removeListItemFromSpecificIndex1.pop()  # removes item from end of a list
print(removeListItemFromSpecificIndex1)

# del keyword

usingDel = [1, 2, 3, 4]
del usingDel[2]
print(usingDel)

# del usingDel # delete an entire list

# clear() method

clearList = [1, 2, 3]
print(len(clearList))
# 3
clearList.clear()
# del clearList
print(len(clearList))  # 0

print(clearList)

# clear --> {1000} -> [1, 2, 3, 4] -> [] -> clear
# del --> {}

loopList = [1, 2, 3, 4, 2, 5]

for item in loopList:
    if item == 2:
        print("Arushi!!")
    else:
        print(item)

# item = 1 , 1 == 2 -> No, print 1
# item = 2, 2 == 2 --> yes, print "Arushi"
# item = 3, 3== 2 --> No,  print 3
# item = 4, 4 == 2 --> F, print 4
# item = 2, 2 == 2, --> T, print "Arushi"
# ...
print("$$$$$$$$$$$$$$$$$$$$$$$$")
loopList = [1, 2, 3, 4, 2, 5]

for item in loopList:
    if item == 2:
        print("Arushi!!")

    print(item)

# item = 1, 1 == 2, F -> print 1
# item = 2, 2 == 2, T --> Print "Arushi", print 2
# item = 3,  3 == 2, F -> print 3

print("&&&&&")
# range
       #    0  1  2  3  4  5  6
loopList = [1, 2, 3, 4, 2, 5, 8]

for index in range(0, len(loopList), 1):
    print(index, loopList[index])


# While:
    #  0    1     2    3
l1 = ["a", "b", "c", "d"]

# initialise
# condition
# increment/decrement

index = 0
l = len(l1)
print("Length:", l)
while index < l:
    item = l1[index]
    print("item is;", item)
    if item == "c":
        print("Arushi!")
    else:
        print("Not found!!!")

    index += 1
    print("index is: ", index)
    # index = index + 1
print("Finished!")

# List comprehension

# fill the list from numbers 1-10.

# l = [1, 2, 3, 4, 5, 6 ..10]
#
l = []
for i in range(1, 101):
    l.append(i)

print(l)

l1 = []
index = 0

while index < 100:
    l1.append(index+1)
    if index == 5:
        index = 98
    else:
        index += 1

print(l1)

# l = [1, 2, 3, 4]
print([i for i in range(1, 11)])
print([i for i in range(1, 11) if i %2 == 0])

# syntax -> [ expression for item in iterable if condition == true ]
print([i+25 for i in range(1, 11) if i %2 == 0])

print(["even" if i%2 == 0 else "odd" for i in range(1, 11)])


#########################################################################33

l = [7, 8, 3, 4, 1, -4]
l.sort() # Ascending
print(l)

print("sort in reverse order:")
l.sort(reverse=True) # Descending
print(l)

list1 = ["hi","Anusha", "bye","Arushi","oye"]
list1.sort()
print(list1)

# case in_senstive

l = ["banglore", "Odissa", "Kerala", "China", "Abc"]

l.sort(key=str.lower)
print(l)

# Reverse a list:
l = [7, 5, 4, 3, 5, 8]
print("Reversed list:", l[::-1])

l.reverse()
print(l)

# copy list
new_list = l
print("new_list", new_list)

new_list1 = l.copy()
print("copied list:", new_list1)

new_list2 = list([1, 2, 3])
print("new list:", new_list2)

print(l[:])

# Join List

l1 = ["x", "y", "z"]
l2 = [3, 4, 5]

l3 = l1 + l2
# l1.extend(l2)
# print(l1)
print(l3)

