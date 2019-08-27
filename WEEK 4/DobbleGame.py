#!/usr/bin/python3

"""
A game in which two cards with one similar element is presented and we 
have to spot the similarity

string library has been used to generate characters from a-z
string.ascii_letters

Here we simulate the game using Alphabets
"""

import string
import random

card_size = 8
card_1    = [0 for i in range(card_size)]       # Append 0 to show list size
card_2    = [0 for i in range(card_size)]
i         = 0

letters   = list(string.ascii_letters)         # ASCII letters will give all alphabets, made it a list
pos_1     = random.randint(0,card_size-1)      # Position to place similar element
pos_2     = random.randint(0,card_size-1)      # Position to place similar element
similar   = random.choice(letters)             # Get similar element from list letters

letters.remove(similar)                        # Removing similar element else it may be repeated

if ( pos_1 == pos_2 ):                         # Place the similar element
    card_1[pos_1] = similar
    card_2[pos_1] = similar
else:
    card_1[pos_1] = similar
    card_1[pos_2] = random.choice(letters)    
    letters.remove(card_1[pos_2])
    card_2[pos_2] = similar
    card_2[pos_1] = random.choice(letters)
    letters.remove(card_2[pos_1])

while ( i < card_size ):                      # Fill list with random symbols
    if ( i != pos_1 and i != pos_2 ):
        card_1[i] = random.choice(letters)
        letters.remove(card_1[i])
        card_2[i] = random.choice(letters)
        letters.remove(card_2[i])
    i += 1

print(" WELCOME TO DOBBLE GAME ")    
print(''.join(card_1))                        # To complicate elements of list are joined
print(''.join(card_2))

sol = input("Spot the similar letter : ")     # get similar letter as input

if ( sol == similar ):
    print("Right Answer")
else:
    print("Wrong Answer")
