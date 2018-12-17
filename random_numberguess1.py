from random import randint

#total_guess holds the value of how many attempts have been made to guess the number

total_guess = []

print("####           Random Number Guessing Game       ####")
print("#### Can you guess what the next number will be? ####")
print("#### Pick any number between 1 and 5 and see if  ####")
print("#### you can guess the random number!            ####")
print("#### You will also only receive 3 guesses!       ####\n")

#user_guess is the variable for the input string and it is converted into an integer on the following line.


user_guess = input("Enter a number between 1 and 5 \n")
guess_int = int(user_guess)
total_guess.append(user_guess)

#random_num is a variable that holds the value of the randomly generated number
#So (1, 5) = 1, 2, 3, 4, 5 allowing a number to be randomly selected from the range

random_num = randint(1, 5)

print("Your guess:", user_guess)

#While len(total_guess) < 3: allows for the loop to continue for only 3 guesses

while len(total_guess) < 3:
    if guess_int != random_num:
        user_guess = input("You guessed incorrectly...sorry please try again!\n")
        total_guess.append(user_guess)
        guess_int = int(user_guess)
        print("Your guess:", user_guess)

#The loop will continue until total_guess > 2 or guess_int == random_num
print("The random number was:", random_num)
if guess_int == random_num:
    print("Congrats! You guessed the correct number!")

print("\n")
print("Thanks for playing!")
print("Created by Garrett Johnson,2018")









