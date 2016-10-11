"""Test suite for alternating array challenge."""
from __future__ import unicode_literals, division, print_function

from alternating_array import alternate_iter


def test_basic_1():
    """Simple test on odd number of values."""
    assert alternate_iter([1, 3, 6, 9, -3]) == [9, -3, 6, 1, 3]


def test_basic_2():
    """Simple test on odd number of values."""
    assert alternate_iter([1, 6, 9, -3]) == [9, -3, 6, 1]
