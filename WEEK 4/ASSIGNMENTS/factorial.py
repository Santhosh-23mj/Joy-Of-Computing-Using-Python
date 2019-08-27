#!/usr/bin/python3

"""
Given an integer number n, you have to print the factorial of this number. To know about factorial please click on this link.

Input Format:
A number n.

Output Format:
Print the factorial of n.

Example:
Input:
4

Output:
24 
"""

fact = 1
num = int(input())
for i in range(1,num+1):
  fact *= i
print(fact,end="")
