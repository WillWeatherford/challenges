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

Challenge input

As suggested by /u/wutaki, this input is a greater challenge then the original:

??????
???2??
???4??
?2??2?
?2222?
?1  1?

Minesweeper is a game of both logic and luck. Sometimes it is impossible to
find free fields through logic. The right output would then be an empty list.
Your algorithm does not need to guess.

Bonus

Extra hard mode: Make a closed-loop bot. It should take a screenshot, parse the
board state from the pixels, run the algorithm and manipulate the cursor to
execute the clicks.
"""
from __future__ import unicode_literals, division
from itertools import cycle, chain

# Iterate across whole board -- any way to speed up?
# Should be able to modify in place and continue working, without modifying
# length of list.
#
# Check numbered square for obvious flag:
#   1 touching only 1 ? == flag
#   2 touching only 2 ? == flag
#   etc
#   n touching only n ? == flag

# Flagged
#   1 touching 1 flag = all other adjacent are safe
#   2 touching 2 flag = all other adjacent are safe
#   etc
#   n touching n flags = all other adjacent are safe

# phase 2:
# Better graph-like approach; add cells to a queue; flag then mark safe, then add
# neighbors


def sweep(grid):
    """Return a set of safe coordinates in the given grid."""
    safe = set()
    grid = _listify(grid)
    for y, x, cell in _two_sweeps(grid):
        flagged_neighbors = list(_flagged_neighbors(y, x, grid))

        # When the number of flagged numbers equals the current number,
        # the rest of unsolved neighbors are all safe.
        # import pdb;pdb.set_trace()
        if len(flagged_neighbors) == int(cell):
            for y, x in _unsolved_neighbors(y, x, grid):
                grid[y][x] = 'S'
                safe.add((y, x))

        elif len(flagged_neighbors) > int(cell):
            for row in grid:
                print(row)
            # import pdb;pdb.set_trace()
            raise ValueError('More than {} flagged neighbors at {}, {}.'
                             ''.format(cell, y, x))

        unsolved_neighbors = list(_unsolved_neighbors(y, x, grid))
        flagged_neighbors = list(_flagged_neighbors(y, x, grid))

        # If there are less or equal unsolved neighbors AND flagged than N,
        # flag all the unsolved
        if len(unsolved_neighbors) + len(flagged_neighbors) <= int(cell):
            for y, x in unsolved_neighbors:
                grid[y][x] = 'F'
    return safe


def _listify(grid):
    """Convert a string grid into a list of lists."""
    return [list(row) for row in grid.split('\n') if row]


def _two_sweeps(grid):
    """Sweep forward once then backwards once across whole grid."""
    yield from chain(
        _iter_numbered_cells(grid),
        _iter_numbered_cells(grid)
    )


def _iter_numbered_cells(grid):
    """Generate all coordinates in the grid."""
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            cell = grid[y][x]
            if cell.isdigit():
                yield y, x, cell


def _unsolved_neighbors(y, x, grid):
    """Generate only those neighbors where the cell is uncovered."""
    for n_y, n_x, nei in _get_neighbors(y, x, grid):
        if nei == '?':
            yield n_y, n_x


def _flagged_neighbors(y, x, grid):
    """Generate only those neighbors with a flag."""
    for n_y, n_x, nei in _get_neighbors(y, x, grid):
        if nei == 'F':
            yield n_y, n_x


def _get_neighbors(y, x, grid):
    """Generate all neighbors around the given coordinates."""
    for n_y in range(max(0, y - 1), y + 2):
        for n_x in range(max(0, x - 1), x + 2):
            if not (y, x) == (n_y, n_x):
                try:
                    yield n_y, n_x, grid[n_y][n_x]
                except IndexError:
                    pass
