import random
from random import randint
from colorama import Fore, Back, Style

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_score = 0
player_score = 0

while True:
    player_move = input(Fore.MAGENTA + "Choose [r]ock, [p]aper, [s]cissors: ").lower()

    if player_move == "End":
        print("Goodbye! ")
        break
    elif player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Please try again...")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print(f"The computer choose {computer_move}.")

    if (player_move == rock and computer_move == scissors)\
            or (player_move == paper and computer_move == rock)\
            or (player_move == scissors and computer_move == paper):
        player_score += 1
        print(Fore.BLUE + "You win!")
    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw!")
    else:
        computer_score += 1
        print(Fore.RED + "You lose!")

    print(f"{player_score} : {computer_score}")

    input_to_continue_game = input(Fore.MAGENTA + "If you want to play again type [yes] or [no] to quit: ").lower()

    if input_to_continue_game == "yes":
        continue
    elif input_to_continue_game == "no":
        print("Bye! See you again!")
        break
    else:
        raise SystemExit("Invalid Input. Please try again...")
