"""Algorithm to solve a square boggle board of any size.

Provides access to the entire dictionary of allowed English words in a Trie
data structure.

"""
from __future__ import unicode_literals, division
from itertools import product


def solve_boggle_board(board):
    """Return a set of all allowed English words found in the given board."""
    words = set()
    for y, x, letter in iter_board(board):
        visited = set()
        pass


def find_words(y, x, prefix, visited):
    """Return words found recursively from the starting position."""

    # Base case: if prefix isn't in dictionary, return nothing

    # For neighbor in neighbors NOT IN VISITED:
        # new visited set copy including y, x
        # concatenate find_words





def iter_board(board):
    """Return generator of all coords in board and letter at that coord."""
    size = len(board)
    for y, x in product(range(size), range(size)):
        yield y, x, board[y][x]
