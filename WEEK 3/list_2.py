#!/usr/bin/python3

shopping = ["Bread", "Butter", "Jam", "Bun"]
shopping.append("Cream")

#Printing list using indices
print("Printing list using indices : ")
for i in range(len(shopping)):
    print("Element @ shopping[",i,"] = ",shopping[i])
print()

#Insering elements into the list
print("Append() - appends elements at last. To insert at specific position use insert()",end="\n\n")
print("Using insert() - list.insert(index,element)",end="\n\n")

shopping.insert(1,"Oil")

print("Printing after inserting 'Oil' : ")
for i in shopping:
    print(i)
print()
# Using count() to determine no.of specific element in the list
# Creating new list 
age = [10,20,30,44,23,43,21,23,2,13,3,11,3]

#Using len() to get length of list
print("The len() - returns the total no.of elements in list")
print("Printing length using len(list)")
print(len(age))
print()
print("The count() is used to count how many specified elements are there in the list")
print("Usage : list.count(value to count)",end="\n\n")
print("Counting 3 in age[]",age.count(3))
print("Counting unavailable element in age[]",age.count(100))