#!/usr/bin/python3

"""
You are provided with the number of rows (R) and columns (C). Your task is to generate the matrix having R rows and C columns such that all the numbers are in increasing order starting from 1 in row wise manner.

Input Format:
The first line contain two numbers R and C separated by a space.

Output Format:
Print the elements of the matrix with each row in a new line and elements of each row are separated by a space.

NOTE: There should not be any space after the last element of each row and no new line after the last row.

Example:
Input:
3 3

Output:
1 2 3
4 5 6
7 8 9
"""

m,n = map(int,input().split())
num = 1
for i in range(m):
  for j in range(n-1):
    print(num,end=" ")
    num += 1
  if ( num == m*n ):
    print(num,end="")
  else:
    print(num)
    num += 1

