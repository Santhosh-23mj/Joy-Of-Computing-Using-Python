#!/usr/bin/python3

"""
This program demonstrates the right way to code a FizzBuzz game
and also the use of functions 
"""

def fizzBuzz(r):
    for i in range(1,(r+1)):
        if ( (i % 3 == 0) and (i % 5 == 0) ):
            print(str(i)+" = FizzBuzz")
        elif ( i % 3 == 0 ):
            print(str(i)+" = Fizz")
        elif ( i % 5 == 0 ):
            print(str(i)+" = Buzz")

ran = int(input("Enter a range to play... "))
fizzBuzz(ran)