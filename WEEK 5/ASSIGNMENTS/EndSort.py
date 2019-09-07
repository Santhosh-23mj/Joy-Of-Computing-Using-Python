#!/usr/bin/python3
"""
Given a list A of N distinct integer numbers, you can sort the list by moving an element to the end of the list. Find the minimum number of moves required to sort the list using this method in ascending order. 

Input Format:
The first line of the input contains N distinct integers of list A separated by a space.

Output Format
Print the minimum number of moves required to sort the elements.

Example:

Input:
1 3 2 4 5

Output:
3
"""

def endsort(a): 
  sa = sorted(a) 
  n = len(a)
  k = 0
  for i in range(n):
    try:
      k = a.index(sa[i], k)+1 
    except ValueError:
      break 
  else:
    i += 1;
  return n-i;

print(endsort(list(map(int, input().split()))),end="");