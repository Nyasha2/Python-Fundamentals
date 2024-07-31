
import sys
import pytest

sys.path.insert(0, '../lab01_pitfalls')

from lab01 import init_board, is_game_over
from lab01_tests01 import *


def test_init_board_compiles():
    assert True

def test_is_game_over_compiles():
    assert True

def test_init_board():
    board = []
    board_size = 10
    bomb_percentage = 0.5
    init_board(board, board_size, bomb_percentage)
    assert board != []

def test_init_board_size():
    board = []
    board_size = 10
    bomb_percentage = 0.5
    init_board(board, board_size, bomb_percentage)
    assert len(board) == board_size
    assert len(board[0]) == board_size

def test_init_board_bombs_in_range():
    board = []
    board_size = 10
    bomb_percentage = 0.5
    init_board(board, board_size, bomb_percentage)

    bomb_counter = 0
    for row in board:
        for cell in row:
            if cell == "B":
                bomb_counter += 1

    true_percentage = bomb_counter / (board_size ** 2)
    assert 0.4 < true_percentage and true_percentage < 0.6

def test_init_board_only_bombs():
    board = []
    board_size = 10
    bomb_percentage = 0.5
    init_board(board, board_size, bomb_percentage)

    for row in board:
        for cell in row:
            assert cell == "B" or cell == "S"


def test_is_game_over_all_bombs():
    board = [["B" for _ in range(10)] for _ in range(10)]
    assert is_game_over(board)

def test_is_game_over_all_flags():
    board = [["F" for _ in range(10)] for _ in range(10)]
    assert is_game_over(board)

def test_is_game_over_all_numbers():
    board = [["2" for _ in range(10)] for _ in range(10)]
    assert not is_game_over(board)

def test_is_game_over_letters_and_numbers():
    board = [["B", "F", "2", "4", "B", "F"] for _ in range(6)]
    assert not is_game_over(board)


if __name__ == "__main__":
    # section 1
    test_welcome_menu_compiles()
    test_init_numbers_compiles()
    test_is_game_over_compiles()

    # section 2
    test_init_board_compiles()
    test_is_game_over_compiles()
    test_init_board()
    test_init_board_size()
    test_init_board_bombs_in_range()
    test_init_board_only_bombs()
    test_is_game_over_all_bombs()
    test_is_game_over_all_flags()
    test_is_game_over_all_numbers()
    test_is_game_over_letters_and_numbers()