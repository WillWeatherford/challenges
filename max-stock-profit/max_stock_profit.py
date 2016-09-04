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
    best_data = _recurse(enum, 0, len(enum) - 1)

    return best_data['buy_idx'], best_data['sell_idx'], best_data['profit']


def _recurse(enum, first_idx, last_idx):
    min_idx, min_val = min((enum[first_idx], enum[last_idx]), key=itemgetter(1))
    max_idx, max_val = max((enum[first_idx], enum[last_idx]), key=itemgetter(1))
    buy_idx, buy_val = enum[first_idx]
    sell_idx, sell_val = enum[last_idx]

    result = {
        'min_idx': min_idx,
        'max_idx': max_idx,
        'min_val': min_val,
        'max_val': max_val,
        'buy_idx': buy_idx,
        'sell_idx': sell_idx,
        'buy_val': buy_val,
        'sell_val': sell_val,
        'profit': sell_val - buy_val,
    }

    if last_idx - first_idx <= 1:
        return result

    half_idx = ((last_idx + 1 - first_idx) // 2) + first_idx
    first_half_data = _recurse(enum, first_idx, half_idx - 1)
    last_half_data  = _recurse(enum, half_idx, last_idx)

    result = _best_data(first_half_data, last_half_data)
    # import pdb;pdb.set_trace()
    return result


def _best_data(first, last):
    """Get best data from combining first half and second half of the list."""
    combo = {
        'buy_idx': first['buy_idx'],
        'sell_idx': last['sell_idx'],
        'buy_val': first['buy_val'],
        'sell_val': last['sell_val'],
        'profit': last['sell_val'] - first['buy_val'],
    }
    if last['max_val'] > first['min_val']:
        combo['buy_val'] = combo['min_val'] = first['min_val']
        combo['buy_idx'] = combo['min_idx'] = first['min_idx']
        combo['sell_val'] = combo['max_val'] = first['max_val']
        combo['sell_idx'] = combo['max_idx'] = first['max_idx']
        combo['profit'] = combo['sell_val'] - combo['buy_val']
    return max((first, last, combo), key=itemgetter('profit'))


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
