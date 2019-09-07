#!/usr/bin/python3
"""
This is bubble sort used to sort a given list of numbers
Each number is compared with the immediate next number if less it is swapped
and else next pair is compared and looped until the list gets sorted
"""

def bubble_sort( a ):
    
    n = len(a)
    
    for i in range(n):
        for j in range(n-i-1):
            if ( a[j] > a[j+1] ):
                a[j],a[j+1] = a[j+1],a[j]
                print(a)

a = [2, 9, 5, 4, 8, 1]
bubble_sort( a )

print(a)
