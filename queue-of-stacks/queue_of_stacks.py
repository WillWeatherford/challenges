"""Implementation of a Queue using only stacks.

Credit to Crystal Stellwagen for the idea of optimizing for repeated
enqueue or repeated dequeue operations, and for help in implementation.

Utilizes two stacks:
A "normal" stack where the top item is the front, i.e. the item to
be dequeued.
A "reversed" stack where the top is the "back" i.e. where items go when
enqueued.

The flag attribute "_reverse" keeps track of which stack is active. When the
operation alternates between enqueue and dequeue, the "_transfer" method will
flip all items from one stack to the other, and flip the "_reverse" boolean.

Best case is O(1) on repeated dequeue or repeated enqueue operations.
Worst case is O(n) on alternated enqueue and dequeue operations.
"""

from data_structures.stack import Stack


class QueueOfStacks(object):
    """A Queue using only Stacks as its underlying data stucture."""

    def __init__(self):
        """Initialize the Queue with two stacks holding data."""
        self._out_stack = Stack()
        self._in_stack = Stack()
        self._size = 0

    def enqueue(self, val):
        """Add an item to the Queue."""
        self._in_stack.push(val)
        self._size += 1

    def dequeue(self):
        """Remove the front item in the Queue and return it."""
        try:
            item = self._pop()
        except IndexError:
            raise IndexError("Cannot dequeue from an empty Queue.")
        else:
            self._size -= 1
            return item

    def peek(self):
        """Return the front item in the Queue without removing it."""
        try:
            item = self._pop()
            self._out_stack.push(item)
            return item
        except IndexError:
            return None

    def size(self):
        """Return the length of the Queue."""
        return self._size

    def _pop(self):
        """Pop item from out stack, transferring or raising error if needed."""
        try:
            item = self._out_stack.pop()
        except IndexError:
            self._transfer()
            item = self._out_stack.pop()
        return item

    def _transfer(self):
        """Transfer all items from the from_stack to the to_stack."""
        while True:
            try:
                self._out_stack.push(self._in_stack.pop())
            except IndexError:
                break
