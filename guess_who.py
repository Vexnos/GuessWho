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
    player1_choice = input("Player 1, please pick your plane: ")

    return player1_choice

if __name__ == "__main__":
    bar = "-" * 64
    planes = ["B747-8", 
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
              "Concorde"]

    player1_choice = intro()