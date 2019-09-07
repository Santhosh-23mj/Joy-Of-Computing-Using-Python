#!/usr/bin/python3

"""
This program computes the Factorial of number 
using Recursion
"""

def factorial(n):
    if ( n == 0 ):                     # This condition is the base condition it 
        return 1                       # is very important because it breaks the recursion  
    else:
        number = factorial(n-1) * n
        return number

number = int(input("Enter the number to find factorial : "))
result = factorial(number)
print("Factorial of ",number," is ",result)