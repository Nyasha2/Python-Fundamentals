import random
import pytest

import sys

sys.path.insert(0, '../lab02_loops')
from lab02 import get_complement

def test_get_complement_empty():
    assert get_complement([]) == []

def test_get_complement2():
    assert get_complement(["U", "A", "C", "G"]) == ["A", "U", "G", "C"]

def test_get_complement3():
    assert get_complement(['C', 'C', 'U', 'G', 'C', 'C', 'C', 'G', 'G', 'G', 'U', 'C', 'A', 'C', 'U', 'G', 'U', 'C', 'C', 'U']) \
        == ['G', 'G', 'A', 'C', 'G', 'G', 'G', 'C', 'C', 'C', 'A', 'G', 'U', 'G', 'A', 'C', 'A', 'G', 'G', 'A']

def test_get_complement4():
    assert get_complement(['U', 'U', 'C', 'G', 'A', 'A', 'A', 'G', 'C', 'U', 'A', 'G', 'C', 'G', 'C', 'G', 'A', 'U', 'U', 'C']) \
        == ['A', 'A', 'G', 'C', 'U', 'U', 'U', 'C', 'G', 'A', 'U', 'C', 'G', 'C', 'G', 'C', 'U', 'A', 'A', 'G']

def test_get_complement5():
    assert get_complement(['A', 'C', 'C', 'C', 'C', 'C', 'A', 'A', 'U', 'U', 'G', 'A', 'G', 'A', 'A', 'U', 'A', 'G', 'C', 'G']) \
        == ['U', 'G', 'G', 'G', 'G', 'G', 'U', 'U', 'A', 'A', 'C', 'U', 'C', 'U', 'U', 'A', 'U', 'C', 'G', 'C']

def test_get_complement6():
    assert get_complement(['C', 'U', 'U', 'A', 'A', 'U', 'A', 'U', 'G', 'A', 'A', 'C', 'G', 'A', 'A', 'C', 'G', 'A', 'G', 'C']) \
        == ['G', 'A', 'A', 'U', 'U', 'A', 'U', 'A', 'C', 'U', 'U', 'G', 'C', 'U', 'U', 'G', 'C', 'U', 'C', 'G']

def test_get_complement7():
    assert get_complement(['G', 'G', 'G', 'A', 'U', 'G', 'A', 'C', 'C', 'C', 'C', 'G', 'U', 'G', 'C', 'G', 'C', 'G', 'G', 'A']) \
        == ['C', 'C', 'C', 'U', 'A', 'C', 'U', 'G', 'G', 'G', 'G', 'C', 'A', 'C', 'G', 'C', 'G', 'C', 'C', 'U']

def test_get_complement8():
    assert get_complement(['C', 'C', 'C', 'C', 'A', 'C', 'A', 'U', 'A', 'G', 'C', 'G', 'A', 'G', 'C', 'A', 'U', 'C', 'C', 'A']) \
        == ['G', 'G', 'G', 'G', 'U', 'G', 'U', 'A', 'U', 'C', 'G', 'C', 'U', 'C', 'G', 'U', 'A', 'G', 'G', 'U']

def test_get_complement9():
    assert get_complement(['A', 'G', 'G', 'C', 'G', 'A', 'A', 'C', 'U', 'G', 'C', 'A', 'U', 'A', 'A', 'C', 'U', 'A', 'C', 'C']) \
        == ['U', 'C', 'C', 'G', 'C', 'U', 'U', 'G', 'A', 'C', 'G', 'U', 'A', 'U', 'U', 'G', 'A', 'U', 'G', 'G']

def test_get_complement10():
    assert get_complement(['A', 'A', 'U', 'A', 'U', 'C', 'C', 'U', 'G', 'G', 'A', 'A', 'G', 'U', 'A', 'G', 'C', 'A', 'A', 'G']) \
        == ['U', 'U', 'A', 'U', 'A', 'G', 'G', 'A', 'C', 'C', 'U', 'U', 'C', 'A', 'U', 'C', 'G', 'U', 'U', 'C']

def test_get_complement11():
    assert get_complement(['U', 'C', 'A', 'G', 'C', 'A', 'U', 'C', 'C', 'U', 'A', 'C', 'U', 'U', 'U', 'G', 'G', 'A', 'U', 'A']) \
        == ['A', 'G', 'U', 'C', 'G', 'U', 'A', 'G', 'G', 'A', 'U', 'G', 'A', 'A', 'A', 'C', 'C', 'U', 'A', 'U']

def test_get_complement12():
    assert get_complement(['G', 'C', 'U', 'G', 'U', 'G', 'G', 'A', 'C', 'C', 'A', 'C', 'A', 'G', 'G', 'C', 'C', 'C', 'G', 'G']) \
        == ['C', 'G', 'A', 'C', 'A', 'C', 'C', 'U', 'G', 'G', 'U', 'G', 'U', 'C', 'C', 'G', 'G', 'G', 'C', 'C']

