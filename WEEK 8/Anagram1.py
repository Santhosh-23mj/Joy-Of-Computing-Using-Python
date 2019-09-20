#!/usr/bin/python3
"""
This program tests whether a given string 
is an anagram or not by comparing the ASCII 
values 
Anagrams are words made of same characters where
order is changed eg. RAT  TAR
"""

str1 = input("Enter string 1 : ")
str2 = input("Enter string 2 : ")

str1_ascii = 0
str2_ascii = 0

if ( len(str1) == len(str2) ):
    for i in range(len(str1)):
        str1_ascii += ord(str1[i])
        str2_ascii += ord(str2[i])
else:
    print("Not Anagrams")
    exit(0)

if ( str1_ascii == str2_ascii ):
    print("Yes ! they are anagrams")
else:
    print("No ! they arent anagrams")
