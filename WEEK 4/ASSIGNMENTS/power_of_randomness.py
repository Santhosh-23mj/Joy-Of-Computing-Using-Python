#!/usr/bin/python3

"""
You all have used the random library of python. You have seen in the screen-cast of how powerful it is.
In this assignment, you will sort a list let's say list_1 of numbers in increasing order using the random library.

Following are the steps to sort the numbers using the random library.

Step 1: Import the randint definition of the random library of python. Check this page if you want some help.
Step 2: Take the elements of the list_1 as input.
Step 3: randomly choose two indexes i and j within the range of the size of list_1.
Step 4: Swap the elements present at the indexes i and j. After doing this, check whether the list_1 is sorted or not.
Step 5: Repeat step 3 and 4 until the array is not sorted.

Input Format:
The first line contains a single number n which signifies the number of elements in the list_1.
From the second line, the elements of the list_1 are given with each number in a new line.

Output Format:
Print the elements of the list_1 in a single line with each element separated by a space. 
NOTE 1: There should not be any space after the last element.

Example:

Input:
4
3
1
2
5

Output:
1 2 3 5

"""

from random import randint

def issort(ls):
  for i in range(1,n):
    if( ls[i-1] > ls[i] ):
      return False
  return True

n = int(input())
ls = []
for i in range(n):
  ls.append(int(input()))
while(not issort(ls)):
  i = randint(0,n-1)
  j = randint(0,n-1)
  ls[i],ls[j] = ls[j],ls[i]
for i in range(n-1):
  print(ls[i],end=" ")
print(ls[n-1],end="")

