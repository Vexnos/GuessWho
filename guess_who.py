'''
-------------------------------------------------
Author: Daniel Lagesse
Project: Guess Who
Date: 2022-10-25
Version: 1.0.0
-------------------------------------------------
'''
#-------Libraries-------
import sys, subprocess

#-------Functions-------
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

    return player1_choice, player2_choice

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
if __name__ == "__main__":
    bar = "-" * 128
    bar_small = "-" * 64
    planes = ["B747", 
              "B777",
              "B787",
              "B767",
              "B757",
              "B737",
              "A220",
              "A320",
              "A321",
              "A330",
              "A340",
              "A350",
              "A380",
              "F18",
              "F22",
              "F35",
              "F14",
              "Concorde",
              "A-10 Warthog",
              "DC-3",
              "DC-10",
              "MD-80"]

    planes_print = ", ".join([str(plane) for plane in planes])

    playing = True
    while playing:
        player1_choice, player2_choice = intro()
        winner = guess(player1_choice, player2_choice)

        print(f"{bar_small}\nCongratulations! {winner} has won the game!\n{bar_small}")

        play_again = input("Play again? (y/n): ")
        playing = play_again.lower().startswith("y")
