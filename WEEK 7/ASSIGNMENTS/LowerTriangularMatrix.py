#!/usr/bin/python3

"""
Write a program to convert a square matrix into a lower triangular matrix.

Input Format:
The first line of the input contains an integer number n which represents the 
number of rows and the number of columns.
From the second line, take n lines input with each line containing n integer elements. 
Elements are separated by space.

Output format:
Print the elements of the matrix with each row in a 
new line and each element separated by a space.

Example 1:
Input:
3
1 2 3
4 5 6
7 8 9

Output:
1 0 0
4 5 0
7 8 9
  
n = int(input())
ls = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        if ( i < j ):
            print('0',end=" ")
        else:
            print(ls[i][j],end=" ")
    print()
    

"""

n=int(input());
a=[list(map(int,input().split())) for i in range(n)];
for i in range(n):
  for j in range(n):
    end = '' if j == n-1 else ' ';
    if(i<j):
      print(0, end=end);
    else:
      print(a[i][j], end=end);
  end = '' if i == n-1 else '\n';
  print('',end=end);
    