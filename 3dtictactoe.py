import numpy as np
import numpy as np
import random as rnd

# a 4 by 4 3d tic tac toe implementation


# array0 = np.array(['' for _ in range(16)]).reshape(4,4)
# array1 = np.array(['' for _ in range(16)]).reshape(4,4)
# array2 = np.array(['' for _ in range(16)]).reshape(4,4)
# array3 = np.array(['' for _ in range(16)]).reshape(4,4)


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

'''next steps:
       1) visualize it using GUI libraries
       2) make the computer smarter by implementing different dificulty levels
       3) put it on the web and your github repo
'''
    
            
        
        
            
            

    
                    

                
    
    
    



# my primary implementation
# computer moves defined
# def computer_play():
#     while True:
#         x,y,z = [rnd.randrange(4) for _ in range(3)]
#         if z == 0:
#             global array0
#             if not array0[x,y]:
#                 array0[x,y] = 'O'
#                 return array0
#             else:
#                 continue
#         elif z == 1:
#             global array1
#             if not array1[x,y]:
#                 array1[x,y] = 'O'
#                 return array1
#             else:
#                 continue
#         elif z == 2:
#             global array2
#             if not array2[x,y]:
#                 array2[x,y] = 'O'
#                 return array2
#             else:
#                 continue
#         else:
#             global array3
#             if not array3[x,y]:
#                 array3[x,y] = 'O'
#                 return array3
#             else:
#                 continue
# user_moves 
# def user_play():
#     global array0
#     global array1
#     global array2
#     global array3
#     x,y,z = list(map(int,
#                      input('enter the coordinates with space in between(x y z): ').split(' ')))
#     if z == 0:
#         if not array0[x,y]:
#             array0[x,y] = 'X'
#             return array0
#         else:
#             raise ValueError('Invalid Input')
#     elif z == 1:
#         global array1
#         if not array1[x,y]:
#             array1[x,y] = 'X'
#             return array1
#         else:
#             raise ValueError('Invalid Input')
#     elif z == 2:
#         global array2
#         if not array2[x,y]:
#             array2[x,y] = 'X'
#             return array2
#         else:
#             raise ValueError('Invalid Input')
#     else:
#         global array3
#         if not array3[x,y]:
#             array3[x,y] = 'X'
#             return array3
#         else:
#             raise ValueError('Invalid Input')
# checks for diagonal check in each plane
# def diagonal_check(arrays):
#     for array in arrays:
#         if array[0,0] == 'X' and array[1,1] == 'X' and array[2,2] == 'X' and array[3,3] == 'X':
#             winning_status = 'player wins'
#             return winning_status
#         if array[0,0] == 'O' and array[1,1] == 'O' and array[2,2] == 'O' and array[3,3] == 'O':
#             winning_status = 'computer wins'
#             return winning_status
#         if array[0,3] == 'X' and array[1,2] == 'X' and array[2,1] == 'X' and array[3,0] == 'X':
#             winning_status = 'player wins'
#             return winning_status
#         if array[0,3] == 'O' and array[1,2] == 'O' and array[2,1] == 'O' and array[3,0] == 'O':
#             winning_status = 'computer wins'
#             return winning_status
#     winning_status = ''
#     return winning_status
# checks for row match in each plane
# def row_check(arrays):    
#     for array in arrays:
#         for row in array:
#             if 'X' in row and 'O' in row:
#                 continue
#             elif 'X' in row:
#                 count = 0
#                 for elm in row:
#                     if elm == 'X':
#                         count += 1
#                 if count == 4:
#                     winning_status = 'player wins'
#                     return winning_status
#             elif 'O' in row:
#                 count = 0
#                 for elm in row:
#                     if elm == 'O':
#                         count += 1
#                     if count == 4:
#                         winning_status = 'computer wins'
#                         return winning_status
#     winning_status = ''
#     return winning_status
# checks for column matchs in each plane
# def col_check(arrays):
#     for array in arrays:
#         for i in range(4):
#             col = array[:,i]
#             if 'X' in col and 'O' in col:
#                 continue
#             elif 'X' in col:
#                 count = 0
#                 for elm in col:
#                     if elm == 'X':
#                         count += 1
#                 if count == 4:
#                     winning_status = 'player wins'
#                     return winning_status
#             elif 'O' in col:
#                 count = 0
#                 for elm in col:
#                     if elm == "O":
#                         count += 1
#                 if count == 4:
#                     winning_status = 'computer wins'
#                     return winning_status
#     winning_status = ''
#     return winning_status

# check cross-plane column and row check????


# implement an algorithem for checking cross-plane diagonal check????


# def game_status():
#     global array0
#     global array1
#     global array2
#     global array3
#     arrays = [array0,array1,array2,array3]
#     winning_status = ''
#     # checking for cross-diagonal match between planes
#     if array0[0,0] == 'O' and array1[1,1] == 'O' and array2[2,2] == 'O' and array3[3,3] == "O":
#         winning_status = 'computer wins'
#         return winning_status
#     if array0[0,0] == 'X' and array1[1,1] == 'X' and array2[2,2] == 'X' and array3[3,3] == "X":
#         winning_status = 'player wins'
#         return winning_status
#     if array0[0,3] == 'O' and array1[1,2] == 'O' and array2[2,1] == 'O' and array3[3,0] == "O":
#         winning_status = 'computer wins'
#         return winning_status
#     if array0[0,0] == 'X' and array1[1,1] == 'X' and array2[2,2] == 'X' and array3[3,3] == "X":
#         winning_status = 'player wins'
#         return winning_status
#     if array0[0,0] == 'O' and array1[1,1] == 'O' and array2[2,2] == 'O' and array3[3,3] == "O":
#         winning_status = 'computer wins'
#         return winning_status
    # checking for winning positions in each songle plane
#     winning_status = diagonal_check(arrays)
#     if winning_status:
#         return winning_status
#     else:
#         winning_status = row_check(arrays)
#         if winning_status:
#             return winning_status
#         else:
#             winning_status = col_check(arrays)
#             if winning_status:
#                 return winning_status
#             return winning_status
    
    
# # flow of the game
# count = 0
# flag = 0
# while count < 64:
#     if flag == 0:
#         computer_play()
#         print(array0,'\n\n',array1,'\n\n',array2,'\n\n',array3)
#         winning_status = game_status()
#         if winning_status:
#             break
#         count +=1 
#         flag = 1
#     elif flag == 1:
#         try:
#             user_play()
#             print(array0,'\n',array1,'\n',array2,'\n',array3,'\n****')
#             winning_status = game_status()
#             if winning_status:
#                 break
#             count += 1
#             flag = 0
#         except:
#             print('Buuuuzzzz')
#             user_play()
#             print(array0,'\n',array1,'\n',array2,'\n',array3,'\n****')
#             winning_status = game_status()
#             if winning_status:
#                 break
#             count += 1
#             flag = 0

# if count == 63:
#     print('It\'s a Tie')
# else:
#     # print the winner side
#     print(winning_status)
            
            
        
        


     
    
    
    

    
    
        
    
    


