# a 4 by 4 3d tic tac toe implementation

import numpy as np
import numpy as np
import random as rnd

def initialize_board():
    return np.full((4,4,4),' ')

def print_board(board):
    for plane in board:
        for row in plane:
            print(' | '.join(row))
            print("-"*30)
        print('\n' + '=' * 30)


def check_winner(board,player):
    # check along rows,cols and diagonals
    for i in range(4):  
        if (
            # checking for column match in every single plane
            np.any(np.all(board[i,:,:] == player,axis = 0)) or 
            # checking for row match in every single plane
            np.any(np.all(board[i,:,:]==player,axis = 1)) or
            # cheking for main diag match in every single plane
            np.all(np.diag(board[i])==player) or
            # cheking for other diagonal match in every single plane
            np.all(np.diag(np.fliplr(board[i])==player)) or
            # checking for cross-plane column match
            np.any(np.all(board[:,:,i]==player,axis=0))    
            # np.diag(np.diagonal(board[:,:,:],axis1=1,axis2=0,offset=i)))
        ):
            return True
    # checking for cross-plane diagonal match
    if (
        all(board[i,i,i] == player for i in range(4)) or
        all(board[i,i,3-i] == player for i in range(4))
    ):
        return True
    return False
    
def is_board_full(board):
    return np.all(board != ' ')
    
def player_move(board):
    while True:
        try:
            move = tuple(map(int,input('Enter your move: (plane,row,column): ').split(',')))
            if board[move] == ' ':
                return move
            else:
                print('Buuzzzzzz')
                print('Invalid move. cell already occupied.Try again')
        except (ValueError,IndexError):
            print('Invalid move please enter three comma seperated values')

def computer_move(board):
    empty_cells = list(zip(*np.where(board == ' ')))
    return rnd.choice(empty_cells)


def play_game():
    board = initialize_board()
    current_player = rnd.choice(['X','O'])
    print('Welcome to Tic Tac Toe')
    while True:
        print_board(board)
        if current_player == 'X':
            move = player_move(board)
        else:
            print('Computer is making a move...')
            move = computer_move(board)
        board[move] = current_player
        # check if there is a winner
        if check_winner(board,current_player):
            print_board(board)
            print(f" {current_player} wins")
            break
        # check if it's a tie
        if is_board_full(board):
            print('It\'s a Tie')
            break
        # switch players
        current_player = 'X' if current_player == 'O' else 'O'
            
            
play_game()
