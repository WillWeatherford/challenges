"""Define Stack data-type with last-in, first-out operation."""
from linked_list import LinkedList


class Stack(object):
    """Stack data type with last-in, first-out operation."""

    def __init__(self, seq=None):
        """Construct new Stack instance."""
        self._stack = LinkedList(seq)

    def push(self, val):
        """Push a value onto the end of the list."""
        self._stack.insert(val)

    def pop(self):
        """Remove and return the top value in the stack."""
        if not self._stack.head:
            raise IndexError("Cannot pop from an empty stack.")
        else:
            return self._stack.pop()
