"""
Leo Jenkins
CS 1
lab01_student.py
"""

import random
from lab01_backend import display_board, player_move, give_opening_clue

easy_size = 6
medium_size = 8
hard_size = 10

easy_bomb_percentage = 0.20
medium_bomb_percentage = 0.25
hard_bomb_percentage = 0.30


def welcome_menu(board):
    print('Hello! Welcome to Minesweeper')
    difficulty = input("Choose your difficulty: ")
    while True:
        if difficulty == "easy":
            init_board(board, easy_size, easy_bomb_percentage)
            break
        elif difficulty == "medium":
            init_board(board, medium_size, medium_bomb_percentage)
            break
        elif difficulty == "hard":
            init_board(board, hard_size, hard_bomb_percentage)
            break
        else:
            print('easy, medium, or hard')


def init_numbers(board):
    board_size = len(board)
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] != "B":
                board[row][col] = str(num_neighbor_bombs(board, row, col))


def init_board(board, board_size, bomb_percentage):
    for row in range(board_size):
        row = []
        for col in range(board_size):
            choice = random.random()
            if choice <= bomb_percentage:
                row.append("B")
            else:
                row.append("S")
        board.append(row)


def is_game_over(board):
    for row in range(len(board) + 1):
        for col in range(len(board) + 1):
            if board[row][col][-1] not in ["B", "F"]:
                return False
        return True


def num_neighbor_bombs(board, row, col):
    for i in range(-1, 2):
        bomb_counter = 0
        for j in range(-1, 2):
            if row + i >= 0 and row + i < len(board):
                if col + j >= 0 and col + j < len(board):
                    if board[row + i][col + j] == "B":
                        bomb_counter + 1
        return bomb_counter


if __name__ == "__main__":
    board = []
    welcome_menu(board)
    init_numbers(board)
    give_opening_clue(board)
    display_board(board)
    while not is_game_over(board):
        player_move(board)
        display_board(board)