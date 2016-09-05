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
1??
1??
"""

CASES = [
    (GRID1, set()),
    (GRID2, {(1, 2), (2, 1)}),
]


@pytest.mark.parametrize('input_, output', CASES)
def test_grid(input_, output):
    """Test that minesweeper_solver delivers the expected output."""
    from minesweeper_solver import sweep
    assert sweep(input_) == output
