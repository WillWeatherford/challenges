"""Implementation of a Queue using only stacks."""

from data_structures.stack import Stack


class QueueOfStacks(object):
    """A Queue using only Stacks as its underlying data stucture."""

    def __init__(self):

        self._stack = Stack()
        self._reverse_stack = Stack()
        self._reverse = False

    def enqueue(self, val):
        """Add an item to the Queue."""
        if not self._reverse:
            self._transfer(self._stack, self._reverse_stack)
            self._reverse = True
        self._reverse_stack.push(val)

    def dequeue(self):
        """Remove the front item in the Queue and return it."""
        if self._reverse:
            self._transfer(self._reverse_stack, self._stack)
            self._reverse = False
        return self._stack.pop()

    def peek(self):
        """Return the front item in the Queue without removing it."""

    def size(self):
        """Return the length of the Queue."""
        if self._reverse:
            return self._reverse_stack.size()
        return self._stack.size()

    def _transfer(self, from_stack, to_stack):
        """Transfer all items from the from_stack to the to_stack."""
        while True:
            try:
                to_stack.push(from_stack.pop())
            except IndexError:
                break
