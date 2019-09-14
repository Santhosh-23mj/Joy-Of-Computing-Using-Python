#!/usr/bin/python3

"""
Given a square matrix of N rows and columns, find out whether it is symmetric or not.
i.e A = transpose(A)

Input Format:
The first line of the input contains an integer number n which represents the number of rows and the number of columns.
From the second line, take n lines input with each line containing n integer elements with each element separated by a space.

Output Format:
Print 'YES' if it is symmetric otherwise 'NO'

Example:

Input:
2
1 2
2 1

Output:
YES 
"""
n = int(input())
ls = [list(map(int,input().split())) for i in range(n) ]

trans = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        trans[i][j] = ls[j][i]

count = 0

for i in range(n):
    for j in range(n):
        if ( trans[i][j] == ls[i][j] ):
            count += 1
            print(count,trans[i][j],ls[i][j])
if ( count == (n*n) ):
    print('YES')
else:
    print('NO')
