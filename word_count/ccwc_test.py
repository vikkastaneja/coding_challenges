import sys
import os

from ccwc import word_count

def test_word_count():
    sys.argv = ["ccwc.py", "-c", os.path.dirname(__file__) + "/test.txt"]
    actual = word_count(sys.argv)

    assert actual == 12, "Results are different"