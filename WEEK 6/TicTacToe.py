#!/usr/bin/python3

"""
This is a game program
It is the Tic Tac Toe
Whoever doesnt know it?
"""

import numpy

player_1 = 'X'
player_2 = 'O'
board    = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])

"""
This method is used to check if a player has won the game or not
it takes in input symbol and checks the row,columns and diagonal
returns true if it is a win else returns false
"""
def won(symbol):
    
    # Check the rows for matching symbol
    for r in range(3):
        counter = 0
        for c in range(3):
            if ( board[r][c] == symbol ):
                counter += 1
    
    if ( counter == 3 ):
        row_win = True
    else:
        row_win = False
    
    # Check the collumns for matching symbol
    for c in range(3):
        counter = 0
        for r in range(3):
            if ( board[r][c] == symbol ):
                counter += 1
    
    if ( counter == 3 ):
        col_win = True
    else:
        col_win = False
    
    # Check the diagonals for matching symbol
    for i in range(3):
        counter = 0
        if ( board[i][i] == symbol ):
            counter += 1
    if ( counter == 3 ):
        dia_win = True
    else:
        dia_win = False
    
    if (not dia_win):
        if ( board[0][2] == board[1][1] and board[1][1] == board[2][0]  ):
            dia_win = True
    
    return (row_win or col_win or dia_win)

"""
place() is a method that takes in the input symbol
gets row and column as input and places the symbol
in specified row,col
"""
def place(symbol):
    print()
    print(board)
    while (1):                                           # if invalid input is provided
        row = int(input("Enter the row (1/2/3)    : "))
        col = int(input("Enter the column (1/2/3) : "))
        if ( (row < 4 and row > 0) and (col < 4 and col > 0) and (board[row-1][col-1] == '-') ):
            break                                       # Check if given row,col is empty
        else:
            print("Please enter a valid input !!")      # if not empty
            continue
   board[row-1][col-1] = symbol                        # place the 'X' 'O' in the specified pos

"""
Play() is method to start the game
it prints whether the game is won by some player or
the game is draw
"""
def play():
    for turn in range(9):                                 # alternate player turns 
        if ( turn % 2 == 0 ):
            print("\nPlayer 1's turn ")
            place(player_1)                               # mark 'X'
            if ( won(player_1) ):                         # Check if win
                print(player_1," won the game\n")
                print(board)
                break
        else:
            print("\nPlayer 2's turn ")
            place(player_2)                              # mark 'O'
            if ( won(player_2) ):                        # Check if win
                print(player_2," won the game\n")
                print(board)
                break
    if ( (not won(player_1)) and (not won(player_2)) ):  # Draw both players didnt win
        print("\nThis is match is DRAW")

play()                                                   # Calling play)()