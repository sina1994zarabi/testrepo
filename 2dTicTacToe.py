import numpy as np
import random as rnd

def initializa_borad():
    return np.full((3,3),' ')

def print_board(board):
    print(board)
    print("-"*15)

def check_winner(board,player):
    # check rows,columns,and diagonals
    # checks if all the marks in a column is the same
    col_wins = np.any(np.all(board==player,axis=0))
    # checks if all the marks in a row is the same
    row_wins = np.any(np.all(board==player,axis=1))
    # checks if all the marks in a main diag is the same
    main_diag_wins = np.all(np.diag(board==player))
    # checks if all the marks in the other  diagonal is the same
    other_diag_wins = np.all(np.diag(np.fliplr(board)==player))
    
    # if any of the winning conditions come true print it
    
    return row_wins or col_wins or main_diag_wins or other_diag_wins
    


def is_board_full(board):
    return ' ' not in board

# returns the move by player
def player_move(board):
    while True:
        try:
            move = tuple(map(int,input('Enter youre move: (row,col) :').split(',')))
            if board[move] == ' ':
                return move
            else:
                print('Invalid move. Cell already occupied. Try again')
        # if the user enters an out of range index for row and columns
        except (ValueError,IndexError):
            print('Invalid Input please enter two space seperated integers')

# the computer chooses among the remaining empty cells
def computer_move(board):
    empty_cells = list(zip(*np.where(board == ' ')))
    return rnd.choice(empty_cells)

def play_game():
    board = initializa_borad()
    players = ['X','O']
    current_player = rnd.choice(players)
    print('Welcome to Tic-Tac-Toe')
    while True:
        print(board)
        if current_player == 'X':
            move = player_move(board)
        else:
            print('Computer is making a move...')
            move = computer_move(board)
            
        board[move] = current_player
        if check_winner(board,current_player):
            print_board(board)
            print(f'{current_player} wins')
            break
        
        if is_board_full(board):
            print_board(board)
            print('It\'s a tie. the board is full')
        
        # assign 'X' as the marker if it is already 'X' if not assign it 'X'
        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    play_game()
        
        
            
    
    
    
    
    



            
            
                



        
    
        
        
    


