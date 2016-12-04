"""Algorithm to solve the word game Boggle.

Solution provides a set of all allowed words found on a square Boggle board of
any size, by a recursive depth-first search. Per the rules of Boggle, words
must be at least 3 letters long, and cannot use the same tile more than once.

Access to the entire dictionary of allowed English words is provided by a Trie
data structure.

Time Complexity:
In the worst case scenario, the algorithm will explore every possible 16-letter
permutation of the board. This is gives O(n!) factorial time.

Space Complexity:
In order to obey the rule of not re-using the same tile to make a word, the
recursive search algorithm creates a new set object tracking already-visited
tiles every time it explores a new tile, meaning space complexity is also O(n!)
factorial.
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
        words = find_words(y, x, char, set(), board, ALL_WORDS)
        found_words.update(words)
    return found_words


def find_words(y, x, chars, visited, board, all_words):
    """Return words found recursively from the given y, x position."""
    if len(chars) >= MIN_WORD_LEN and all_words.contains(chars):
        found_words = {chars}
    else:
        found_words = set()

    visited.add((y, x))

    for n_y, n_x, n_char in neighbors(y, x, board):
        if (n_y, n_x) in visited:
            continue
        n_chars = chars + n_char
        if not all_words.contains_prefix(n_chars):
            continue
        # Necessary to create multiple copies of the visited set, since
        # different recursive branches will traverse grid in different order
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
    """Return generator of all neighbor coords and chars of given coord."""
    size = len(board)
    mods = (-1, 0, 1)
    for y_mod, x_mod in product(mods, mods):
        n_y, n_x = y + y_mod, x + x_mod
        if any((n_y < 0,  n_y >= size, n_x < 0, n_x >= size)):
            continue
        yield n_y, n_x, board[n_y][n_x]
