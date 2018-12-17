"""IMPORT RANDOM LIB"""


from random import randint

"""TOTAL GUESSES FROM USERS STORED IN VARIABLE TOTAL_GUESS"""

total_guess = []

print("####           Random Number Guessing Game       ####")
print("#### Can you guess what the next number will be? ####")
print("#### Pick any number between 1 and 5 and see if  ####")
print("#### you can guess the random number!            ####")
print("#### You will also only receive 3 guesses!       ####\n")

"""USER INPUT 1 - 5/NO FLOAT/INT CONVERSION/APPEND USER INPUT IF GUESS IS INCORRECT TO TOTAL_GUESS"""

user_guess = input("Enter a number between 1 and 5 \n")
guess_int = int(user_guess)
total_guess.append(user_guess)

"""RANDOM INT GENERATED 1 - 5"""

random_num = randint(1, 5)

print("Your guess:", user_guess)

"""IF USER GUESSES INCORRECT WHILE LOOP FOR 2 MORE CHANCES"""

while len(total_guess) < 3:
    if guess_int != random_num:
        user_guess = input("You guessed incorrectly...sorry please try again!\n")
        total_guess.append(user_guess)
        guess_int = int(user_guess)
        print("Your guess:", user_guess)

"""IF THE USER FAILS AFTER 3 CHANCES IT WILL AUTO PRINT WHAT THE RANDOM NUMBER WAS AND END THE CODE"""

print("The random number was:", random_num)

"""IF THE RANDOM NUMBER IS GUESSED CORRECTLY CONGRATS WILL BE DISPLAYED"""

if guess_int == random_num:
    print("Congrats! You guessed the correct number!")

print("\n")
print("Thanks for playing!")
print("Created by Garrett Johnson,2018")









