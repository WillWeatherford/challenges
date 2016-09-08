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

GRID6 = """
??????
???2??
???4??
?2??2?
?2222?
?1  1?
"""

CASES = [
    (GRID1, set(), 2),
    (GRID2, set(), 3),
    (GRID3, {(1, 2), (2, 1)}, 3),
    (GRID4, {(1, 0), (0, 1)}, 3),
    # (GRID5, RESULT5, 9),
    # (GRID6, {(3, 0), (3, 5)}, 6),
]


@pytest.mark.parametrize('input_, output, size', CASES)
def test_listify_height(input_, output, size):
    """Test that _listify makes multiline comment into lists."""
    from minesweeper_solver import _listify
    assert len(_listify(input_)) == size


@pytest.mark.parametrize('input_, output, size', CASES)
def test_listify_width(input_, output, size):
    """Test that _listify makes multiline comment into lists."""
    from minesweeper_solver import _listify
    for row in _listify(input_):
        assert len(row) == size


@pytest.mark.parametrize('input_, output, size', CASES)
def test_grid(input_, output, size):
    """Test that minesweeper_solver delivers the expected output."""
    from minesweeper_solver import sweep
    assert sweep(input_) == output
