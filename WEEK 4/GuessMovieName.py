#!/usr/bin/python3

"""
This is a game that gives us movie name as blanks and ask us fill 
the name for each guess and finally reveal the movie name
"""

import random

movies = ["ANBE SIVAM","STRAWBERRY","DARLING","DILLUKKU DUDDU","PETTA","VISWASAM","THALAIVA","MERSAL","DHARMATHIN THALAIVAN","THANGAMEENGAL"]

def make( movie ):
    n = len(movie)
    temp_ls = []
    for i in range(n):
        if (movie[i] != " "):
            temp_ls.append("_")
        else:
            temp_ls.append(" ")
    return ''.join(temp_ls)

def is_present(ch,movie):
    movie = list(movie)
    count = movie.count(ch)
    if ( count == 0 ):
        return 0
    else:
        return 1

def mod_mov(ch,ques,movie):
    temp_ls = []
    n       = len(movie)
    ques    = list(ques)
    movie   = list(movie)
    
    for i in range(n):
        if ( movie[i] == " " or movie[i] == ch ):
            temp_ls.append(movie[i])
        else:
            if ( ques[i] == "_" ):
                temp_ls.append("_")
            else:
                temp_ls.append(movie[i])
    return ''.join(temp_ls)
            
P1_name  = input("Player 1, Enter your name : ")
P2_name  = input("Player 2, Enter your name : ")
P1_score = 0
P2_score = 0
turn     = 0
game_on  = 1


while ( game_on ):
    if ( turn == 0 ):
        turn = 1
        print()
        print("Please use CAPITAL LETTERS ")
        print()
        print("------------------------------")
        print(P1_name,"your turn ")
        print("------------------------------")
        pick = random.choice(movies)
        qn = make(pick)
        print()
        print("It is ",len(pick),"characters")
        print(qn)
        modify = qn
        
        right = 1
        while ( right ):
            letter = input("Your guess : ")
            print()
            if ( (is_present(letter,pick)) == 1 ):
                modify = mod_mov(letter,modify,pick)
                print(modify)
                ch = int(input("Did you get the movie name : 0-Letter 1-Movie Name  : "))
                if ( ch == 1 ):
                    ans = input("Enter the movie name : ")
                    if ( ans == pick ):
                        print()
                        print("Right Answer !!")
                        P1_score += 10
                        print(P1_name,"Your score is now :",P1_score)
                        right = 0
                    else:
                        print("Wrong Answer :( Please try again")
            else:
                print("Letter not present :( Try harder")
        
        cont = int(input("Wish to Continue..(0-quit/1-continue) : "))
        if ( cont == 0 ):
            print()
            print("Thanks for playing the game")
            print("Hope you guys enjoyed the game")
            print(P1_name,"has scored :",P1_score)
            print(P2_name,"has scored :",P2_score)
            game_on = 0
            continue
        
        if( turn == 1 ):
            turn = 0
            print()
            print("Please use CAPITAL LETTERS")
            print()
            print("----------------------------")
            print(P2_name,"your turn ")
            print("----------------------------")
            pick = random.choice(movies)
            qn = make(pick)
            print("It is ",len(pick),"characters")
            print(qn)
            modify = qn
            
            right = 1
            while ( right ):
                letter = input("Your guess : ")
                print()
                if ( (is_present(letter,pick)) == 1 ):
                    modify = mod_mov(letter,modify,pick)
                    print(modify)
                    ch = int(input("Did you get the movie name : 0-Letter 1-Movie Name  : "))
                    if ( ch == 1 ):
                        ans = input("Enter the movie name : ")
                        if ( ans == pick ):
                            print()
                            print("Right Answer !!")
                            P2_score += 10
                            print(P2_name,"Your score is now :",P2_score)
                            right = 0
                        else:
                            print("Wrong Answer :( Please try again")
                else:
                    print("Letter not present :( Try harder")
        
        cont = int(input("Wish to Continue..(0-quit/1-continue) : "))
        if ( cont == 0 ):
            print()
            print("Thanks for playing the game")
            print("Hope you guys enjoyed the game")
            print(P1_name,"has scored :",P1_score)
            print(P2_name,"has scored :",P2_score)
            game_on = 0
            continue
        