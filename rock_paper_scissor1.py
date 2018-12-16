#Simple Rock Paper and Scissors Game!

from random import randint

print("#### Simple Rock vs. Paper Game!                ####\n")
print("#### Please type one of the following options   ####\n")

player = input("#### Rock, Paper, or Scissors                   ####\n\n")
print("You Played:\n")
print(player)

#rRandom number generator 1-3
#Numbers 1-3 each have unique values and printed depending on value generated
#Program can then compares the user input value to the randomly generated value giving the ruslt of the game.

chosen_random = randint(1,3)
if chosen_random == 1:
    computer = "Rock"
elif chosen_random == 2:
    computer = "Paper"
elif chosen_random == 3:
    computer = "Scissors"

print("\nThe Computer played: \n")
print(computer)

#Currently does not have capability to show invalid option if incorrect valu is given,
# etc: if any other value besides Rock, Paper or Scissors is inserted nothing will happen
# since program is not being told what to do in that case giving no result at all

if computer == player:
    print("\nIt is a draw!\n")
elif computer == "Scissors" and player == "Paper" or computer == "Rock" and player == "Scissors" or computer == "Paper" and player == "Rock":
    print("\nThe Computer Wins!\n")
elif computer == "Paper" and player == "Scissors" or computer == "Scissors" and player == "Rock" or computer == "Rock" and player == "Paper":
    print("\nYou Win!\n\n")

print("Thanks for playing!")
print("Created by Garrett Johnson, 2018")


