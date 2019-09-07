#!/usr/bin/python3
"""
This Program implements linear search
search an sorted list from 0 till n in order
but it is inefficient when the list is large
"""

def linear_search( ls,search ):
    
    count = 0
    for i in ls:
        count += 1
        if ( i == search ):
            print("Found the element @ index : ",i," in ",count," iterations")
            break

ls = []
for i in range(1001):
    ls.append(i)

search = int(input("Enter number to search : "))

linear_search(ls,search)