#!/usr/bin/python3

"""
This program implements the binary search. This is very much efficient than
the linear search. Notice the no.of iterations taken in both searching methods
"""

def Binary_Search( ls, search ):
    last  = len(ls)-1
    first = 0
    count = 0
    
    while ( first <= last ):
        
        mid = (first+last)//2
        count += 1
        
        if ( ls[mid] == search ):
            print("Element found @ ",mid," in ",count," iterations")
            break
        else:
            if ( ls[mid] < search ):
                first = mid+1
            elif ( ls[mid] > search ):
                last = mid-1

ls = []
for i in range(1001):
    ls.append(i)

search = int(input("Enter the number to search : "))

Binary_Search( ls, search )