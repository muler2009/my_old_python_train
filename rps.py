import sys
import random
from enum import Enum

class Rps(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
print(Rps(2))

playagain = True

while playagain:

    print("")
    playerchoice = input("Enter ...\n1 for Rock, \n2 for Paper, \n3 for scissor: \n\n")

    player =int(playerchoice)

    if player < 1 or player > 3:
        sys.exit(f"You must enter values 1, 2, 3")

    computerChoice =int(random.choice("123"))

    print(f"You Chose {str(Rps(player)).replace('Rps.', '')}")
    print(f"CPU Chose {str(Rps(computerChoice)).replace('Rps.', '')}")

    if player == 1 and computerChoice == 3:
        print("You Win")
    elif player == 2 and computerChoice == 1 :
        print("You Win")
    elif player == 3 and computerChoice == 2 :
        print("You Win")
    elif player == computerChoice:
        print("Owww, Tie Game!")
    else:
        print("Python Wins!")
        
    playagain = input(f"\n Playagain? \nY for Yes or \nQ to Quit \n\n")
    if playagain.lower() == "y":
        continue
    else:
        print("Thank You Playing!")
        break