#!/usr/bin/python3

"""
This program computes the factorial of a given number 
using a loop
"""

def factorial(number):
    
    result = 1
    
    for i in range(1,number+1):
        result *= i
    
    return result

while (1):
    number = int(input("Enter a number to find factorial : "))
    if ( number > 0 ):
        result = factorial(number)
        break
    else:
        print("Enter a positive number !!")

print("The factorial of ",number," is ",result)