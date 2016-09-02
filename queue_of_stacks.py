"""Implementation of a Queue using only stacks."""

from data_structures.stack import Stack

class QueueOfStacks(object):
    """A Queue using only Stacks as its underlying data stucture."""

    _in_stack = Stack()
    _out_stack = Stack()

    def enqueue(self, val):
        """Add an item to the Queue."""

    def dequeue(self):
        """Remove the front item in the Queue and return it."""

    def peek(self):
        """Return the front item in the Queue without removing it."""

    def size(self):
        """Return the length of the Queue."""
