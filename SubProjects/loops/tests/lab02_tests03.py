import random
import pytest

import sys

sys.path.insert(0, '../lab02_loops')
from lab02 import get_similarity_score

def test_get_similarity_score_one_letter():
    assert get_similarity_score(["A"], ["A"]) == 1

def test_get_similarity_score_complement():
    assert get_similarity_score(['C', 'G', 'A', 'C', 'G', 'C', 'A', 'C', 'U', 'C', 'U', 'G', 'G', 'C', 'U', 'C', 'C', 'U', 'G', 'U'], \
        ['G', 'C', 'U', 'G', 'C', 'G', 'U', 'G', 'A', 'G', 'A', 'C', 'C', 'G', 'A', 'G', 'G', 'A', 'C', 'A']) == 0

def test_get_similarity_score():
    assert get_similarity_score(['C', 'U', 'A', 'G', 'C', 'A', 'U', 'G', 'U', 'C', 'C', 'C', 'A', 'C', 'A', 'A', 'G', 'U', 'C', 'G'], \
        ['G', 'G', 'U', 'A', 'C', 'C', 'A', 'A', 'U', 'U', 'G', 'G', 'A', 'C', 'U', 'G', 'G', 'U', 'U', 'G']) == 0.35

def test_get_similarity_score2():
    assert get_similarity_score(['U', 'G', 'U', 'U', 'G', 'C', 'A', 'G', 'A', 'C', 'U', 'C', 'U', 'C', 'G', 'U', 'G', 'A', 'U', 'G'], \
        ['C', 'C', 'G', 'A', 'A', 'A', 'A', 'A', 'U', 'U', 'A', 'C', 'G', 'A', 'G', 'C', 'U', 'C', 'U', 'C']) == 0.2

def test_get_similarity_score3():
    assert get_similarity_score(['G', 'U', 'G', 'A', 'A', 'C', 'G', 'G', 'U', 'U', 'C', 'G', 'U', 'A', 'G', 'A', 'U', 'G', 'C', 'C'], \
        ['A', 'U', 'C', 'U', 'U', 'C', 'G', 'C', 'C', 'C', 'U', 'C', 'A', 'A', 'G', 'A', 'A', 'G', 'C', 'A']) == 0.4

def test_get_similarity_score4():
    assert get_similarity_score(['G', 'A', 'A', 'U', 'A', 'C', 'C', 'U', 'U', 'G', 'G', 'A', 'U', 'U', 'C', 'G', 'A', 'U', 'C', 'A'], \
        ['C', 'U', 'C', 'A', 'C', 'A', 'U', 'C', 'A', 'A', 'A', 'U', 'U', 'G', 'U', 'A', 'U', 'A', 'U', 'G']) == 0.05

def test_get_similarity_score5():
    assert get_similarity_score(['C', 'C', 'C', 'U', 'U', 'A', 'A', 'G', 'U', 'G', 'A', 'A', 'A', 'A', 'A', 'G', 'C', 'A', 'A', 'A'], \
        ['G', 'U', 'G', 'U', 'U', 'C', 'A', 'U', 'U', 'A', 'U', 'C', 'U', 'U', 'C', 'A', 'U', 'A', 'G', 'G']) == 0.25

def test_get_similarity_score6():
    assert get_similarity_score(['A', 'G', 'C', 'U', 'U', 'U', 'U', 'U', 'G', 'A', 'G', 'C', 'C', 'A', 'C', 'A', 'C', 'A', 'A', 'A'], \
        ['C', 'U', 'A', 'C', 'U', 'G', 'G', 'C', 'U', 'U', 'A', 'U', 'C', 'C', 'A', 'C', 'A', 'A', 'U', 'C']) == 0.15

def test_get_similarity_score7():
    assert get_similarity_score(['A', 'A', 'G', 'A', 'A', 'A', 'U', 'G', 'G', 'G', 'U', 'C', 'G', 'G', 'G', 'C', 'C', 'U', 'A', 'G'], \
        ['U', 'G', 'G', 'C', 'G', 'A', 'U', 'G', 'G', 'C', 'U', 'C', 'A', 'U', 'A', 'A', 'C', 'C', 'A', 'A']) == 0.45

def test_get_similarity_score8():
    assert get_similarity_score(['C', 'G', 'U', 'C', 'G', 'C', 'C', 'A', 'U', 'C', 'A', 'A', 'C', 'U', 'C', 'A', 'G', 'A', 'C', 'A'], \
        ['C', 'G', 'A', 'U', 'G', 'C', 'C', 'G', 'C', 'G', 'C', 'A', 'U', 'C', 'A', 'G', 'G', 'C', 'A', 'U']) == 0.35

def test_get_similarity_score9():
    assert get_similarity_score(['C', 'C', 'U', 'A', 'A', 'C', 'G', 'A', 'G', 'C', 'C', 'C', 'U', 'U', 'A', 'G', 'A', 'G', 'G', 'C'], \
        ['G', 'U', 'G', 'U', 'C', 'G', 'G', 'C', 'U', 'G', 'U', 'C', 'U', 'C', 'C', 'U', 'U', 'C', 'C', 'G']) == 0.15

