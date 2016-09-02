"""Implementation of a Queue using only stacks."""

from data_structures.stack import Stack


class QueueOfStacks(object):
    """A Queue using only Stacks as its underlying data stucture."""

    def __init__(self):

        self._stack = []
        self._reverse_stack = []
        self._reverse = False

    def enqueue(self, val):
        """Add an item to the Queue."""
        if not self._reverse:
            self._transfer(self._stack, self._reverse_stack)
            self._reverse = True
        self._reverse_stack.append(val)

    def dequeue(self):
        """Remove the front item in the Queue and return it."""
        if self._reverse:
            self._transfer(self._reverse_stack, self._stack)
            self._reverse = False
        return self._stack.pop()

    def peek(self):
        """Return the front item in the Queue without removing it."""
        if self._reverse:
            self._transfer(self._reverse_stack, self._stack)
            self._reverse = False
        try:
            return self._stack[-1]
        except IndexError:
            return None
    
    def size(self):
        """Return the length of the Queue."""
        try:
            return len(self._stack)
        except IndexError:
            return None

    def _transfer(self, from_stack, to_stack):
        """Transfer all items from the from_stack to the to_stack."""
        while True:
            try:
                item = from_stack.pop()
                to_stack.append(item)
            except IndexError:
                break
