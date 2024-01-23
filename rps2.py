import sys
import random
from enum import Enum

game_count = 0
def play_rps():
    class Rps(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3  
   
    playerchoice = input("\nEnter ...\n1 for Rock, \n2 for Paper, \n3 for scissor: \n\n")
    if playerchoice not in ["1", "2", "3"]:
        print(f"You must enter values 1, 2, 3")
        return play_rps()
    
    player =int(playerchoice)

    if player < 1 or player > 3:
        sys.exit()

    computerChoice =int(random.choice("123"))

    print(f"You Chose {str(Rps(player)).replace('Rps.', '')}")
    print(f"CPU Chose {str(Rps(computerChoice)).replace('Rps.', '')}")
    
    def decide_winner(player, computerChoice):
        if player == 1 and computerChoice == 3:
            return "You Win"
        elif player == 2 and computerChoice == 1 :
            return "You Win"
        elif player == 3 and computerChoice == 2 :
            return "You Win"
        elif player == computerChoice:
            return "Owww, Tie Game!"
        else:
            return "Python Wins!"
            
    game_result = decide_winner(player, computerChoice)
    print(game_result)
        
    global game_count
    game_count += game_count
    print(f"\n Game count: {game_count}")
        
    print("\n Play again?")
    
    while True:
        playagain = input(f"\n Playagain? \nY for Yes or \nQ to Quit \n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else: 
            break
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("Thank You Playing!")
        sys.exit("Bye!")
    
if __name__ == "__main__":
    play_rps()