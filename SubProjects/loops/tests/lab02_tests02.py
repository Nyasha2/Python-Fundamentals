import random
import pytest

import sys

sys.path.insert(0, '../lab02_loops')
from lab02 import search_sequence

def test_search_sequence_empty_sequence_and_segment():
    assert search_sequence([], []) == False

def test_search_sequence_empty_sequence():
    assert search_sequence([], ["U", "A", "C", "G"]) == False

def test_search_sequence_empty_segment():
    assert search_sequence(["U", "A", "C", "G"], []) == True

def test_search_sequence_long_segment():
    assert search_sequence(["U", "A", "C", "G"], ["A", "U", "G", "C", "A"]) == False

def test_search_sequence_complements():
    assert search_sequence(["U", "A", "C", "G"], ["A", "U", "G", "C"]) == False

def test_search_sequence_at_the_end():
    assert search_sequence(['C', 'C', 'U', 'G', 'C', 'C', 'C', 'G', 'G', 'G'], ["G", "G", "G"]) == True

def test_search_sequence():
    assert search_sequence(['C', 'C', 'U', 'G', 'C', 'C', 'C', 'G', 'G', 'G'], ["G", "C", "G"]) == False

def test_search_sequence_at_the_beginning():
    assert search_sequence(['C', 'C', 'U', 'G', 'C', 'C', 'C', 'G', 'G', 'G'], ["C", "C", "U"]) == True

def test_search_sequence_wrap_around():
    assert search_sequence(['C', 'C', 'U', 'G', 'C', 'C', 'C', 'G', 'G', 'G'], ["G", "G", "C"]) == False

def test_search_sequence_single_letter():
    assert search_sequence(['C', 'C', 'U', 'G', 'C', 'C', 'C', 'G', 'G', 'G'], ["C"]) == True

def test_search_sequence_lower_case():
    assert search_sequence(['C', 'C', 'U', 'G', 'C', 'C', 'C', 'G', 'G', 'G'], ["c"]) == False

def test_search_sequence2():
    assert search_sequence(['U', 'U', 'C', 'G', 'A', 'A', 'A', 'G', 'C', 'U'], ["A", "G", "C"]) == True

def test_search_sequence_segement_equals_sequence():
    assert search_sequence(['A', 'C', 'C', 'C', 'C', 'C', 'A', 'A', 'U', 'U', 'G', 'A', 'G', 'A', 'A', 'U', 'A', 'G', 'C', 'G'], \
       ['A', 'C', 'C', 'C', 'C', 'C', 'A', 'A', 'U', 'U', 'G', 'A', 'G', 'A', 'A', 'U', 'A', 'G', 'C', 'G']) == True

def test_search_sequence3():
    assert search_sequence(['C', 'U', 'U', 'A', 'A', 'U', 'A', 'U', 'G', 'A', 'A', 'C', 'G', 'A', 'A', 'C', 'G', 'A', 'G', 'C'], \
        ['U', 'G', 'A', 'A', 'C', 'G', 'A', 'A', 'C']) == True

def test_search_sequence4():
    assert search_sequence(['G', 'G', 'G', 'A', 'U', 'G', 'A', 'C', 'C', 'C', 'C', 'G', 'U', 'G', 'C', 'G', 'C', 'G', 'G', 'A'], \
        ['A', 'U', 'G', 'A', 'C', 'C', 'C', 'C', 'G', 'U']) == True

def test_search_sequence5():
    assert search_sequence(['C', 'C', 'C', 'C', 'A', 'C', 'A', 'U', 'A', 'G', 'C', 'G', 'A', 'G', 'C', 'A', 'U', 'C', 'C', 'A'], \
        ['G', 'C', 'A', 'U', 'C', 'C']) == True

# def test_get_complement9():
#     assert get_complement(['A', 'G', 'G', 'C', 'G', 'A', 'A', 'C', 'U', 'G', 'C', 'A', 'U', 'A', 'A', 'C', 'U', 'A', 'C', 'C']) \
#         == ['U', 'C', 'C', 'G', 'C', 'U', 'U', 'G', 'A', 'C', 'G', 'U', 'A', 'U', 'U', 'G', 'A', 'U', 'G', 'G']

# def test_get_complement10():
#     assert get_complement(['A', 'A', 'U', 'A', 'U', 'C', 'C', 'U', 'G', 'G', 'A', 'A', 'G', 'U', 'A', 'G', 'C', 'A', 'A', 'G']) \
#         == ['U', 'U', 'A', 'U', 'A', 'G', 'G', 'A', 'C', 'C', 'U', 'U', 'C', 'A', 'U', 'C', 'G', 'U', 'U', 'C']

# def test_get_complement11():
#     assert get_complement(['U', 'C', 'A', 'G', 'C', 'A', 'U', 'C', 'C', 'U', 'A', 'C', 'U', 'U', 'U', 'G', 'G', 'A', 'U', 'A']) \
#         == ['A', 'G', 'U', 'C', 'G', 'U', 'A', 'G', 'G', 'A', 'U', 'G', 'A', 'A', 'A', 'C', 'C', 'U', 'A', 'U']

# def test_get_complement12():
#     assert get_complement(['G', 'C', 'U', 'G', 'U', 'G', 'G', 'A', 'C', 'C', 'A', 'C', 'A', 'G', 'G', 'C', 'C', 'C', 'G', 'G']) \
#         == ['C', 'G', 'A', 'C', 'A', 'C', 'C', 'U', 'G', 'G', 'U', 'G', 'U', 'C', 'C', 'G', 'G', 'G', 'C', 'C']

