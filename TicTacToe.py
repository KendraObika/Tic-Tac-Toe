#Tic Tac Toe
import random

# The empty board
board = {'1': ' ' , '2': ' ' , '3': ' ' ,
        '4': ' ' , '5': ' ' , '6': ' ' ,
        '7': ' ' , '8': ' ' , '9': ' ' }

shuffle = ['X', 'O']

def display(board):
    """
    Displays the board to the player each round.

    Board is a dictionary
    """
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def turn(player):
    """
    Completes the turn of a player.

    Player is a string.
    """
    print("It's player " + player + "'s turn.")
    choice = input("Choose a square 1-9: ")

    while not choice.isdigit() or int(choice) < 1 or int(choice) > 9 or board[choice] != ' ':

        if not choice.isdigit():
            choice = input("Choice must be a number. Choose a square 1-9: ")

        elif int(choice) < 1 or int(choice) > 9:
            choice = input("Invalid input. Choose a square 1-9: ")

        elif board[choice] != ' ':
            choice = input("That slot is filled. Choose a different square 1-9: ")

    board[choice] = player


def board_full(board):
    """
    Board is a dictionary.

    Returns whether the entire board is full.
    """
    return all (board[slot] != ' ' for slot in board)


def endGame(player, running, winner):
    """
    Ends the game with a winner

    Player is a string, running is a boolean, winner is a boolean.
    """
    print("Player " + player +  " won the game!")
    running = False
    winner = True

################################################################################

def play():
    """
    Controls the gameplay
    """

    player = random.choice(shuffle)
    rounds = 1
    running = True
    winner = False
    display(board)

    #Introduce yourself and say what we're playing
    print("Hello! Welcome to TicTacToe, what's your name?")
    name = input("My name is: ")
    print("Hello " + name + " and good luck!")


    while running:

        turn(player)
        display(board)

        if rounds >= 5:
            if board['1'] == board['2'] == board['3'] == player: #top row
                endGame(player, running, winner)
            elif board['4'] == board['5'] == board['6'] == player: #middle row
                endGame(player, running, winner)
            elif board['7'] == board['8'] == board['9'] == player: #bottom row
                endGame(player, running, winner)
            elif board['1'] == board['4'] == board['7'] == player: #left column
                endGame(player, running, winner)
            elif board['2'] == board['5'] == board['8'] == player: #middle column
                endGame(player, running, winner)
            elif board['3'] == board['6'] == board['9'] == player: #right column
                endGame(player, running, winner)
            elif board['1'] == board['5'] == board['9'] == player: #left diagonal
                endGame(player, running, winner)
            elif board['3'] == board['5'] == board['7'] == player: #right diagonal
                endGame(player, running, winner)

            if board_full(board) and not winner:
                running = False
                print("It was a tie!")


        if player == 'X':
            player = 'O'
        else:
            player = 'X'

        rounds=rounds+1


################################################################################





if __name__ == '__main__':
    play()
