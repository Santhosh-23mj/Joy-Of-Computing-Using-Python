#!/usr/bin/python3

"""
You are given a number A which contains only digits 0's and 1's. Your task is to make all digits same by just flipping one digit (i.e. 0 to 1 or 1 to 0 ) only. If it is possible to make all the  digits same by just flipping one digit then print 'YES' else print 'NO'.

Input Format:
The first line contains a number made up of 0's and 1's.

Output Format:
Print 'YES' or 'NO' accordingly without quotes.

Example:
Input:
101

Output:
YES
"""
num = list(input())
zero = num.count('0')
one = num.count('1')
if ( zero == 1 or one ==1 ):
    print("YES",end="")
else:
    print("NO",end="")
