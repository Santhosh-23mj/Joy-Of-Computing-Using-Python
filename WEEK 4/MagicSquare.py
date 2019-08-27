#!/usr/bin/python3
"""
Magic square Program
  0  1  2
  __ __ __
0| 1  2  3|
1| 4  5  6|
2| 7  8  9|

The sum of all rows, columns and diagonals should be same

M = n*(n^2+1)/2

Steps :
    1. 1 (one) is at ( n/2, n-1 )
    2. let position of 1 ( n/2, n-1 ) be ( p,q ) next num is @ ( p-1, q+1 )
        if row becomes -1 make it n-1, if column is n make it 0
    3.if calculated position already has number decrement column by 2 increment
        row by 1
    4.if row becomes -1 and column becomes n switch it to ( 0, n-2 )

"""

def MagicSquare( n ):
    
    i      = int(n/2)
    j      = n-1
    count  = 1
    matrix = []
    square = n*n
    
    # one cool way to create matrix in python
    matrix = [[0 for i in range(n)]for j in range(n)]
    
    # The classical method
    """
    for i in range(n):
        ls = []
        for j in range(n):
            ls.append(0)
        matrix.append(ls)
    """
    
    while ( count <= square ):       # count for all elements of matrix 1 to n^2
        if ( i == -1 and j == n ):   # condition 4
            i,j = 0,n-2
        else:
            if ( j == n ):           # Condition 2
                j = 0
            if ( i < 0 ):            # Condition 2
                i = n-1
        if ( matrix[i][j] != 0 ):    # Condition 3
            j -= 2
            i += 1
            continue                 # continue to recheck the conditions
        else:
            matrix[i][j] = count     # start filling the matrix
            count += 1               # next number to fill
            
        i = i-1                      # Condition 2
        j = j+1                      # Condition 2
    
    print("The Magic sum is : ",int(n*(square+1)/2))  # Printing M
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")   # Printing Matrix end to give matrix look
        print()

size = int(input("Enter the size to print : "))
while ( size % 2 != 1 ):                                     # Check if input is odd
    size = int(input("Please enter an odd number : "))
MagicSquare(size)
                