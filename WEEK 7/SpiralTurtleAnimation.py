#!/usr/bin/python3

"""
This program demonstrates the spiral traversal of 
a matrix given an nxn matrix
"""

import turtle

turtle.bgcolor("black")
pen = turtle.Turtle()

width = 5
height = 7

dot_distance = 25

pen.setpos(-250,250)

def spiral( m, n ):
    
    k = 0
    l = 0
    f = 0
    pen.color("white")
    """
    k - row index
    l - column index
    """
    
    while ( k < m and l < n ):
        
        if ( f == 1 ):
            pen.right(90)
        # print first row from 0 - n
        for i in range( l, n ):
            pen.forward(dot_distance)
        
        k += 1
        f = 1
        
        pen.right(90)
        # Print columns from 1,n to n,n
        for i in range( k, m ):
            pen.forward(dot_distance)
        
        n -= 1
        pen.right(90)
        
        if ( k < m ):
            # print the rows in reverse
            for i in range( n-1, l-1, -1 ):
                pen.forward(dot_distance)
            
            m -= 1
        pen.right(90)
        if ( l < n ):
            # Print the columns in reverse
            for i in range( m-1, k-1, -1 ):
                pen.forward(dot_distance)
            l += 1

spiral(20,20)
turtle.done()