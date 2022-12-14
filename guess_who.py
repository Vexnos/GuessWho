'''
-------------------------------------------------
Author: Daniel Lagesse
File: Main Guess Who
Project: Guess Who
Date: 2022-10-25
-------------------------------------------------
'''
#-------Libraries-------
import sys, subprocess, random
from guesswho_plane_lists import *

#-------Functions-------
# Intro Function
def intro():
    clear() # Clears the output to avoid clutter

    #Player 1's choice
    false_input = True
    while false_input:
        print(f"Welcome Player 1 to Guess Who! Here are your choices:")
        print(f"\n{bar}\n{planes_print}\n{bar}\n")
        player1_choice = input("Player 1, please pick your plane: ").upper()
        if not player1_choice in planes:
            print("Plane not listed!")
            continue
        false_input = False
        clear() # Clears the output so the users' choice isn't spoiled

    #Player 2's choice
    false_input = True
    while false_input:
        print(f"Welcome Player 2 to Guess Who! Here are your choices:")
        print(f"\n{bar}\n{planes_print}\n{bar}\n")
        player2_choice = input("Player 2, please pick your plane: ").upper()
        if not player2_choice in planes:
            print("Plane not listed!")
            continue
        false_input = False
        clear() # Clears the output so the users' choice isn't spoiled

    # player2_choice = random.choice(planes) # The AI picks its plane

    return player1_choice, player2_choice

# Guess function
def guess(player1_choice, player2_choice):
    turn = 1

    unguessed = True
    while unguessed:
        
        # Who is guessing?
        while True:
            try:
                turn = int(input("Who would like to guess? (1/2): "))
                break
            except ValueError:
                print("Invalid input entered, please try again.")

        # Player 1's Turn
        if turn == 1:
            player1_guess = input("Guess Player 2's plane: ")
            if player1_guess != player2_choice:
                print("Incorrect!")
                continue
            print("Correct!")
            winner = "Player 1"
            unguessed = False

        # Player 2's Turn
        if turn == 2:
            player2_guess = input("Guess Player 1's plane: ")
            if player2_guess != player1_choice:
                print("Incorrect!")
                continue
            print("Correct!")
            winner = "Player 2"
            unguessed = False

    return winner 

def clear():
    subprocess.run('clear') # Runs clear command in the Python terminal

#-------Main Routine-------
bar = "-" * 128
bar_small = "-" * 64

planes_print = ", ".join([str(plane) for plane in planes])

# Start
if __name__ == "__main__":
    playing = True
    while playing:
        player1_choice, player2_choice = intro()
        winner = guess(player1_choice, player2_choice)

        print(f"{bar_small}\nCongratulations! {winner} has won the game!\n{bar_small}")

        play_again = input("Play again? (y/n): ")
        playing = play_again.lower().startswith("y")
