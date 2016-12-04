"""Algorithm to solve a square boggle board of any size.

Provides access to the entire dictionary of allowed English words in a Trie
data structure.

"""
from __future__ import unicode_literals, division
from itertools import product
from words_trie import Trie

MIN_WORD_LEN = 3
JSON_TRIE_WORDS = 'words.json'
ALL_WORDS = Trie(JSON_TRIE_WORDS)


def solve_boggle_board(board):
    """Return a set of all allowed English words found in the given board."""
    found_words = set()
    for y, x, char in iter_board(board):
        found_words.update(find_words(y, x, char, set(), board, ALL_WORDS))
    return found_words


def find_words(y, x, chars, visited, board, all_words):
    """Return words found recursively from the starting position."""
    found_words = set()
    if not all_words.contains_prefix(chars):
        return found_words

    if len(chars) >= MIN_WORD_LEN and all_words.contains(chars):
        found_words.add(chars)

    visited.add((y, x))

    for n_y, n_x, n_char in neighbors(y, x, board):
        if (n_y, n_x) in visited:
            continue

        n_chars = chars + n_char
        n_visited = visited.copy()
        n_words = find_words(n_y, n_x, n_chars, n_visited, board, all_words)
        found_words.update(n_words)

    return found_words


def iter_board(board):
    """Return generator of all coords in board and char at that coord."""
    size = len(board)
    for y, x in product(range(size), range(size)):
        yield y, x, board[y][x]


def neighbors(y, x, board):
    """Return generator of all coords of neighbors and char at that coord."""
    size = len(board)
    mods = (-1, 0, 1)
    for y_mod, x_mod in product(mods, mods):
        n_y, n_x = y + y_mod, x + x_mod
        if any((n_y < 0,  n_y >= size, n_x < 0, n_x >= size)):
            continue
        yield n_y, n_x, board[n_y][n_x]
