#!/usr/bin/python3

"""
This program demonstrates the spiral traversal of 
a matrix given an nxn matrix
"""

def spiral( m, n, a ):
    
    k = l = 0
    
    """
    k - row index
    l - column index
    """
    
    while ( k < m and l < n ):
        
        # print first row from 0 - n
        for i in range( l, n ):
            print(a[k][i],end=" ")
        
        k += 1
        
        # Print columns from 1,n to n,n
        for i in range( k, m ):
            print(a[i][n-1],end=" ")
        
        n -= 1
        
        if ( k < m ):
            # print the rows in reverse
            for i in range( n-1, l-1, -1 ):
                print(a[m-1][i],end=" ")
            
            m -= 1
            
        if ( l < n ):
            # Print the columns in reverse
            for i in range( m-1, k-1, -1 ):
                print(a[i][l],end=" ")
            l += 1


a = []
count = 1
for i in range(5):
    l = []
    for j in range(5):
        l.append(count)
        count += 1
    a.append(l)

spiral(5,5,a)
