from random import randint

print("#### Simple Rock vs. Paper Game!                ####")
print("#### Please type one of the following options   ####")

"""USER INPUT"""

player = input("#### Rock, Paper, or Scissors                   ####\n")
print("You Played:")
print(player)

"""RANDOM NUMBER CHOSEN BETWEEN 1 - 3 EACH GIVEN A VALUE TO COMPARE TO USER"""

chosen_random = randint(1,3)
if chosen_random == 1:
    computer = "Rock"
elif chosen_random == 2:
    computer = "Paper"
elif chosen_random == 3:
    computer = "Scissors"

print("The Computer played:")
print(computer)

"""CHECKING IF COMPUTER IS < > OR = TO USER"""

if computer == player:
    print("\nIt is a draw!\n")
elif computer == "Scissors" and player == "Paper" or computer == "Rock" and player == "Scissors" or computer == "Paper" and player == "Rock":
    print("\nThe Computer Wins!\n")
elif computer == "Paper" and player == "Scissors" or computer == "Scissors" and player == "Rock" or computer == "Rock" and player == "Paper":
    print("\nYou Win!\n\n")

print("Thanks for playing!")
print("Created by Garrett Johnson, 2018")


