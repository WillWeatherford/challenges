"""Minesweeper Solver challenge from reddit.com/r/dailyprogrammer.

In this challenge you will come up with an algorithm to solve the classic game
of Minesweeper. The brute force approach is impractical since the search space
size is anywhere around 1020 to 10100 depending on the situation, you'll have
to come up with something clever.

Input description

The current field state where each character represents one field.
Flags will not be used.
Hidden/unknown fields are denoted with a '?'.
'Zero-fields' with no mines around are denoted with a space.

Example for a 9x9 board:

  012345678
 ----------
0|    1????
1|    1????
2|    111??
3|      1??
4|1211  1??
5|???21 1??
6|????211??
7|?????????
8|?????????

Output description

A list of zero-based row and column coordinates for the fields that you have
determined to be SAFE.  The list does not need to be ordered.
For the above input example this would be:

0 5
1 6
1 7
2 7
3 7
5 1
5 7
6 2
6 7

Challenge Input

As suggested by /u/wutaki, this input is a greater challenge then the original:

??????
??F2F?
F??4?F
S2FF2S
?2222?
F1  1F

3 0
3 5
0 2
0 3
0 4

Minesweeper is a game of both logic and luck. Sometimes it is impossible to
find free fields through logic. The right output would then be an empty list.
Your algorithm does not need to guess.

Bonus

Extra hard mode: Make a closed-loop bot. It should take a screenshot, parse the
board state from the pixels, run the algorithm and manipulate the cursor to
execute the clicks.
"""
from __future__ import unicode_literals, division
from itertools import tee, product
from functools import partial

SAFE = 'S'
FLAG = 'F'
UNSOLVED = '?'


def sweep(grid):
    """Return a set of safe coordinates in the given grid."""
    safe = set()
    grid = _listify(grid)

    # Set up functions with grid argument pre-baked in using partial.
    neighbors = partial(_neighbors, grid=grid)
    lookup_cell = partial(_lookup_cell, grid=grid)
    set_cell = partial(_set_cell, grid=grid)

    # Need to evaluate all numbered cells in the grid.
    to_evaluate = set(filter(_is_numbered, _all_cells(grid)))

    while True:
        try:
            # Discard the cell value previously stored in the to_evaluate set.
            coords, _ = to_evaluate.pop()
        except KeyError:
            # When there are no more cells left to evaluate, we're done.
            break

        # Make sure to get the new cell value directly from the grid.
        cell_value = int(lookup_cell(coords))

        # Use the neighbors generator in two different filtered ways.
        n1, n2 = tee(neighbors(coords), 2)
        unsolved = set(filter(_is_unsolved, n1))
        flagged = set(filter(_is_flagged, n2))

        if len(flagged) == cell_value:
            # Deduce that all unsolved neighbor cells are safe.

            for u_coords, _ in unsolved:
                set_cell(u_coords, SAFE)
                safe.add(u_coords)

                # Re-evaluate all numbered neighbors of the newly safed cell.
                to_evaluate.update(filter(_is_numbered, neighbors(u_coords)))

        # Sanity check: if the flagged neighbors outnumber the cell, something
        # has gone horribly wrong.
        elif len(flagged) > cell_value:
            raise ValueError('More than {} flagged neighbors at {}.'
                             ''.format(cell_value, coords))

        if len(unsolved) + len(flagged) <= cell_value:
            # Deduce that these neighbors should be flagged.

            for u_coords, _ in unsolved:
                set_cell(u_coords, FLAG)

                # Re-evaluate all numbered neighbors of the newly flagged cell.
                to_evaluate.update(filter(_is_numbered, neighbors(u_coords)))

    return safe


def _lookup_cell(coords, grid=None):
    """Return the value at the given coordinates in the grid."""
    y, x = coords
    try:
        return grid[y][x]
    except IndexError:
        raise IndexError('Coordinates {} are outside the grid.'.format(coords))


def _set_cell(coords, cell_value, grid=None):
    y, x = coords
    try:
        grid[y][x] = cell_value
    except IndexError:
        raise IndexError('Coordinates {} are outside the grid.'.format(coords))


def _listify(grid):
    """Convert a string grid into a list of lists."""
    return [list(row) for row in grid.split('\n') if row]


def _all_cells(grid):
    """Generate all coordinates in the grid."""
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            yield (y, x), value


def _is_numbered(coords_and_value):
    """Return boolean of whether there is a number at given coords."""
    return coords_and_value[1].isdigit()


def _is_unsolved(coords_and_value):
    """Return boolean of whether the cell at given coords is unsolved."""
    return coords_and_value[1] == UNSOLVED


def _is_flagged(coords_and_value):
    """Return boolean of whether cell at given coords is flagged."""
    return coords_and_value[1] == FLAG


def _neighbors(coords, grid=None):
    """Generate coordinates of all 8 neighbors around given y, x coords."""
    y, x = coords
    y_range = range(max(0, y - 1), y + 2)
    x_range = range(max(0, x - 1), x + 2)
    for n_coords in product(y_range, x_range):
        if (n_coords) != coords:
            try:
                yield n_coords, _lookup_cell(n_coords, grid)
            except IndexError:
                pass
