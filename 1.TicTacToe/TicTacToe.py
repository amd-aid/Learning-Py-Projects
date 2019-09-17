# Tic Tac Toe Game 

import random

# Creating the board  

def display_board(board):
    pb = {1:'     |     |     \n',
          2:'_________________\n',
          3:'  '+board[1]+'  |  '+board[2]+'  |  '+board[3]+'  \n',
          4:'  '+board[4]+'  |  '+board[5]+'  |  '+board[6]+'  \n',
          5:'  '+board[7]+'  |  '+board[8]+'  |  '+board[9]+'  \n'}

    print(pb[1]+pb[1]+pb[3]+pb[1]+pb[1]+pb[2]+
          pb[1]+pb[1]+pb[4]+pb[1]+pb[1]+pb[2]+
          pb[1]+pb[1]+pb[5]+pb[1]+pb[1])

# Taking user input X or O

def player_input():
    answer = input("Please pick a marker 'X' or 'O' ")
    while True:
        if answer.upper() == 'X':
            return answer.upper()
        elif answer.upper() == 'O':
            return answer.upper()
        else:
            answer = input("Invalid input. Please pick a marker 'X' or 'O'")
            

# Place marker on board

def place_marker(board, marker, position):
    board[position] = marker
    return board

# check for a win

def win_check(board, mark):
    # 1, 2 ,3
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    # 4, 5, 6
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    # 7, 8, 9
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    # 1, 4, 7
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    # 2, 5, 8
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    # 3, 6 ,9
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    # 1, 5, 9
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    # 3, 5, 7
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False

# who goes first

def choose_first():
    i = random.randint(1,2)
    if i == 1:
        return 'Player 1'
    else:
        return 'Player 2' 

# Check if space is free

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

# Check if board is full

def full_board_check(board):
    for i in board:
        if i == ' ':
            return False
    return True
    

# input position and check if its free

def player_choose(board):
    position = int(input("Please enter a number: "))

    while position > 9 or position < 1:
        position = int(input("Please enter a number from 1-9: "))
    
    while position <= 9 or position >= 1:
        if space_check(board, position):
            return position
        else:
            position = 0
            while position <= 0 or position > 9:
                position = int(input("Please enter a number from 1-9 that is free: "))

# ask if players want to replay the game 

def replay():
    rplay = input("Would you like to play again, Yes or No: ")

    while True:
        if rplay.lower() == 'yes':
            return True
        elif rplay.lower() == 'no':
            return False
        else:
            rplay = input('Please answer yes or no: ')


print("Welcome to Tic Tac Toe")

while True:
    # Clear the board
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    #Which player first
    player = choose_first()
    print(player, "will go first")

    # Choose Marker and set first and second player
    if player == 'Player 1':
        marker1 = player_input()
        print('Your marker is', marker1)
        first = 'Player 1'
        second = 'Player 2'
        if marker1 == 'X':
            marker2 = 'O'
        else:
            marker2 = 'X'
    else:
        marker1 = player_input()
        print('Your marker is', marker1)
        first = 'Player 2'
        second = 'Player 1'
        if marker1 == 'X':
            marker2 = 'O'
        else:
            marker2 = 'X'
    
    # Start the game
    i = 2

    while True:
        if win_check(board, marker1):
            print(first, 'WINS')
            break
        elif win_check(board, marker2):
            print(second, 'WINS')
            break
        elif full_board_check(board):
            print('GAME IS A TIE')
            break
        else:
            if i%2 == 0:
                display_board(board)
                print(first)
                position = player_choose(board)
                place_marker(board, marker1, position)
                i = i+1
            else:
                display_board(board)
                print(second)
                position = player_choose(board)                
                place_marker(board, marker2, position)
                i = i+1

    display_board(board)
    
    if replay():
        continue
    else:
        break



