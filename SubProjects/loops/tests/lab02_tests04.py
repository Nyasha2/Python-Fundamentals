import random
import pytest

import sys

sys.path.insert(0, '../lab02_loops')
from lab02 import find_close_contacts

def generate_random_sequence():
    random_sequence = []
    for _ in range(10):
        random_sequence.append(random.choice(["U", "A", "C", "G"]))
    return random_sequence

def test_find_close_contacts_empty_infected():
    assert find_close_contacts([["U", "A", "C"], ["G", "C", "A"]], []) == []

def test_find_close_contacts():
    assert find_close_contacts(['U', 'G', 'U', 'G', 'A', 'A', 'U', 'A', 'C', 'A'], \
        [['U', 'U', 'C', 'A', 'A', 'U', 'C', 'U', 'A', 'A'], \
        ['A', 'G', 'A', 'C', 'G', 'A', 'C', 'G', 'C', 'G'], \
        ['A', 'C', 'C', 'U', 'C', 'A', 'A', 'U', 'C', 'U'], \
        ['G', 'A', 'A', 'G', 'C', 'C', 'U', 'C', 'A', 'G'], \
        ['U', 'G', 'U', 'G', 'A', 'A', 'U', 'A', 'C', 'A']]) == [4]


def test_find_close_contacts2():
    assert find_close_contacts(['G', 'A', 'C', 'G', 'A', 'U', 'U', 'U', 'U', 'A'], \
        [['U', 'C', 'U', 'U', 'A', 'G', 'C', 'G', 'A', 'C'], \
        ['C', 'A', 'A', 'A', 'A', 'A', 'G', 'G', 'A', 'U'], \
        ['A', 'G', 'G', 'U', 'C', 'A', 'C', 'A', 'U', 'G'], \
        ['G', 'A', 'C', 'G', 'A', 'U', 'U', 'U', 'U', 'A'], \
        ['G', 'G', 'G', 'U', 'C', 'G', 'C', 'A', 'G', 'A']]) == [3]


def test_find_close_contacts3():
    assert find_close_contacts(['A', 'G', 'C', 'A', 'A', 'U', 'A', 'C', 'G', 'C'], \
        [['U', 'A', 'G', 'G', 'G', 'C', 'U', 'C', 'A', 'C'], \
        ['A', 'G', 'C', 'G', 'C', 'G', 'U', 'G', 'U', 'C'], \
        ['U', 'G', 'A', 'C', 'U', 'A', 'G', 'C', 'A', 'A'], \
        ['A', 'G', 'C', 'A', 'A', 'U', 'A', 'C', 'G', 'C'], \
        ['A', 'G', 'C', 'A', 'A', 'U', 'A', 'C', 'G', 'C']]) == [3, 4]

def test_find_close_contacts4():
    assert find_close_contacts(['G', 'A', 'C', 'C', 'C', 'U', 'C', 'U', 'U', 'G'], \
        [['A', 'U', 'C', 'U', 'G', 'C', 'G', 'C', 'U', 'C'], \
        ['A', 'U', 'A', 'A', 'C', 'C', 'U', 'U', 'A', 'G'], \
        ['C', 'C', 'A', 'C', 'A', 'C', 'C', 'G', 'C', 'A'], \
        ['A', 'A', 'G', 'A', 'C', 'C', 'A', 'A', 'U', 'C']]) == []


def test_find_close_contacts5():
    assert find_close_contacts(['C', 'U', 'C', 'G', 'C', 'G', 'G', 'G', 'C', 'A'], \
        [['C', 'U', 'C', 'G', 'C', 'G', 'G', 'G', 'C', 'A'], \
        ['C', 'U', 'C', 'G', 'C', 'G', 'G', 'G', 'C', 'A'], \
        ['C', 'U', 'C', 'G', 'C', 'G', 'G', 'G', 'C', 'A'], \
        ['C', 'U', 'C', 'G', 'C', 'G', 'G', 'G', 'C', 'A']]) == [0, 1, 2, 3]

def test_find_close_contacts6():
    assert find_close_contacts(['U', 'C', 'U', 'U', 'C', 'C', 'U', 'A', 'G', 'G'], \
        [['U', 'C', 'U', 'U', 'C', 'C', 'U', 'A', 'G', 'G'], \
        ['U', 'A', 'G', 'G', 'U', 'U', 'C', 'U', 'C', 'C'], \
        ['C', 'G', 'U', 'U', 'A', 'U', 'A', 'A', 'A', 'G'], \
        ['G', 'C', 'G', 'G', 'C', 'G', 'C', 'U', 'C', 'A'], \
        ['U', 'C', 'U', 'U', 'C', 'C', 'U', 'A', 'G', 'G']]) == [0, 4]

