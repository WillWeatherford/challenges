"""Test that max stock profit solution works in a number of scenarios.

Output should be a tuple of (buy_index, sell_index, profit).
"""
from __future__ import unicode_literals
import pytest


OPT_OUT_CASES = [
    (list(range(99, -1, -1)), (0, 0, 0)),
    ([100, 100, 90], (0, 0, 0)),
    ([0, 0, 0, 0], (0, 0, 0)),
]


OPT_IN_CASES = [
    ([0, 100],                      (0, 1, 100)),
    (list(range(100)),              (0, 99, 99)),
    ([100, 90, 100],                (1, 2, 10)),
    ([80, 100, 70, 100],            (2, 3, 30)),
    ([80, 100, 70, 100, 90, 100],   (2, 3, 30)),  # could also accept 2, 5, 30
    ([70, 80, 100, 50, 80, 90, 70], (3, 5, 40)),
    ([80, 100, 60, 70],             (0, 1, 20)),
]

CASES = OPT_OUT_CASES + OPT_IN_CASES


@pytest.mark.parametrize('input_, output', CASES)
def test_calc_profit(input_, output):
    """Test that calc_profit returns the expected output for given input."""
    from max_stock_profit import calc_profit
    assert calc_profit(input_) == output
