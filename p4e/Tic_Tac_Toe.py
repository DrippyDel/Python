import random
# Tic Tac Toe Game - Delali & John 

# Project Checklist:
# 1) Print welcome screen, rules, and print Tic Tac Toe board (Done)

# 2) Take Player input of choice X's or O's (Done) 

# 3) Take Player input (Done)

# 4) Take Computer (Cpu) input 

# 5) Check if winner or tie

# 6) Switch back to Player's input 

# 7) Repeat steps 3 - 6

# -  |  -  |  -
#---------------
#  - |  -  |  -
#---------------
#  - |  -  |  -

player = ""
winner = ""
cpu = ""

game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

gamerunning = True

def print_game_board(game_board):
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])


def welcome_screen():
    print("\nWelcome to Legendary TicTacToe Battle Sim!!")
    print("Do you think you can beat our formittable Champion!?")
    rules()

    player = input("With the rules out of the way. Which character would you like to play, X's or O's?\n")
    return player 

def rules():
    print("\nHere are the rules: The game board is layed out in a 3 by 3 grid (1-9), choose between the numbers in the grid to mark you choice!")
    print("Be the first to make three in a row Horizontally, Vertcally, or Across to win or become another victim of our Champion!")
    print("If neither players are able to make three in a row the game results in a tie!\n")

def player_input(game_board):
    user_input = int(input("Enter a number 1 - 9: "))

    trueInput = True
    
    while(trueInput):
        if user_input >= 1 and user_input <= 9 and game_board[user_input - 1] == "-":
            game_board[user_input-1] = player
            trueInput = False

        elif user_input < 1 or user_input > 9:
            print("Number entered isn't on our game field!")
            user_input = int(input("Enter a number 1 - 9: "))

        else:
            print("Hey! That spot already has " + game_board[user_input - 1] + " .Please choose another spot!")
            user_input = int(input("Enter a number 1 - 9: "))


def checkWinHorizontal(game_board):

    # If the all the first row is the same value but not "-" then the player of that value is the winner.    
    if game_board[0] == game_board[1] == game_board[2] and game_board[1] != "-":
        winner = game_board[0]
        return winner
    elif game_board[3] == game_board[4] == game_board[5] and game_board[4] != "-":
        winner = game_board[3]
        return winner
    elif game_board[6] == game_board[7] == game_board[8] and game_board[7] != "-":
        winner = game_board[3]
        return winner
    else:
        return None

def checkWinVertical(game_board):
    # If the all the first row is the same value but not "-" then the player of that value is the winner.    
    if game_board[0] == game_board[3] == game_board[6] and game_board[3] != "-":
        winner = game_board[0]
        return winner
    elif game_board[1] == game_board[4] == game_board[7] and game_board[4] != "-":
        winner = game_board[1]
        return winner
    elif game_board[2] == game_board[5] == game_board[8] and game_board[5] != "-":
        winner = game_board[2]
        return winner
    else:
        return None
    
def checkWinAcross(game_board):

    # If the all the first row is the same value but not "-" then the player of that value is the winner.    
    if game_board[0] == game_board[4] == game_board[8] and game_board[4] != "-":
        winner = game_board[0]
        return winner
    elif game_board[2] == game_board[4] == game_board[6] and game_board[4] != "-":
        winner = game_board[2]
        return winner
    else:
        return None

def checkTie(game_board):
    if "-" not in game_board:
        print_game_board(game_board)
        print("The game resulted in a tie")
        winner = "Tie"
        return winner
    else:
        return None

def gameWinner(game_board):
    if checkWinHorizontal(game_board) == "X" or checkWinHorizontal(game_board) == "O":
        return checkWinHorizontal(game_board)             
                        
    elif checkWinVertical(game_board) == "X" or checkWinVertical(game_board) == "O":
        return checkWinVertical(game_board) 
    
    elif checkWinAcross(game_board) == "X" or checkWinAcross(game_board) == "O":
        return checkWinAcross(game_board)
    
    elif checkTie(game_board) == "Tie":
        return checkTie(game_board)

def winMessage():
    print("\nYou have defeated the Champion!!\n")

def switchPlayer(current_player):
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    return current_player

def cpu_input(game_board):
    cpu_choice = random.randint(1,9)
    winner = gameWinner(game_board)

    trueInput = True

    while(trueInput):
        if game_board[cpu_choice - 1] == "-":
            game_board[cpu_choice-1] = cpu
            trueInput = False

        elif winner == "X" or winner == "O":
            trueInput = False

        elif checkTie(game_board) == "Tie":
            trueInput = False
        else:
            cpu_choice = random.randint(1,9)

player = welcome_screen()
#print(player)
#player_input(game_board)

while gamerunning:
    print_game_board(game_board)
    winner = gameWinner(game_board)

    if winner == "X" or winner == "O":
        print("The winner is ", winner)
        winMessage()
        break
    elif winner == "Tie":
        break

    player_input(game_board)
    cpu = switchPlayer(player)
    cpu_input(game_board)
    
