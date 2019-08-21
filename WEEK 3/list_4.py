#!/usr/bin/python3

# Slicing to reduce the list 
# Just use list[start:end+1]
# If none is specified default start and 
# end is taken 
# start = 0
# end = len(list)

age = [1,10,20,30,44,23,43,21,23,2,13,3,11,3,5,10,12,34,22,20]

age.sort()
print("Printing the list in ascending order : ")
for i in range(len(age)):
    print(i)
print()

print("Slicing list using age[:] - Using default values :")
print(age[:],end="\n\n")

print("Slicing the list using age[3:] - from 3 to len(list)")
print(age[3:],end="\n\n")

print("Slicing the list using age[:4] - from 0 to 4")
print(age[:4],end="\n\n")

print("Slicing list using age[3:11] - from 3 to 10")
print(age[3:11])
