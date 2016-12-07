"""Code challenge: create a square array with a spiral from the given size."""
from itertools import cycle, chain


def spiralize(size):
    """Return list of lists -- 2D grid -- with a spiral of 1s starting in topleft."""
    grid = initialize_grid(size)


def initialize_grid(size):
    """Create the initial grid with blank spaces."""
    return [[0] * size for _ in range(size)]


def move_and_write(moves, direction, y, x):
    """Move the given number of moves/direction starting from y, x, setting coords to 1."""


def generate_sequence(size):
    """Return a generator of the correct moves to make a spiral."""
    for n, flag in zip(range(size - 1, 1, -1), cycle((0, 1))):
        if flag:
            yield n - 1
        else:
            yield n
