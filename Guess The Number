# Guess The Number
# You have to guess the number in 9 try
import random as ran
number_of_guess = 9
number_to_guess = ran.randint(1, 100)
print("Welcome to the game of guess.\n")
print("You have to guess the number in 9 guess\n")
while (True):
    player_guess = int(input("\nPlese guess the number.\n"))
    if number_of_guess == 0:
        print("You have lost the game\n")
        break
    elif player_guess == number_to_guess:
        number_of_guess = number_of_guess - 1
        print("Congratulation you have won the game in", 9 - number_of_guess, end=" try.\n")
        w = input("would you like to countinu the game(Y/N):")
        if w.capitalize() == "Y":
            number_of_guess = 9 - number_of_guess + number_of_guess
            print("Lets start the game agane.\n")
            print("You have to guess the number in 9 guess\n")
        else:
            break
    elif player_guess > number_to_guess:
        print("Plese put a lower number.")
        print("You have", number_of_guess, end=" guess left.\n")
        number_of_guess = number_of_guess - 1
    else:
        print("Plese put a greater number.")
        print("You have", number_of_guess, end=" guess left.\n")
        number_of_guess = number_of_guess - 1
   
