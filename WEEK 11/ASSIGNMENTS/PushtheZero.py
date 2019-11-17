#!/usr/bin/python3

"""
 Write a Python program to push all zeros to the end of a given list a. The order of the elements should not change.

Input Format:
Elements of the list a with each element separated by a space.

Output Format:
Elements of the modified list with each element separated by a space. After the last element, there should not be any space.

Example:

Input:
0 2 3 4 6 7 10

Output:
2 3 4 6 7 10 0

Explanation:
There is one zero in the list. After pushing it at the end the elements of the list becomes 2 3 4 6 7 10 0. The order of other
elements remains the same. 
"""

ls = input().split()
for i in range(len(ls)):
    if(ls[i] == '0'):
        ls.remove(ls[i])
        ls.append(0)
for i in range(len(ls)-1):
  print(ls[i],end=" ")
print(ls[len(ls)-1],end="")
