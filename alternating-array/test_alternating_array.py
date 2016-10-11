"""Test suite for alternating array challenge."""
from __future__ import unicode_literals, division, print_function

import pytest
from alternating_array import alternate_iter, alternate_recur


@pytest.mark.parametrize('func', (alternate_iter, alternate_recur))
def test_basic_1(func):
    """Simple test on odd number of values."""
    assert func([1, 3, 6, 9, -3]) == [9, -3, 6, 1, 3]


@pytest.mark.parametrize('func', (alternate_iter, alternate_recur))
def test_basic_2(func):
    """Simple test on odd number of values."""
    assert alternate_iter([1, 6, 9, -3]) == [9, -3, 6, 1]
