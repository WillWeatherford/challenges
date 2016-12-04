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
        [['x', 'x', 'x'],
         ['x', 'x', 'x'],
         ['x', 'x', 'x']],
        set()
    ),
    (
        [['c', 'a', 't'],
         ['x', 'x', 's'],
         ['x', 'x', 'x']],
        {'cat', 'cats', 'cast', 'sat'}
    )
]


@pytest.mark.parametrize('board, words', CASES)
def test_solve_boggle_board(board, words):
    """Test that the correct set of words is returned for a given board."""
    assert solve_boggle_board(board) == words
