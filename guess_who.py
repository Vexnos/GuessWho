'''
-------------------------------------------------
Author: Daniel Lagesse
Project: Guess Who
Date: 2022-10-25
Version: 1.0.0
-------------------------------------------------
'''
def intro():
    print(f"Welcome to Guess Who! Here are your choices!")
    planes_print = ", ".join([str(plane) for plane in planes])
    print(planes_print)

    #Player 1's choice
    false_input = True
    while false_input:
        player1_choice = input("Player 1, please pick your plane: ")
        if not player1_choice.upper() in planes:
            print("Plane not listed!")
            continue
        false_input = False

    #Player 2's choice
    false_input = True
    while false_input:
        player2_choice = input("Player 2, please pick your plane: ")
        if not player2_choice.upper() in planes:
            print("Plane not listed!")
            continue
        false_input = False

    # print(f"Success! {player1_choice} {player2_choice}") # Debugging Statement
    return player1_choice, player2_choice

def guess(player1_choice, player2_choice):
    turn = 1

    unguessed = True
    while unguessed:
        if turn == 1:
            print("It's Player1's turn!")
            player1_guess = input("Guess player2's plane: ")
            if not player1_guess.upper() == player2_choice.upper():
                print("Incorrect!")
                turn = 2
                continue
            unguessed = False
        elif turn == 2:
            print("It's Player2's turn!")
            player2_guess = input("Guess player1's plane: ")
            if not player2_guess.upper() == player1_choice.upper():
                print("Incorrect!")
                turn = 1
                continue
            unguessed = False

if __name__ == "__main__":
    bar = "-" * 64
    planes = ["B747", 
              "B777",
              "B787",
              "B767",
              "B757",
              "B737",
              "A320CEO",
              "A320NEO",
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

    player1_choice, player2_choice = intro()
    guess(player1_choice, player2_choice)
