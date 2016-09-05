"""Minesweeper Solver challenge from reddit.com/r/dailyprogrammer.

In this challenge you will come up with an algorithm to solve the classic game
of Minesweeper. The brute force approach is impractical since the search space
size is anywhere around 1020 to 10100 depending on the situation, you'll have
to come up with something clever.

Input description

The current field state where each character represents one field.
Flags will not be used.
Hidden/unknown fields are denoted with a '?'.
'Zero-fields' with no mines around are denoted with a space.

Example for a 9x9 board:

    1????
    1????
    111??
      1??
1211  1??
???21 1??
????211??
?????????
?????????

Output description

A list of zero-based row and column coordinates for the fields that you have
determined to be SAFE.  The list does not need to be ordered.
For the above input example this would be:

0 5
1 6
1 7
2 7
3 7
5 1
5 7
6 2
6 7

Challenge input

As suggested by /u/wutaki, this input is a greater challenge then the original:

??????
???2??
???4??
?2??2?
?2222?
?1  1?

Notes/Hints

If you have no idea where to start I suggest you play the game for a while and
try to formalize your strategy.

Minesweeper is a game of both logic and luck. Sometimes it is impossible to
find free fields through logic. The right output would then be an empty list.
Your algorithm does not need to guess.
Bonus

Extra hard mode: Make a closed-loop bot. It should take a screenshot, parse the
board state from the pixels, run the algorithm and manipulate the cursor to
execute the clicks.
"""
