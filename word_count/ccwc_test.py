import sys
import os

from ccwc import word_count
text_file = os.path.dirname(__file__) + "/test.txt"

def test_word_count_c():
    sys.argv = ["ccwc.py", "-c", text_file]
    actual = word_count(sys.argv)

    assert actual == 12, "Byte counts are different"


def test_word_count_w():
    sys.argv = ["ccwc.py", "-w", text_file]
    actual = word_count(sys.argv)

    assert actual == 2, "Word counts are different"

def test_word_count_default():
    sys.argv = ["ccwc.py", "-a", text_file]
    actual = word_count(sys.argv)

    assert actual == -1, "Default counts are different"

def test_word_count_l():
    sys.argv = ["ccwc.py", "-l", text_file]
    actual = word_count(sys.argv)

    assert actual == 1, "Line counts are different"

