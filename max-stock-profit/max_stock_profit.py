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
    result = (0, 0, 0)

    return result


# Iterate through the list
# save the min-so-far
    # if max has already been found, save min-so-far in case a better max
    # comes along
# save the max-so-far
#   if min has already been found, take max-so-far
#   be able to overwrite max with lower max if lower min comes along


def calc_profit_nsquared(array):
    """O(n ** 2) version of calc_profit."""
    best = (0, 0, 0)
    for idx1, num1 in enumerate(array):
        for idx2, num2 in enumerate(array[idx1 + 1:]):
            profit = num2 - num1
            if profit > best[2]:
                best = (idx1, idx1 + 1 + idx2, profit)
    return best
