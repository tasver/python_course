#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random 
board = list(range(1, 10))

def draw_board(board:list)->None:
    """Drow board in console"""
    print("*"*13)
    for i in range(3):
        print("*", board[0+i*3], "*", board[1+i*3], "*", board[2+i*3], "*")
        print("*"*13)

def take_input(player_token:str)->None:    
    """Input your move"""
    valid = False
    while not valid:
        player_answer = input("Enter your move in coord(1-9): " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Check your inpunt data. This is not a number.")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("This cell is ocupied")
        else:
            print("Check your input data. This is not a number from 1 to 9.")

def bot_check(board:list, player_token:str)->None:
    """ bot moves"""
    win_coord = ((0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8),(0,1,2),(3,4,5),(6,7,8))
    valid = False
    count = 0
    x_positions=""
    o_positions=""
    for i in board:
        if i == "X":
            x_positions+=str(count)+","
            count+=1 
        if i == player_token:
            o_positions+=str(count)+","
            count+=1                          
    while not valid:
        bot_answer = 5
        if (str(board[bot_answer-1]) not in "XO"):
            if player_token not in board:
                board[bot_answer-1] = player_token
                valid = True
                break
        else: 
            bot_answer = random.randint(1,9)
            if player_token not in board:
                board[bot_answer-1] = player_token
                valid = True
                break
        for i in win_coord:
            if board[i[0]] == board[i[1]] == player_token and str(board[i[2]]) not in "XO":
                board[i[2]]=player_token
                valid = True
                break           
            elif board[i[1]] == board[i[2]] == player_token and str(board[i[0]]) not in "XO":
                board[i[0]]=player_token
                valid = True
                break
            elif board[i[0]] == board[i[2]] == player_token and  str(board[i[1]]) not in "XO":
                board[i[1]]=player_token
                valid = True
                break
            else:
                if board[i[0]] == board[i[1]] and str(board[i[2]]) not in "XO":
                    board[i[2]]=player_token
                    valid = True
                    break
                elif board[i[1]] == board[i[2]] and str(board[i[0]]) not in "XO":
                    board[i[0]]=player_token
                    valid = True
                    break
                elif board[i[0]] == board[i[2]] and str(board[i[1]]) not in "XO":
                    board[i[1]]=player_token
                    valid = True
                    break
        if board[i[0]] != board[i[1]] and board[i[0]]!= board[i[2]] and board[i[1]]!= board[i[2]] and count>1:
            if str(board[i[1]]) not in "XO":
                board[i[1]]=player_token
                valid = True
                print("1")
                break
            if str(board[i[0]]) not in "XO":
                board[i[0]]=player_token
                valid = True
                print("0")
                break
            if str(board[i[2]]) not in "XO":
                board[i[2]]=player_token
                valid = True
                print("2")
                break                
                    
def check_win(board:list)->bool:
    """Check winner"""
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_coord:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def main(board:list)->None:
    """Controller"""
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            bot_check(board, "O")
            
        else: 
            take_input("X")         
        """else:
            take_input(player_token)"""
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print( tmp, "WIN!")
                win = True
                break
        if counter == 9:
            print( "DROW!")
            break
    draw_board(board)
main(board)

