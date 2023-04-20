"""
Pseudo code:

player1 <- Empty array
player2 <- Empty array

playing = True

while playing is true
    player1 = [Random number between 1-6, Random number between 1-6]
    player2 = [Random number between 1-6, Random number between 1-6]
    if the sum of player1 is equal to 7 or 11
        playing = False
        OUTPUT "Player 1 Won"
    else if the sum of player2 is equal to 7 or 11
        playing = False
        OUTPUT "Player 2 Won"
    else if the sum of player1 is equal to 2 or 3 or 12
        playing = False
        OUTPUT "Player 1 Lost"
    else if the sum of player2 is equal to 2 or 3 or 12
        playing = False
        OUTPUT "Player 2 Lost"

"""

from random import randint
import tkinter

play = True
game = True

p1 = {"name":input("Enter your name:\n>>"),"nums":None,"score":None}
p2 = {"name":input("Enter your name:\n>>"),"nums":None,"score":None}

while game:
    a = input("Do you want to play the game?\n>>")
    play = False if a == "no" else True
    game = False if a == "no" else True
    
    while play:
        
        p1["nums"] = [randint(1,6),randint(1,6)]
        p2["nums"] = [randint(1,6),randint(1,6)]

        if sum(p1["nums"]) in [7,11]:
            print("Player 1 Won")
            play = False
        elif sum(p2["nums"]) in [7,11]:
            print("Player 2 Won")
            play = False
        elif sum(p1["nums"]) in [2,3,12]:
            print("Player 1 Lost")
            play = False
        elif sum(p2["nums"]) in [2,3,12]:
            print("Player 2 Lost")
            play = False