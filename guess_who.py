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
    subprocess.run('clear') # Clears the output to avoid clutter
    print(f"Welcome to Guess Who! Here are your choices!")

    #Player 1's choice
    false_input = True
    while false_input:
        print(planes_print)
        player1_choice = input("Player 1, please pick your plane: ").upper()
        if not player1_choice in planes:
            print("Plane not listed!")
            continue
        false_input = False
        subprocess.run('clear') # Clears the output so the users' choice isn't spoiled

    #Player 2's choice
    false_input = True
    while false_input:
        print(planes_print)
        player2_choice = input("Player 2, please pick your plane: ").upper()
        if not player2_choice in planes:
            print("Plane not listed!")
            continue
        false_input = False
        subprocess.run('clear') # Clears the output so the users' choice isn't spoiled

    return player1_choice, player2_choice

def guess(player1_choice, player2_choice):
    turn = 1

    unguessed = True
    while unguessed:

        #Player 1's Turn
        if turn == 1:
            print("It's Player1's turn!")
            player1_guess = input("Guess player2's plane: ").upper()
            if not player1_guess == player2_choice:
                print("Incorrect!")
                turn = 2
                continue
            winner = "Player 1"
            unguessed = False

        #Player 2's Turn
        elif turn == 2:
            print("It's Player2's turn!")
            player2_guess = input("Guess player1's plane: ").upper()
            if not player2_guess == player1_choice:
                print("Incorrect!")
                turn = 1
                continue
            winner = "Player 2"
            unguessed = False

    return winner 

#-------Main Routine-------
if __name__ == "__main__":
    bar = "-" * 64
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
              "A-10",
              "DC-3",
              "MD-80"]

    planes_print = ", ".join([str(plane) for plane in planes])

    playing = True
    while playing:
        player1_choice, player2_choice = intro()
        winner = guess(player1_choice, player2_choice)

        print(f"Congratulations! {winner} has won the game!")

        play_again = input("Play again? (y/n): ")
        playing = play_again.lower().startswith("y")
