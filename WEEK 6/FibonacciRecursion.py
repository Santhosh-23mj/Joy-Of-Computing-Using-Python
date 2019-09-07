#!/usr/bin/python3

"""
This program is the application of Recursion
It computes the nth Fibonacci Number
"""

def Fibonacci(n):
    if ( n == 0 or n == 1 ):
        return n
    else:
        return Fibonacci(n-2)+Fibonacci(n-1)

while (1):
    num = int(input("Enter a number : "))
    if ( num > 0 ):
        break
    else:
        print("Enter a positive number !")

result = Fibonacci(num)
print(num,"th fibonacci number is ",result)