def test_find_close_contacts7():
    assert find_close_contacts(['A', 'U', 'U', 'U', 'A', 'G', 'A', 'C', 'C', 'G'], \
        [['U', 'A', 'U', 'A', 'C', 'A', 'U', 'G', 'U', 'A'], \
        ['A', 'U', 'U', 'U', 'A', 'G', 'A', 'C', 'C', 'G'], \
        ['A', 'U', 'U', 'U', 'A', 'G', 'A', 'C', 'C', 'G'], \
        ['A', 'U', 'U', 'U', 'A', 'G', 'A', 'C', 'C', 'G']]) == [1, 2, 3]

def test_find_close_contacts8():
    assert find_close_contacts(['U', 'U', 'U', 'C', 'C', 'A', 'U', 'G', 'U', 'C'], \
        [['G', 'G', 'C', 'G', 'U', 'U', 'U', 'G', 'C', 'U'], \
        ['G', 'U', 'U', 'A', 'A', 'U', 'U', 'A', 'G', 'G'], \
        ['U', 'U', 'U', 'C', 'C', 'A', 'U', 'G', 'U', 'C'], \
        ['U', 'A', 'A', 'C', 'U', 'U', 'A', 'U', 'G', 'U'], \
        ['G', 'G', 'C', 'G', 'U', 'U', 'U', 'G', 'C', 'U']]) == [2]

def test_find_close_contacts9():
    assert find_close_contacts(['A', 'U', 'A', 'C', 'G', 'U', 'G', 'A', 'G', 'U'], \
        [['C', 'A', 'C', 'C', 'G', 'C', 'G', 'A', 'G', 'A'], \
        ['G', 'C', 'C', 'U', 'G', 'G', 'G', 'A', 'G', 'U'], \
        ['U', 'G', 'A', 'U', 'C', 'U', 'U', 'C', 'C', 'A'], \
        ['A', 'U', 'C', 'U', 'U', 'C', 'G', 'U', 'G', 'C'], \
        ['A', 'U', 'A', 'C', 'G', 'U', 'G', 'A', 'G', 'U']]) == [4]

def test_find_close_contacts10():
    assert find_close_contacts(['C', 'A', 'U', 'G', 'G', 'A', 'G', 'U', 'G', 'C'], \
        [['A', 'A', 'G', 'A', 'A', 'G', 'G', 'U', 'C', 'C'], \
        ['G', 'G', 'A', 'C', 'G', 'A', 'U', 'U', 'C', 'A'], \
        ['C', 'A', 'C', 'C', 'G', 'U', 'G', 'G', 'G', 'A'], \
        ['U', 'A', 'C', 'C', 'G', 'A', 'G', 'U', 'G', 'G'], \
        ['C', 'A', 'U', 'G', 'G', 'A', 'G', 'U', 'G', 'C'], \
        ['A', 'A', 'G', 'A', 'A', 'G', 'G', 'U', 'C', 'C'], \
        ['G', 'G', 'A', 'C', 'G', 'A', 'U', 'U', 'C', 'A'], \
        ['C', 'A', 'C', 'C', 'G', 'U', 'G', 'G', 'G', 'A'], \
        ['U', 'A', 'C', 'C', 'G', 'A', 'G', 'U', 'G', 'G'], \
        ['C', 'A', 'U', 'G', 'G', 'A', 'G', 'U', 'G', 'C']]) == [4, 9]

def test_find_close_contacts11():
    assert find_close_contacts(['G', 'U', 'G', 'C', 'U', 'U', 'A', 'A', 'G', 'G'], \
        [['G', 'U', 'G', 'C', 'U', 'U', 'A', 'A', 'G', 'G']]) == [0]

def test_find_close_contacts12():
    assert find_close_contacts(['A', 'G', 'U', 'G', 'U', 'U', 'C', 'C', 'C', 'U'], \
        [['C', 'A', 'C', 'U', 'U', 'G', 'U', 'G', 'C', 'A'], \
        ['G', 'C', 'C', 'G', 'U', 'U', 'C', 'C', 'C', 'C'], \
        ['A', 'G', 'U', 'G', 'U', 'U', 'C', 'C', 'C', 'U'], \
        ['A', 'A', 'G', 'U', 'U', 'G', 'C', 'G', 'G', 'U'], \
        ['A', 'G', 'U', 'G', 'U', 'U', 'C', 'C', 'C', 'U']]) == [2, 4]

def test_find_close_contacts13():
    assert find_close_contacts(['G', 'C', 'G', 'G', 'G', 'G', 'C', 'A', 'G', 'A'], \
        [['G', 'C', 'G', 'G', 'G', 'G', 'C', 'A', 'G', 'A'], \
        ['U', 'A', 'C', 'G', 'G', 'A', 'A', 'C', 'A', 'A'], \
        ['C', 'A', 'A', 'U', 'C', 'C', 'G', 'C', 'U', 'C'], \
        ['G', 'C', 'C', 'A', 'C', 'U', 'C', 'U', 'C', 'C'], \
        ['A', 'C', 'U', 'U', 'G', 'G', 'C', 'A', 'U', 'G']]) == [0]