# def test_get_complement13():
#     assert get_complement(['C', 'U', 'U', 'U', 'G', 'U', 'U', 'C', 'A', 'G', 'C', 'U', 'A', 'A', 'A', 'C', 'G', 'C', 'U', 'C']) \
#         == ['G', 'A', 'A', 'A', 'C', 'A', 'A', 'G', 'U', 'C', 'G', 'A', 'U', 'U', 'U', 'G', 'C', 'G', 'A', 'G']

# def test_get_complement14():
#     assert get_complement(['G', 'A', 'A', 'C', 'G', 'U', 'G', 'C', 'A', 'U', 'U', 'G', 'U', 'C', 'G', 'C', 'C', 'C', 'U', 'A']) \
#         == ['C', 'U', 'U', 'G', 'C', 'A', 'C', 'G', 'U', 'A', 'A', 'C', 'A', 'G', 'C', 'G', 'G', 'G', 'A', 'U']

# def test_get_complement15():
#     assert get_complement(['G', 'U', 'G', 'G', 'U', 'C', 'G', 'A', 'C', 'G', 'G', 'G', 'U', 'A', 'C', 'C', 'C', 'A', 'C', 'U']) \
#         == ['C', 'A', 'C', 'C', 'A', 'G', 'C', 'U', 'G', 'C', 'C', 'C', 'A', 'U', 'G', 'G', 'G', 'U', 'G', 'A']

# def test_get_complement16():
#     assert get_complement(['G', 'U', 'A', 'A', 'U', 'G', 'A', 'A', 'G', 'A', 'G', 'U', 'A', 'A', 'G', 'A', 'U', 'C', 'G', 'C']) \
#         == ['C', 'A', 'U', 'U', 'A', 'C', 'U', 'U', 'C', 'U', 'C', 'A', 'U', 'U', 'C', 'U', 'A', 'G', 'C', 'G']

# def test_get_complement17():
#     assert get_complement(['A', 'G', 'A', 'A', 'C', 'A', 'C', 'A', 'A', 'A', 'G', 'G', 'U', 'U', 'C', 'A', 'G', 'U', 'G', 'U']) \
#         == ['U', 'C', 'U', 'U', 'G', 'U', 'G', 'U', 'U', 'U', 'C', 'C', 'A', 'A', 'G', 'U', 'C', 'A', 'C', 'A']

# def test_get_complement18():
#     assert get_complement(['C', 'G', 'A', 'C', 'C', 'C', 'U', 'G', 'C', 'C', 'U', 'A', 'A', 'A', 'C', 'C', 'U', 'U', 'A', 'C']) \
#         == ['G', 'C', 'U', 'G', 'G', 'G', 'A', 'C', 'G', 'G', 'A', 'U', 'U', 'U', 'G', 'G', 'A', 'A', 'U', 'G']

# def test_get_complement19():
#     assert get_complement(['C', 'G', 'G', 'G', 'C', 'A', 'G', 'C', 'C', 'A', 'A', 'U', 'C', 'C', 'C', 'C', 'C', 'A', 'G', 'U']) \
#         == ['G', 'C', 'C', 'C', 'G', 'U', 'C', 'G', 'G', 'U', 'U', 'A', 'G', 'G', 'G', 'G', 'G', 'U', 'C', 'A']

# def test_get_complement20():
#     assert get_complement(['U', 'U', 'G', 'C', 'A', 'C', 'G', 'G', 'C', 'U', 'C', 'G', 'C', 'A', 'G', 'G', 'U', 'G', 'C', 'C']) \
#         == ['A', 'A', 'C', 'G', 'U', 'G', 'C', 'C', 'G', 'A', 'G', 'C', 'G', 'U', 'C', 'C', 'A', 'C', 'G', 'G']

# def test_get_complement21():
#     assert get_complement(['C', 'U', 'C', 'A', 'C', 'U', 'U', 'C', 'C', 'A', 'G', 'G', 'U', 'U', 'C', 'U', 'U', 'G', 'A', 'U']) \
#         == ['G', 'A', 'G', 'U', 'G', 'A', 'A', 'G', 'G', 'U', 'C', 'C', 'A', 'A', 'G', 'A', 'A', 'C', 'U', 'A']

# def test_get_complement22():
#     assert get_complement(['C', 'G', 'A', 'C', 'G', 'C', 'A', 'C', 'U', 'C', 'U', 'G', 'G', 'C', 'U', 'C', 'C', 'U', 'G', 'U']) \
#         == ['G', 'C', 'U', 'G', 'C', 'G', 'U', 'G', 'A', 'G', 'A', 'C', 'C', 'G', 'A', 'G', 'G', 'A', 'C', 'A']


if __name__ == "__main__":
    test_search_sequence()
    test_search_sequence2()
    test_search_sequence3()
    test_search_sequence4()
    test_search_sequence5()

    test_search_sequence_empty_sequence_and_segment()
    test_search_sequence_empty_sequence()
    test_search_sequence_empty_segment()
    test_search_sequence_long_segment()
    test_search_sequence_complements()
    test_search_sequence_at_the_end()
    test_search_sequence_at_the_beginning()
    test_search_sequence_wrap_around()
    test_search_sequence_single_letter()
    test_search_sequence_lower_case()
    test_search_sequence_segement_equals_sequence()