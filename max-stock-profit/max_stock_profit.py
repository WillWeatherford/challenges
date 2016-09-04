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
    enum = list(enumerate(array))
    buy_idx, buy_val = min(enum, key=itemgetter(1))
    sell_idx, sell_val = max(enum, key=itemgetter(1))

    if not sell_idx > buy_idx:
        return 0, 0, 0

    return buy_idx, sell_idx, sell_val - buy_val
