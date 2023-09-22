# Library for random
import random

cpu_number = random.randint(1,100)
user_guess = 0


print("\nWelcome to our guessing game!")
print("Try to guess a number between 1 and 100")
print("Don't worry, you have unlimited tries \n")

while user_guess != cpu_number:

    user_guess = int(input("Enter your guess:"))

    if (user_guess < cpu_number):
        print(str(user_guess) + " is too small")
        print("Pick a higher number\n")

    elif (user_guess > cpu_number):
        print(str(user_guess) + " is too big")
        print("Pick a smaller number\n")

    else:
        print("Nice you got my number!")
        print(str(cpu_number) + " was my guess\n")
