#!/usr/bin/python3

"""
Given an integer number n, define a function named printDict() which can print a dictionary where the keys are numbers between 1 and n (both included) and the values are square of keys.
The function printDict() doesn't take any argument.

Input Format:
The first line contains the number n.

Output Format:
Print the dictionary in one line.

Example:
Input:
5

Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

n = int(input())

def printDict():
  dictionary = {}
  for i in range(1,n+1):
    dictionary[i] = i*i
  print(dictionary,end='')

printDict()