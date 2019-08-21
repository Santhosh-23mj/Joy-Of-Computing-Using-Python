#!/usr/bin/python3

shopping = ["Bread", "Butter", "Jam", "Bun"]

#Print using loop 
print("Printing using a loop")
for i in shopping:
    print(i)

print()   

#Print using print()
print("Printing using print syntax")
print(shopping)
print()

#Appending to a list using append() 
print("Appending 'Cream' to list using list.append(item)",end="\n\n")
shopping.append("Cream")

#Print after appending
print("Printing after appending")
print(shopping,end="\n\n")
for i in shopping:
    print(i)
