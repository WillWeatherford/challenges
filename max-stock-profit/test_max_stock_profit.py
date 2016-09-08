"""Test that max stock profit solution works in a number of scenarios.

Output should be a tuple of (buy_index, sell_index, profit).
"""
from __future__ import unicode_literals
import time
import random
import pytest


OPT_OUT_CASES = [
    (list(range(99, -1, -1)), (0, 0, 0)),
    ([100, 100, 90], (0, 0, 0)),
    ([0, 0, 0, 0], (0, 0, 0)),
]


OPT_IN_CASES = [
    # Easy and simple.
    ([0, 100],                      (0, 1, 100)),
    # Easy and longer.
    (list(range(100)),              (0, 99, 99)),
    # Delayed max -- sell index is same as earlier.
    ([100, 90, 100],                (1, 2, 10)),
    # Delayed max after prior positive min/max
    ([80, 100, 70, 100],            (2, 3, 30)),
    # Correct result is between multiple min/max matches.
    ([80, 100, 70, 100, 90, 100],   (2, 3, 30)),  # could also accept 2, 5, 30
    # Max is not involved in correct result
    ([70, 80, 100, 50, 80, 90, 70], (3, 5, 40)),
    # Min is not involved in correct result
    ([80, 100, 60, 70],             (0, 1, 20)),
    # Neither min or max are involved in correct result
    ([80, 100, 50, 80, 40, 60],     (2, 3, 30)),
]

CASES = OPT_OUT_CASES + OPT_IN_CASES


@pytest.mark.parametrize('input_, output', CASES)
def test_calc_profit(input_, output):
    """Test that calc_profit returns the expected output for given input."""
    from max_stock_profit import calc_profit
    assert calc_profit(input_) == output


@pytest.mark.parametrize('input_, output', CASES)
def test_calc_profit_nsquared(input_, output):
    """Test that calc_profit returns the expected output for given input."""
    from max_stock_profit import calc_profit_nsquared
    assert calc_profit_nsquared(input_) == output


def test_comparitive_time():
    """Test that calc_profit performance can beat calc_profit_nsquared."""
    from max_stock_profit import calc_profit, calc_profit_nsquared
    time1, time2 = 0, 0
    for _ in range(100):
        input_ = random.sample(range(100000), 1000)
        start1 = time.time()
        calc_profit(input_)
        time1 += time.time() - start1

        start2 = time.time()
        calc_profit_nsquared(input_)
        time2 += time.time() - start2
    print("\n")
    print("Total time for 100 reps of calc_profit: {}".format(time1))
    print("Total time for 100 reps of calc_profit_nsquared: {}".format(time2))
    print("Difference: {} or {:.4}%".format(time2 - time1, 100 - (time1 / time2) * 100))
    assert time1 < time2
