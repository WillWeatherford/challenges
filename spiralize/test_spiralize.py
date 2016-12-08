"""Test cases for Spiralize."""
from __future__ import unicode_literals, division
import pytest

CASES = [
    (1, [[1]]),
    (2, [[1, 1],
         [0, 1]]),
    (3, [[1, 1, 1],
         [0, 0, 1],
         [1, 1, 1]]),
    (4, [[1, 1, 1, 1],
         [0, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 1, 1, 1]]),
    (5, [[1, 1, 1, 1, 1],
         [0, 0, 0, 0, 1],
         [1, 1, 1, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1]]),
    (8, [[1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 1],
         [1, 0, 1, 0, 0, 1, 0, 1],
         [1, 0, 1, 1, 1, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1]]),
]

SEQUENCE_CASES = [
    (1, []),
    (2, []),
    (3, [2]),
    (4, [3, 1]),
    (5, [4, 2, 2]),
    (8, [7, 5, 5, 3, 3, 1]),
]


@pytest.mark.parametrize('size, sequence', SEQUENCE_CASES)
def test_gen_sequence(size, sequence):
    """Test that correct sequence to move around spiral is generated."""
    from spiralize import generate_sequence
    assert list(generate_sequence(size)) == sequence


# @pytest.mark.parametrize('size, result', CASES)
# def test_spiralize(size, result):
#     """Test that spiral of given size is created correctly."""
#     from spiralize import spiralize
#     assert spiralize(size) == result