def test_get_similarity_score10():
    assert get_similarity_score(['C', 'C', 'A', 'U', 'C', 'G', 'G', 'U', 'C', 'G', 'G', 'A', 'C', 'A', 'A', 'U', 'U', 'U', 'A', 'G'], \
        ['C', 'G', 'G', 'U', 'A', 'A', 'A', 'U', 'U', 'U', 'C', 'A', 'A', 'U', 'C', 'C', 'G', 'A', 'A', 'A']) == 0.25

def test_get_similarity_score11():
    assert get_similarity_score(['U', 'U', 'A', 'A', 'C', 'C', 'C', 'G', 'G', 'C', 'A', 'A', 'G', 'A', 'C', 'G', 'G', 'C', 'G', 'A'], \
        ['C', 'G', 'C', 'U', 'C', 'G', 'U', 'U', 'G', 'U', 'A', 'G', 'A', 'U', 'C', 'G', 'C', 'C', 'C', 'U']) == 0.3

def test_get_similarity_score12():
    assert get_similarity_score(['A', 'G', 'U', 'A', 'C', 'G', 'C', 'G', 'U', 'G', 'C', 'C', 'C', 'A', 'C', 'U', 'U', 'A', 'C', 'G'], \
        ['G', 'U', 'A', 'A', 'C', 'A', 'C', 'G', 'C', 'A', 'G', 'A', 'A', 'G', 'U', 'U', 'C', 'U', 'C', 'U']) == 0.3

def test_get_similarity_score13():
    assert get_similarity_score(['U', 'G', 'C', 'C', 'A', 'C', 'U', 'A', 'C', 'U', 'G', 'G', 'C', 'A', 'C', 'G', 'C', 'G', 'U', 'G'], \
        ['C', 'G', 'A', 'U', 'U', 'C', 'U', 'C', 'C', 'C', 'C', 'A', 'A', 'A', 'C', 'A', 'C', 'A', 'U', 'G']) == 0.45

def test_get_similarity_score14():
    assert get_similarity_score(['C', 'C', 'G', 'C', 'G', 'U', 'U', 'G', 'U', 'A', 'G', 'U', 'U', 'C', 'G', 'C', 'G', 'U', 'U', 'G'], \
        ['A', 'A', 'A', 'U', 'G', 'G', 'G', 'C', 'C', 'C', 'U', 'U', 'G', 'U', 'A', 'A', 'A', 'A', 'G', 'U']) == 0.1

def test_get_similarity_score15():
    assert get_similarity_score(['C', 'A', 'U', 'G', 'G', 'G', 'U', 'U', 'C', 'G', 'A', 'C', 'G', 'U', 'G', 'U', 'G', 'G', 'G', 'U'], \
        ['U', 'C', 'A', 'A', 'G', 'G', 'C', 'A', 'U', 'A', 'C', 'A', 'G', 'A', 'C', 'C', 'G', 'C', 'C', 'G']) == 0.2

def test_get_similarity_score16():
    assert get_similarity_score(['C', 'C', 'C', 'A', 'A', 'G', 'U', 'A', 'G', 'C', 'G', 'G', 'C', 'U', 'C', 'A', 'G', 'C', 'A', 'U'], \
        ['G', 'G', 'U', 'G', 'A', 'U', 'U', 'A', 'U', 'G', 'C', 'G', 'A', 'A', 'C', 'G', 'C', 'A', 'A', 'A']) == 0.3

def test_get_similarity_score17():
    assert get_similarity_score(['A', 'C', 'G', 'A', 'G', 'U', 'A', 'C', 'A', 'U', 'A', 'C', 'C', 'U', 'G', 'U', 'U', 'G', 'A', 'U'], \
        ['C', 'C', 'G', 'U', 'C', 'G', 'C', 'G', 'A', 'G', 'A', 'U', 'G', 'A', 'U', 'A', 'U', 'C', 'U', 'G']) == 0.25

def test_get_similarity_score18():
    assert get_similarity_score(['U', 'C', 'G', 'G', 'G', 'C', 'G', 'C', 'A', 'C', 'U', 'C', 'U', 'U', 'G', 'U', 'G', 'A', 'G', 'A'], \
        ['A', 'A', 'A', 'A', 'U', 'C', 'A', 'C', 'C', 'U', 'U', 'A', 'U', 'U', 'G', 'G', 'G', 'C', 'A', 'C']) == 0.35

def test_get_similarity_score19():
    assert get_similarity_score(['C', 'G', 'A', 'U', 'G', 'C', 'C', 'U', 'G', 'U', 'A', 'U', 'U', 'C', 'U', 'C', 'G', 'C', 'C', 'C'], \
        ['U', 'A', 'U', 'A', 'U', 'G', 'C', 'C', 'A', 'U', 'U', 'U', 'U', 'G', 'G', 'A', 'A', 'U', 'A', 'A']) == 0.2

def test_get_similarity_score20():
    assert get_similarity_score(['C', 'U', 'U', 'C', 'C', 'G', 'G', 'U', 'C', 'C', 'C', 'G', 'A', 'G', 'A', 'U', 'C', 'G', 'U', 'U'], \
        ['U', 'C', 'A', 'C', 'C', 'A', 'U', 'C', 'C', 'A', 'C', 'A', 'G', 'A', 'U', 'C', 'U', 'C', 'C', 'U']) == 0.25