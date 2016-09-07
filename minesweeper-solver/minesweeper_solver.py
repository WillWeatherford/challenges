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
# Better graph-like approach; add cells to a queue; flag then mark safe, then
# add neighbors


def sweep(grid):
    """Return a set of safe coordinates in the given grid."""
    safe = set()
    grid = _listify(grid)
    to_evaluate = set(_numbered_cells(_all_cells(grid), grid))
    while True:
        try:
            y, x = to_evaluate.pop()
        except KeyError:
            break

        cell = int(grid[y][x])

        # maybe use tee() instead
        numbered, unsolved, flagged = _neighbors(y, x, grid)
        if len(flagged) == cell:
            # Deduce that all unsolved are safe
            for u_y, u_x in unsolved:
                grid[u_y][u_x] = 'S'
                safe.add((u_y, u_x))
                # re-evaluate all numbered neighbors of newly safed cell
                n_numbered, n_unsolved, n_flagged = _neighbors(u_y, u_x, grid)
                to_evaluate.update(n_numbered)
            continue

        elif len(flagged) > cell:
            raise ValueError('More than {} flagged neighbors at {}, {}.'
                             ''.format(cell, y, x))

        if len(unsolved) + len(flagged) <= cell:
            for u_y, u_x in unsolved:
                # Deduce that these neighbors should be flagged
                grid[u_y][u_x] = 'F'

                # re-evaluate all numbered neighbors of newly flagged cell
                n_numbered, n_unsolved, n_flagged = _neighbors(u_y, u_x, grid)
                to_evaluate.update(n_numbered)
    print('\n')
    for row in grid:
        print(row)
    return safe


def _listify(grid):
    """Convert a string grid into a list of lists."""
    return [list(row) for row in grid.split('\n') if row]


def _all_cells(grid):
    """Generate all coordinates in the grid."""
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            yield y, x


def _numbered_cells(sequence, grid):
    """Filter only numbered cells of sequence."""
    for y, x in sequence:
        if grid[y][x].isdigit():
            yield y, x


def _unsolved_cells(sequence, grid):
    """Generate only those neighbors where the cell is uncovered."""
    for y, x in sequence:
        if grid[y][x] == '?':
            yield y, x


def _flagged_cells(sequence, grid):
    """Generate only those neighbors with a flag."""
    for y, x in sequence:
        if grid[y][x] == 'F':
            yield y, x


def _neighbors(y, x, grid):
    """Return sets of numbered, unsolved, flagged neighbors of given coords."""
    numbered = set()
    unsolved = set()
    flagged = set()
    for n_y in range(max(0, y - 1), y + 2):
        if n_y != y:
            x_iter = range(max(0, x - 1), x + 2)
        else:
            x_iter = (x - 1, x + 1) if x else (x + 1, )
        for n_x in x_iter:
            try:
                cell = grid[n_y][n_x]
            except IndexError:
                pass
            else:
                if cell.isdigit():
                    numbered.add((n_y, n_x))
                elif cell == '?':
                    unsolved.add((n_y, n_x))
                elif cell == 'F':
                    flagged.add((n_y, n_x))
    return numbered, unsolved, flagged
