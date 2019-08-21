#!/usr/bin/python3

"""
This is the FizzBuzz game where multiples of 3 are said 'Fizz' and multiples 
of 5 is said 'Buzz' and 'FizzBuzz' for both
"""

# This program demonstrates the common mistakes made in 
# coding a FizzBuzz program

for i in range(1,51):
    if ( i % 3 == 0 ):
        print(str(i)+" = Fizz")        # i is casted to string to use + operator
    else:
        if ( i % 5 == 0 ):
            print(str(i)+" = Buzz")
        else:
            if( (i % 3 == 0) and (i % 5 == 0) ):
                print(str(i)+" = FizzBuzz")
            else:
                print(str(i))

""" 
Note that output contains only 'Fizz' and 'Buzz' even for numbers divisible by
both 3 and 5 can you debug it
"""