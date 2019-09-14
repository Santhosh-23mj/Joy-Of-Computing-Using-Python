#!/usr/bin/python3

"""
This is a snake and ladder game
The thing new here is the PIL library to open images
"""

from PIL import Image
import random

end = 100

"""
This function just shows the picture of a snake
and ladder board
"""
def show_board():
    img = Image.open('snl.jpg')
    img.show()


"""
This function just checks whether the rolled number 
has a ladder if ladder it returns where the ladder
takes us to 
"""
def check_ladder(dice):
    ladder = { 4:14, 9:31, 20:38, 28:84, 40:59, 51:67, 63:81, 71:91 }
    if ( dice in ladder ):
        print("\n==============[ LADDER :) ]===========\n")
        return ladder[dice]
    else:
        return dice


"""
This function just checks whether the rolled number 
is a snake or not if snake it returns where the snake takes us to
"""
def check_snake(dice):
    snake = { 17:8, 62:19, 87:24, 54:34, 64:60, 93:73, 95:75, 99:78  }
    if ( dice in snake ):
        print("\n-------------[ Snake :( ]--------------\n")
        return snake[dice]
    else:
        return dice


"""
This is the main function of the program
which calls others functions and does the job 
"""
def play():


    # Get player names
    player_1 = input("Player 1, Enter your name : ")
    player_2 = input("Player 2, Enter your name : ")

    # intialize player scores
    score_1 = score_2 = 0

    # Variable to alternate chances
    turn = 0

    while (1):

        if ( turn == 0 ):
            turn = 1
            print()
            print(player_1,", your turn...")

            # Whether to Continue or Quit
            c = input("Do you Wish to continue (Y/N)")
            if ( c == 'n' or c == 'N' ):
                print("Thanks for playing !!")
                print(player_1," you are at ",score_1)
                print(player_2," you are at ",score_2)
                break

            # Roll the dice using random()
            dice = random.randint(1,6)
            print()
            print(player_1,", you rolled no. ",dice)

            # Adding on the board
            score_1 = score_1 + dice

            # Bound Checks
            score_1 = check_ladder(score_1)
            score_1 = check_snake(score_1)
            print(player_1, ", you are at ", score_1)

            if ( score_1 >= end ):
                print(player_1,", you WON!!")
                print(player_1,", your score : ")

        else:
            turn = 0
            print()
            print(player_2, ", your turn...")

            # Whether to Continue or Quit
            c = input("Do you Wish to continue (Y/N)")
            if (c == 'n' or c == 'N'):
                print("Thanks for playing !")
                print(player_1, " you are at ", score_1)
                print(player_2, " you are at ", score_2)
                break

            # Roll the dice using random()
            dice = random.randint(1, 6)
            print()
            print(player_2,", you rolled no. ", dice)

            # Adding on the board
            score_2 = score_2 + dice

            # Bound Checks
            score_2 = check_ladder(score_2)
            score_2 = check_snake(score_2)
            print(player_2," , you are at ",score_2)

            if (score_2 >= end):
                print(player_2, ", you WON!!")
                print(player_2, ", your score : ")

show_board()
play()