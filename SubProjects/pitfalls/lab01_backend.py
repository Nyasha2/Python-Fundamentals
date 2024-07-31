"""
Leo Jenkins
CS 1
lab01_backend.py
"""

import random


def display_board(board):
    print()
    
    col_numbers = "   "
    for num in range(len(board)):
        col_numbers += str(num) + "   "
    print(col_numbers)

    for row in range(len(board)):
        column = f"{row} "
        for col in range(len(board)):
            if board[row][col][-1] == "F":
                column += " " + board[row][col][0] + " |"
            elif board[row][col][-1] == "f":
                column += " X |"
            else:
                column += "   |"
        print(column[:-1])
        if row < len(board) - 1:
            horizontal_line = "  " + "---|" * len(board)
            print(horizontal_line[:-1])


def player_move(board):
    flag = False

    while True:
        move = input("Input your next move (in the form row:col). Add an \"f\" to the end to set a flag\n")
        game_over = False

        try:
            [row, col] = move.split(":")

            if col[-1] == "f":
                flag = True
                col = col[:-1]
            row = int(row)
            col = int(col)

            if flag:
                board[row][col] += "f"
                break
            else:
                if board[row][col][-1] == "B":
                    game_over = True
                    break
                else:
                    if board[row][col][-1] != "F":
                        board[row][col] += "F"
                    break
        except:
            print("Invalid input! Input should be of form row:column")

    if game_over:
        quit("Game over! You exploded a bomb!")


def give_opening_clue(board):
    row = random.randint(1, len(board) - 2)
    col = random.randint(1, len(board) - 2)

    for i in range(-1, 2):
        for j in range(-1, 2):
            if row + i >= 0 and row + i < len(board):
                if col + j >= 0 and col + j < len(board):
                    if board[row + i][col + j] != "B":
                        board[row + i][col + j] += "F"