def test_get_complement13():
    assert get_complement(['C', 'U', 'U', 'U', 'G', 'U', 'U', 'C', 'A', 'G', 'C', 'U', 'A', 'A', 'A', 'C', 'G', 'C', 'U', 'C']) \
        == ['G', 'A', 'A', 'A', 'C', 'A', 'A', 'G', 'U', 'C', 'G', 'A', 'U', 'U', 'U', 'G', 'C', 'G', 'A', 'G']

def test_get_complement14():
    assert get_complement(['G', 'A', 'A', 'C', 'G', 'U', 'G', 'C', 'A', 'U', 'U', 'G', 'U', 'C', 'G', 'C', 'C', 'C', 'U', 'A']) \
        == ['C', 'U', 'U', 'G', 'C', 'A', 'C', 'G', 'U', 'A', 'A', 'C', 'A', 'G', 'C', 'G', 'G', 'G', 'A', 'U']

def test_get_complement15():
    assert get_complement(['G', 'U', 'G', 'G', 'U', 'C', 'G', 'A', 'C', 'G', 'G', 'G', 'U', 'A', 'C', 'C', 'C', 'A', 'C', 'U']) \
        == ['C', 'A', 'C', 'C', 'A', 'G', 'C', 'U', 'G', 'C', 'C', 'C', 'A', 'U', 'G', 'G', 'G', 'U', 'G', 'A']

def test_get_complement16():
    assert get_complement(['G', 'U', 'A', 'A', 'U', 'G', 'A', 'A', 'G', 'A', 'G', 'U', 'A', 'A', 'G', 'A', 'U', 'C', 'G', 'C']) \
        == ['C', 'A', 'U', 'U', 'A', 'C', 'U', 'U', 'C', 'U', 'C', 'A', 'U', 'U', 'C', 'U', 'A', 'G', 'C', 'G']

def test_get_complement17():
    assert get_complement(['A', 'G', 'A', 'A', 'C', 'A', 'C', 'A', 'A', 'A', 'G', 'G', 'U', 'U', 'C', 'A', 'G', 'U', 'G', 'U']) \
        == ['U', 'C', 'U', 'U', 'G', 'U', 'G', 'U', 'U', 'U', 'C', 'C', 'A', 'A', 'G', 'U', 'C', 'A', 'C', 'A']

def test_get_complement18():
    assert get_complement(['C', 'G', 'A', 'C', 'C', 'C', 'U', 'G', 'C', 'C', 'U', 'A', 'A', 'A', 'C', 'C', 'U', 'U', 'A', 'C']) \
        == ['G', 'C', 'U', 'G', 'G', 'G', 'A', 'C', 'G', 'G', 'A', 'U', 'U', 'U', 'G', 'G', 'A', 'A', 'U', 'G']

def test_get_complement19():
    assert get_complement(['C', 'G', 'G', 'G', 'C', 'A', 'G', 'C', 'C', 'A', 'A', 'U', 'C', 'C', 'C', 'C', 'C', 'A', 'G', 'U']) \
        == ['G', 'C', 'C', 'C', 'G', 'U', 'C', 'G', 'G', 'U', 'U', 'A', 'G', 'G', 'G', 'G', 'G', 'U', 'C', 'A']

def test_get_complement20():
    assert get_complement(['U', 'U', 'G', 'C', 'A', 'C', 'G', 'G', 'C', 'U', 'C', 'G', 'C', 'A', 'G', 'G', 'U', 'G', 'C', 'C']) \
        == ['A', 'A', 'C', 'G', 'U', 'G', 'C', 'C', 'G', 'A', 'G', 'C', 'G', 'U', 'C', 'C', 'A', 'C', 'G', 'G']

def test_get_complement21():
    assert get_complement(['C', 'U', 'C', 'A', 'C', 'U', 'U', 'C', 'C', 'A', 'G', 'G', 'U', 'U', 'C', 'U', 'U', 'G', 'A', 'U']) \
        == ['G', 'A', 'G', 'U', 'G', 'A', 'A', 'G', 'G', 'U', 'C', 'C', 'A', 'A', 'G', 'A', 'A', 'C', 'U', 'A']

def test_get_complement22():
    assert get_complement(['C', 'G', 'A', 'C', 'G', 'C', 'A', 'C', 'U', 'C', 'U', 'G', 'G', 'C', 'U', 'C', 'C', 'U', 'G', 'U']) \
        == ['G', 'C', 'U', 'G', 'C', 'G', 'U', 'G', 'A', 'G', 'A', 'C', 'C', 'G', 'A', 'G', 'G', 'A', 'C', 'A']


if __name__ == "__main__":
    test_get_complement_empty()
    test_get_complement2()
    test_get_complement3()
    test_get_complement4()
    test_get_complement5()
    test_get_complement6()
    test_get_complement7()
    test_get_complement8()
    test_get_complement9()
    test_get_complement10()
    test_get_complement11()
    test_get_complement12()
    test_get_complement13()
    test_get_complement14()
    test_get_complement15()
    test_get_complement16()
    test_get_complement17()
    test_get_complement18()
    test_get_complement19()
    test_get_complement20()
    test_get_complement21()
    test_get_complement22()