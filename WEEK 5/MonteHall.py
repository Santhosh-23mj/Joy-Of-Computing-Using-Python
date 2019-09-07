#!/usr/bin/python3

"""
Monte Hall is a game similar to the Find the Ace game
We choose one of the three cards if wrong we get a chance 
to swap or stay. This is to demonstrate how effective it 
would be if we swap our choice based on conditional probability
"""

import random

cards  = [0]*3
queens = []

ace = random.randint(0,2)

for i in range(3):
    if ( i == ace ):
        cards[ace] = 'A'
        continue
    else:
        cards[i] = 'Q'
        queens.append(i)
print("|*|  |*|  |*|")
print(" 0    1    2 ")

choice    = int(input("Enter your choice... "))
card_open = random.choice(queens)
print()

while(card_open == choice):
    card_open = random.choice(queens)
    
if (card_open == 0):
    print("|Q|  |*|  |*|")
    print(" 0    1    2 ")
if (card_open == 1):
    print("|*|  |Q|  |*|")
    print(" 0    1    2 ")
if (card_open == 2):
    print("|*|  |*|  |Q|")
    print(" 0    1    2 ")

ch = input("Do you want to swap (Y/N) : ")
print()

if ( ch == 'y' or ch == 'Y' ):
    if ( cards[choice] == 'Q' ):
        print("|"+cards[0]+"|  |"+cards[1]+"|  |"+cards[2]+"|")
        print("You Win")
    else:
        print("|"+cards[0]+"|  |"+cards[1]+"|  |"+cards[2]+"|")
        print("You Lose")
else:
    if ( cards[choice] == 'A' ):
        print("|"+cards[0]+"|  |"+cards[1]+"|  |"+cards[2]+"|")
        print("You Lose")
    else:
        print("|"+cards[0]+"|  |"+cards[1]+"|  |"+cards[2]+"|")
        print("You Win")
