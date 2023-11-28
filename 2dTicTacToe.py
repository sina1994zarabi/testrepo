import numpy as np
import random as rnd
# array = np.array([f"{''}" for _ in range(9)]).reshape(3,3)
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
        
        
            
    
    
    
    
    



            
            
                


''' my primary implementation '''

    

# this function provides all the possible coordinates the computer can take
# def permutations():
#     coordinates = []
#     for i in range(3):
#         for j in range(3):
#             coordinates.append((i,j))
#     return coordinates
    

# The computer impelement changes to the input array
# def computer_play(array):
    # coord = rnd.choice(coords)
    # coords.remove(coord)
    # i,j = coord
    # if array[i,j] == '':
    #     array[i,j] = 'O'
    #     return array , coords
    # else:
    #     computer_play(array,coords=coords)
    # while True:
    #     i , j = rnd.randrange(3) , rnd.randrange(3)
    #     if array[i,j] == ' ':
    #         array[i,j] = 'O'
    #         return array
    #     else:
    #         continue

# the user plays if by accident chooses the wrong pos an arbitrary erro will occur
# def user_play(array):
#     prompt = list(map(int,input('Enter the row & column: [r c]: ').split(' ')))
#     i,j = prompt
#     if array[i,j] == ' ':
#         array[i,j] = 'X'
#         return array
#     else:
#         raise ValueError('Invalid Input')

# indicated the winning side if none returns an empty string
# def game_status(array):
#     winning_status = ''
    # checking for diagonal match
    # if array[0,0] == 'X' and array[1,1] == 'X' and array[2,2] == 'X':
    #     winning_status = 'player wins'
    #     return winning_status
    # if array[0,0] == 'O' and array[1,1] == 'O' and array[2,2] == 'O':
    #     winning_status = 'computer wins'
    #     return winning_status
    # if array[0,2] == 'X' and array[1,1] == 'X' and array[2,0] == 'X':
    #     winning_status = 'player wins'
    #     return winning_status
    # if array[0,2] == 'O' and array[1,1] == 'O' and array[2,0] == 'O':
    #     winning_status = 'computer wins'
    #     return winning_status
    # checking for column check
    # for i in range(3):
    #     col = array[:,i]
    #     if 'X' in col and 'O' in col:
    #        continue
    #     elif 'X' in col:
    #         count = 0
    #         for elm in col:
    #             if elm == 'X':
    #                 count += 1
    #         if count == 3:
    #             winning_status = 'player wins'
    #             return winning_status
    #     elif 'O' in col:
    #         count = 0
    #         for elm in col:
    #             if elm == "O":
    #                 count += 1
    #         if count == 3:
    #             winning_status = 'computer wins'
    #             return winning_status
    # checking for row match
    # for row in array:
    #     if 'X' in row and 'O' in row:
    #         continue
    #     elif 'X' in row:
    #         count = 0
    #         for elm in row:
    #             if elm == 'X':
    #                 count += 1
    #         if count == 3:
    #             winning_status = 'player wins'
    #             return winning_status
    #     elif 'O' in row:
    #         count = 0
    #         for elm in row:
    #             if elm == 'O':
    #                 count += 1
    #         if count == 3:
    #             winning_status = 'computer wins'
    #             return winning_status
    # return winning_status
    
       
# flow of the game 
# count = 0
# flag = 0
# while count < 9:
    # if count == 0 and flag == 0:
    #     # array , coords = computer_play(array)
    #     array = computer_play(array)
    #     print(array)
    #     count += 1
    #     flag = 1
    # else:
        # if flag == 0:
        #     # array , coords = computer_play(array,coords=coords)
        #     array = computer_play(array)
        #     print(array)
        #     winning_status = game_status(array)
        #     if winning_status:
        #         break
        #     flag = 1
        #     count += 1
        # elif flag == 1:
        #     try:
        #         array = user_play(array)
        #         winning_status = game_status(array)
        #         print(array)
        #         if winning_status:
        #             break
        #         count += 1
        #         flag = 0
        #     except:
        #         print('Buzzzzz')
        #         array = user_play(array)
        #         print(array)
        #         winning_status = game_status(array)
        #         if winning_status:
        #             break
                # count += 1
#                 flag = 0
# if count == 8:
#     print("It's a tie")
# else:
#     print(winning_status)

# next steps:
# using GUI visualize youre game and make it more interactive 
# put it on web

        
    
        
        
    


