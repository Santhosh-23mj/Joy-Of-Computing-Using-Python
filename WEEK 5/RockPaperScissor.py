#!/usr/bin/python3

"""
This is the rock , paper , scissor game but it is in encoded form
So there is no room for cheating in the game
Players : enter a decimal number and the bit position to use for the symbol. Even the 
symbols rock paper scissor also vary based on the player and it is converted to 0,1,2 and 
the game is played
"""

player_1 = {0:'Rock',1:'Paper',2:'Scissor'}
player_2 = {0:'Scissor',1:'Paper',2:'Rock'}

def game(num1,num2,bit1,bit2):
    p1 = int(num1[bit1])%3                  # To convert decimal to 0,1,2
    p2 = int(num2[bit2])%3                    
    
    if ( player_1[p1] == player_2[p2] ):
        print("Draw")
    elif ( player_1[p1] == 'Rock' and player_2[p2] == 'Paper' ):
        print("Player 2 Wins!!")
    elif ( player_1[p1] == 'Rock' and player_2[p2] == 'Scissor' ):
        print("Player 1 Wins!!")
    elif ( player_1[p1] == 'Paper' and player_2[p2] == 'Rock' ):
        print("Player 1 Wins!!")
    elif ( player_1[p1] == 'Paper' and player_2[p2] == 'Scissor' ):
        print("Player 2 Wins!!")
    elif ( player_1[p1] == 'Scissor' and player_2[p2] == 'Rock' ):
        print("Player 2 Wins!!")
    elif ( player_1[p1] == 'Scissor' and player_2[p2] == 'Paper' ):
        print("Player 1 Wins!!")

while (1):
    num_1 = input("Player 1, Enter your number : ")
    num_2 = input("Player 2, Enter your number : ")
    bit_1 = int(input("Player 1, Your Bit position : "))
    bit_2 = int(input("Player 2, Your Bit position : "))
    
    game(num_1,num_2,bit_1,bit_2)
    cont  = input("Do you want to Continue (y/n) : ")
    
    if ( cont =='n' or cont == 'N' ):
        break
    else:
        continue
