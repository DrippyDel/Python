# imports random lib
import random

# User's Score
user_score = 0

# Computer's score
cpu_score = 0

game_running = 1

#        0       1        2
rps = ["rock","paper","scissors"]

print("\nWelcome to our Rock, Paper, Scissor Game!")
print("You will be going against our best Cpu!")
print("The first to 3 would win. Good Luck! \n")

while game_running == 1:

    # Asks the user for input and then returns input in lowercase
    userInput = input("Please type Rock, Paper, Scissors, or e to exit: ").lower().strip()

    # If and elif statements to check user input
    if userInput == "e":
        print("You have pressed", userInput)
        print("Game would now end")
        game_running = 0
        break

    elif userInput not in rps:
        print("Wrong input")
        continue

    # if userInput == "e":
    #     print("You have pressed", userInput)
    #     print("Game would now end")
    #     game_running = 0
    #     break
    #
    # elif userInput == "rock":
    #     print(" ")
    #
    # elif userInput == "paper":
    #     print(" ")
    #
    # elif userInput == "scissors":
    #     print(" ")
    #
    # # Program would end if wrong input is entered (should change this)
    # else:
    #     print("Wrong input")
    #     print("Game would now end")
    #     continue

    # Generates a random number 0 thru 2
    random_number = random.randint(0,2)

    computer_pick = rps[random_number]

    # If and elif statements to determine winner
    if userInput == "rock" and computer_pick == "scissors":
        print("You have won")
        print("The Cpu picked", str(computer_pick) + "\n")
        user_score = user_score + 1
        # user_score += 1

    elif userInput == "paper" and computer_pick == "rock":
        print("You have won")
        print("The Cpu picked", str(computer_pick) + "\n")
        user_score = user_score + 1

    elif userInput == "scissors" and computer_pick == "paper":
        print("You have won")
        print("The Cpu picked", str(computer_pick) + "\n")
        user_score = user_score + 1

    elif userInput == computer_pick:
        print("No way a tie")
        print("The Cpu picked", str(computer_pick) + "\n")

    else:
        print("Sucks to suck you lost")
        print("The Cpu picked", str(computer_pick) + "\n")
        cpu_score = cpu_score + 1
        #cpu_score += 1

    print("Reminder your score is",user_score)
    print("Reminder Cpu score is",str(cpu_score) + "\n")

    # Ends the game once one of the players gets 3 wins
    if user_score == 3:
        game_running = 0
        print("You have won you have",str(user_score) + " wins")
        print("Game would now end")

    elif cpu_score == 3:
        game_running = 0
        print("Haha how could lose to a computer",str(cpu_score) + " wins")
        print("Game would now end")
