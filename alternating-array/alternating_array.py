"""Alternating Array code challenge.

"While your friends are good at cracking security, they need some help with
elementary computing tasks. So they reach out to you.

They want to be able to give you an array of positive and negative integers,
representing distances north or south of the capital, and they want to see the
elements of the array in zigzag order.

This means that the largest member appears first, the smallest appears second,
and the remaining elements alternate between the larger members decreasing
from the largest, and the smaller members increasing from the smallest.

For example, the array [ 1, 3, 6, 9, -3 ] becomes [ 9, -3, 6, 1, 3, ] in
zigzag order.

Complete the function zigzagArray which takes one argument, an integer array
of n integers."
"""
from __future__ import unicode_literals


def alternate_iter(array):
    """Return array alternating between largest and smallest numbers."""
    result = []
    array = sorted(array)
    for n in range(len(array)):
        if n >= len(array):
            break
        result.append(array.pop())
        try:
            result.append(array[n])
        except IndexError:
            break

    return result
