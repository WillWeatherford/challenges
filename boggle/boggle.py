"""Algorithm to solve a square boggle board of any size.

Provides access to the entire dictionary of allowed English words in a Trie
data structure.

"""
from __future__ import unicode_literals, division
from itertools import product
from words_trie import Trie

JSON_TRIE_WORDS = 'words.json'


def solve_boggle_board(board):
    """Return a set of all allowed English words found in the given board."""
    all_words = Trie(JSON_TRIE_WORDS)
    found_words = set()
    for y, x, letter in iter_board(board):
        visited = set()
        pass


def find_words(y, x, prefix, visited, all_words):
    """Return words found recursively from the starting position."""
    if not all_words.contains_prefix(prefix):
        return set()

    # Base case: if prefix isn't in dictionary, return nothing

    # For neighbor in neighbors NOT IN VISITED:
        # new visited set copy including y, x
        # concatenate find_words





def iter_board(board):
    """Return generator of all coords in board and letter at that coord."""
    size = len(board)
    for y, x in product(range(size), range(size)):
        yield y, x, board[y][x]


def neighbors(y, x, board):
    """Return generator of all coords of neighbors and letter at that coord."""
    size = len(board)
    mods = (-1, 0, 1)
    for y_mod, x_mod in product(mods, mods):
        n_y, n_x = y + y_mod, x + x_mod
        if any((n_y < 0,  n_y >= size, n_x < 0, n_x >= size)):
            continue
        yield n_y, n_x, board[n_y][n_x]
