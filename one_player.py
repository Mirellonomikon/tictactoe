import random


def display_board(board):
    print('\n' * 50)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def check_board(board, player):
    for i in range(1, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    if board[7] == board[5] == board[3] == player or board[1] == board[5] == board[9] == player:
        return True
    for i in range(1, 4):
        if board[i] == board[i + 3] == board[i + 3] == player:
            return True
    return False


def player_choice():
    mark = ''
    while mark not in ['X', 'O']:
        mark = input("Please pick a marker 'X' or 'O': ")
    if mark == 'X':
        mark2 = 'O'
    else:
        mark2 = 'X'
    return mark, mark2


def player_request_move(board):
    while True:
        move = input('Please enter a number between 1-9: ')
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Enter valid number.")
            continue
        if not board[int(move)] == '_':
            print("Spot already taken!")
            move = 0
            continue
        move = int(move)
        break
    return move


def player_move(board, player, move):
    board[move] = player


def board_full(board):
    return '_' not in board


def still_here():
    while True:
        response = input("Still playing? Y/N ")
        if response == 'Y':
            return True
        elif response == 'N':
            return False
        else:
            print("Unknown command.")


def game():
    print("Game on!")
    while True:
        print("New game")
        board = ['_'] * 10
        board[0] = '#'
        game_on = True
        turn = 1
        move_list = list(range(1, 10))
        player1, player2 = player_choice()
        while game_on:
            if turn == 1:
                display_board(board)
                move1 = player_request_move(board)
                player_move(board, player1, move1)
                turn = 2
                move_list.remove(move1)
                if check_board(board, player1):
                    game_on = False
                    print("You win.")
                    continue
            else:
                display_board(board)
                move2 = random.choice(move_list)
                player_move(board, player2, move2)
                turn = 1
                move_list.remove(move2)
                if check_board(board, player2):
                    game_on = False
                    print("You lose!")
                    continue
            if board_full(board):
                game_on = False
                print("Tie!")
        if not still_here():
            break


game()
