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
    sequence = chain((size, size - 1), generate_sequence(size))
    moves = zip(cycle(DIRECTIONS), sequence)
    y, x = 0, -1
    for direction, num_moves in moves:
        y, x = move_and_write(num_moves, direction, y, x, grid)
    return grid


def initialize_grid(size):
    """Create the initial grid with blank spaces."""
    return [[0] * size for _ in range(size)]


def move_and_write(num_moves, direction, y, x, grid):
    """Move given number of moves/direction, setting values on grid to 1."""
    for _ in range(num_moves):
        y, x = direction(y, x)
        grid[y][x] = 1
    return y, x


def generate_sequence(size):
    """Return a generator of the correct moves to make a spiral."""
    for n, flag in zip(range(size - 1, 1, -1), cycle((0, 1))):
        if flag:
            yield n - 1
        else:
            yield n
