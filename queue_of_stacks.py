"""Implementation of a Queue using only stacks."""

from data_structures.stack import Stack


class QueueOfStacks(object):
    """A Queue using only Stacks as its underlying data stucture."""

    def __init__(self):
        """Initialize the Queue with two stacks holding data."""
        self._stack = Stack()
        self._reverse_stack = Stack()
        self._reverse = False
        self._size = 0

    def enqueue(self, val):
        """Add an item to the Queue."""
        if not self._reverse:
            self._transfer(self._stack, self._reverse_stack)
        self._reverse_stack.push(val)
        self._size += 1

    def dequeue(self):
        """Remove the front item in the Queue and return it."""
        if self._reverse:
            self._transfer(self._reverse_stack, self._stack)
        try:
            item = self._stack.pop()
            self._size -= 1
            return item
        except IndexError:
            raise IndexError("Cannot dequeue from an empty Queue.")

    def peek(self):
        """Return the front item in the Queue without removing it."""
        if self._reverse:
            self._transfer(self._reverse_stack, self._stack)
        try:
            item = self._stack.pop()
            self._stack.push(item)
            return item
        except IndexError:
            return None

    def size(self):
        """Return the length of the Queue."""
        return self._size

    def _transfer(self, from_stack, to_stack):
        """Transfer all items from the from_stack to the to_stack."""
        while True:
            try:
                to_stack.push(from_stack.pop())
            except IndexError:
                break
        self._reverse = not self._reverse
