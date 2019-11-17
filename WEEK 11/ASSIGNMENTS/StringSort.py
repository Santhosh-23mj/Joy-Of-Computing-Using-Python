#!/usr/bin/python3

"""
Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Input Format:
The first line of input contains words separated by the comma.

Output Format:
Print the sorted words separated by the comma.

Example:

Input:
without,hello,bag,world

Output:
bag,hello,without,world 
"""

ls = input().split(',')
ls.sort()
for i in range(len(ls)-1):
  print(ls[i],end="")
  print(",",end="")
print(ls[len(ls)-1],end="")
