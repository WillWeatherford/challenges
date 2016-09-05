"""Coding Challenge: Maximize Future Stock Profit.

You have received a message from your future self, from one year in the future.

The message contains only an array of numbers, which is the daily stock prices
for a company's stock over the next year.

With this information, you can plan to maximize your profit by buying and
selling this stock.

You can only buy once, and only sell once.

Write a function to calculate the maximum profit, buy date and sell date.


Input: an array of integers or floats.

Output: a 3-tuple of (buy_date, sell_date, profit), where buy_date and
sell_date are indexes of the input array.
"""
from __future__ import unicode_literals, division
from operator import itemgetter


def calc_profit(array):
    """Return tuple of buy date, sell date and profit from given list of ints.

    Buy date and sell date are indexes from the input list.
    Profit is the difference between the values at sell date and buy
    date, being the maximum difference possible from the given list.
    """
    current_min = overall_min = (0, array[0])
    best_result = (0, 0, 0)

    for idx in range(1, len(array)):
        num = array[idx]

        if num < overall_min[1]:
            overall_min = (idx, num)

        if num < array[idx - 1]:
            current_min = (idx, num)
        else:
            current_result = _compare(current_min, (idx, num))
            macro_result = _compare(overall_min, (idx, num))
            best_result = max(
                (best_result, current_result, macro_result),
                key=itemgetter(2)
            )

    return best_result


def _compare(first, last):
    """Return result of (idx1, idx2, profit)."""
    return (first[0], last[0], last[1] - first[1])


def calc_profit_nsquared(array):
    """O(n ** 2) version of calc_profit."""
    best = (0, 0, 0)
    for idx1, num1 in enumerate(array):
        for idx2, num2 in enumerate(array[idx1 + 1:]):
            profit = num2 - num1
            if profit > best[2]:
                best = (idx1, idx1 + 1 + idx2, profit)
    return best
