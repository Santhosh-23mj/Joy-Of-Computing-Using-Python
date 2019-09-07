#!/usr/bin/python3

"""
This is an application of recursion
Recursion is implemented in the binary search

it takes a list,element to search,starting and ending index
and returns the index of the search element
"""

def Binary_Search( ls,search,start,end ):
    
    if ( start == end ):              # Base case to break the recursion
        if( ls[start] == search ):
            return start
        else:
            return -1
    
    mid = (start + end)//2
    
    if ( ls[mid] == search ):         # Using sorted list to traverse through
        return search
    elif( ls[mid] > search ):
        return (Binary_Search( ls,search,start,mid-1 ))
    else:
        return (Binary_Search( ls,search,mid+1,end ))

ls = []
for i in range(20):
    ls.append(i)
find = int(input("Enter a number to find : "))
start = 0
end = len(ls)-1

print("Remember indexing starts from 0")
element = Binary_Search(ls,find,start,end)
if ( element == -1 ):
    print(find," is not found !")
else:
    print(find,"is @ ",element)
    