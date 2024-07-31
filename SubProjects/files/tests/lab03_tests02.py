import random
import pytest
import string

import sys

sys.path.insert(0, '../lab03_files')
from lab03 import can_hide_ransom_message

# def generate_test_files():
#     for i in range(20):
#         file = open(f"lab03_files/tests/test_file{i}.txt", "w")
#         file.write(''.join(random.choices(string.ascii_uppercase + string.digits, k=100)))
#         file.write("\n")
#         file.close()

def test_can_hide_ransom_message_empty():
    assert can_hide_ransom_message("", "tests/test_files_2/test_file0.txt") == True

def test_can_hide_ransom_message():
    assert can_hide_ransom_message("I6X4TIK", \
        "tests/test_files_2/test_file0.txt") == True

def test_can_hide_ransom_message2():
    assert can_hide_ransom_message("this is a test", "tests/test_files_2/test_file1.txt") == False

def test_can_hide_ransom_message3():
    assert can_hide_ransom_message("ABCDEFGHIJKLMNOPQRSTUVWXYZ", \
        "tests/test_files_2/test_file2.txt") == False

def test_can_hide_ransom_message4():
    assert can_hide_ransom_message("YPIK8ZHHDK71CU686ZMDPZ8P2RZ3R6P60L480RQIZV93HCE1DJ7S8WQ0NV4LATV1ICR6JRR68F05011VFGPV7HWPRXE9BBLKA0DD", \
        "tests/test_files_2/test_file3.txt") == True

def test_can_hide_ransom_message5():
    assert can_hide_ransom_message("75KEBVCVZWMZTUCTJL3XAS5FJ0P3N", \
        "tests/test_files_2/test_file4.txt") == True

def test_can_hide_ransom_message6():
    assert can_hide_ransom_message("VVDY14Z2OYN5GW3ORLI", \
        "tests/test_files_2/test_file5.txt") == True

def test_can_hide_ransom_message7():
    assert can_hide_ransom_message("YPIK8ZHHDK71CU686ZMDPZ8P2RZ3R6P60L480RQIZV93HCE1DJ7S8WQ0NV4LATV1ICR6JRR68F05011VFGPV7HWPRXE9BBLKA0DD", \
        "tests/test_files_2/test_file6.txt") == False

def test_can_hide_ransom_message8():
    assert can_hide_ransom_message("KNTLCESEBWCYSRFPRVU80", \
        "tests/test_files_2/test_file7.txt") == True

def test_can_hide_ransom_message9():
    assert can_hide_ransom_message("NT0B4CF7MRFXR8T", \
        "tests/test_files_2/test_file8.txt") == True



