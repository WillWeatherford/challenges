"""Tests for minesweeper solver.

Checking that the correct "safe" cells are returned in y, x format.
"""
import pytest

GRID1 = """
11
1?
"""

GRID2 = """
111
???
???
"""

GRID3 = """
111
1??
1??
"""


GRID4 = """
??1
??1
111
"""


GRID5 = """
    1????
    1????
    111??
      1??
1211  1??
???21 1??
????211??
?????????
?????????
"""

RESULT5 = {
    (0, 5),
    (1, 6),
    (1, 7),
    (2, 7),
    (3, 7),
    (5, 1),
    (5, 7),
    (6, 2),
    (6, 7),
}

CASES = [
    (GRID1, set()),
    (GRID2, set()),
    (GRID3, {(1, 2), (2, 1)}),
    (GRID4, {(1, 0), (0, 1)}),
    (GRID5, RESULT5),
]


def test_listify():
    """Test that _listify makes multiline comment into lists."""
    from minesweeper_solver import _listify
    assert _listify(GRID1) == [[1, 1], [1, '?']]


@pytest.mark.parametrize('input_, output', CASES)
def test_grid(input_, output):
    """Test that minesweeper_solver delivers the expected output."""
    from minesweeper_solver import sweep
    assert sweep(input_) == output
