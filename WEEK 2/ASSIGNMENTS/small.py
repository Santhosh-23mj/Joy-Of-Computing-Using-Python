#!/usr/bin/python3

"""
Given two numbers (integers) as input, print the smaller number.

Input Format:
The first line of input contains two numbers separated by a space

Output Format:
Print the smaller number

Example:
Input:
2 3
Output:
2 
"""

num1,num2 = input().split(' ')
num1 = int(num1)
num2 = int(num2)

if ( num1 < num2 ):
    print(num1,end="")
else:
    print(num2,end="")
