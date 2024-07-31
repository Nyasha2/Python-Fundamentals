import sys
import pytest
import os

sys.path.insert(0, '../lab01_pitfalls')

from lab01 import num_neighbor_bombs
from lab01_tests01 import *
from lab01_tests02 import *


def test_num_neighbor_bombs_compiles():
    assert(True)

def test_num_neighbor_bombs_top_left_corner():
    board = [["S" for _ in range(10)] for _ in range(10)]
    board[0][0] = "B"
    assert num_neighbor_bombs(board, 0, 1) == 1
    assert num_neighbor_bombs(board, 1, 1) == 1
    assert num_neighbor_bombs(board, 1, 0) == 1

def test_num_neighbor_bombs_all_directions():
    board = [["B" for _ in range(3)] for _ in range(3)]
    board[1][1] = "S"
    assert num_neighbor_bombs(board, 1, 1) == 8

def test_num_neighbor_bombs_corners():
    board = [["S" for _ in range(3)] for _ in range(3)]
    board[0][0] = "B"
    board[0][2] = "B"
    board[2][0] = "B"
    board[2][2] = "B"
    assert num_neighbor_bombs(board, 1, 1) == 4

def test_num_neighbor_bombs_empty():
    board = [["S" for _ in range(3)] for _ in range(3)]
    assert num_neighbor_bombs(board, 1, 1) == 0


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

    # section 3
    test_num_neighbor_bombs_compiles()
    test_num_neighbor_bombs_top_left_corner()
    test_num_neighbor_bombs_all_directions()
    test_num_neighbor_bombs_corners()
    test_num_neighbor_bombs_empty()
