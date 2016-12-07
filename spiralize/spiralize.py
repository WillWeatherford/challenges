"""Code challenge: create a square array with a spiral from the given size."""
from itertools import cycle


def spiralize(size):
    """Return list of lists -- 2D grid -- with a spiral of 1s starting in topleft."""


def generate_sequence(size):
    """Return a generator of the correct moves to make a spiral."""
    for n, flag in zip(range(size - 1, 1, -1), cycle((0, 1))):
        if flag:
            yield n - 1
        else:
            yield n
