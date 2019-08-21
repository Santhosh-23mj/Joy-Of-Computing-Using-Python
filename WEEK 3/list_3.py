#!/usr/bin/python3

age = [1,10,20,30,44,23,43,21,23,2,13,3,11,3,5,10,12,34,22,20]

# Using sort() - to sort the list in ascending order

print("We can sort a list in ascending order using  sort()")
print("It is done as list.sort() ")
print("\nCalling sort()")
age.sort()
print("Print Sorted list")
print(age)

# using reverse() - to print the list in descending order

print("\nInorder to print a list in descending order just sort it in")
print("ascending order and reverse the elements using reverse()")
print("\nUsage is list.reverse() ",end="\n\n")
print("Calling reverse()")
age.reverse()
print("Printing list in descending order")
print(age)
