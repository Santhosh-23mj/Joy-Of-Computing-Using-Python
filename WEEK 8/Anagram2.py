#!/usr/bin/python3
"""
This program also checks whether a given two strings are anagrams
or not with a different logic that involves sorting the list
"""

str1 = input("Enter the String 1 : ")
str2 = input("Enter the String 2 : ")

if ( sorted(str1) == sorted(str2) ):
    print("Yes ! they are anagrams")
else:
    print("No ! they arent anagrams")

"""
There are many params that can be passed to sorted()
sorted(list,Reverse=True) - Sorts list in descending order
sorted(list,key=len)      - Sorts list based on length of chars stored
sorted(dict)              - Sotrs dictionary based on 'key' not the values
"""