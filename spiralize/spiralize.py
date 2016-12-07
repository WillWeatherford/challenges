"""Code challenge: create a square array with a spiral from the given size."""
from itertools import cycle, chain

DIRECTIONS = [
    lambda y, x: (y, x + 1),
    lambda y, x: (y + 1, x),
    lambda y, x: (y, x - 1),
    lambda y, x: (y - 1, x),
]


def spiralize(size):
    """Return list of lists -- 2D grid -- with a spiral of 1s starting in topleft."""
    grid = initialize_grid(size)
    seq = chain((size, size - 1), generate_sequence(size))
    seq = zip(cycle(DIRECTIONS), seq)
    y, x = 0, -1
    for direction, num_moves in seq:
        y, x = move_and_write(num_moves, direction, y, x, grid)



def initialize_grid(size):
    """Create the initial grid with blank spaces."""
    return [[0] * size for _ in range(size)]


def move_and_write(num_moves, direction, y, x, grid):
    """Move the given number of moves/direction starting from y, x, setting coords to 1."""


def generate_sequence(size):
    """Return a generator of the correct moves to make a spiral."""
    for n, flag in zip(range(size - 1, 1, -1), cycle((0, 1))):
        if flag:
            yield n - 1
        else:
            yield n
