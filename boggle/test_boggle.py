"""Test solutions for boggle solving algorithm."""

from __future__ import unicode_literals, division
import pytest
from boggle import solve_boggle_board

CASES = [
    (
        [[]], set()
    ),
    (
        [['a']], set()
    ),
    (
        [['o', 'n'],
         ['t', 'a']],
        {'ton', 'tan', 'ant', 'oat', 'not'}
    ),
    (
        [['a', 'x'],
         ['x', 'e']],
        {'axe'}
    ),
    (
        [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']],
        set()
    ),
    (
        [['c', 'a', 't'],
         ['-', '-', 's'],
         ['-', '-', '-']],
        {'cat', 'cats', 'cast', 'sat', 'sac'}
    )
]


@pytest.mark.parametrize('board, words', CASES)
def test_solve_boggle_board(board, words):
    """Test that the correct set of words is returned for a given board."""
    assert solve_boggle_board(board) == words
