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
    ),
    (
        [['-', 'l', '-', '-'],
         ['-', 'a', 't', '-'],
         ['-', 's', 'e', '-'],
         ['-', '-', '-', '-']],
        {'steal', 'teal', 'late', 'ate', 'tea', 'teas', 'last', 'east', 'eat',
         'seat', 'sate', 'seal', 'sat', 'salt', 'lats', 'eta', 'sea', 'eats',
         'set'}
    )
]


@pytest.mark.parametrize('board, words', CASES)
def test_solve_boggle_board(board, words):
    """Test that the correct set of words is returned for a given board."""
    assert solve_boggle_board(board) == words
