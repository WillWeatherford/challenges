"""Defines data structure for implementing linked list."""
# -*- coding: utf-8 -*-


class Node(object):
    """Establish node structure for storing data and pointers in list."""

    def __init__(self, val=None, next_node=None):
        """Construct node instance."""
        self.val = val
        self.next = next_node


class LinkedList(object):
    """Establish class for linked list and associated functions."""

    def __init__(self, seq=None):
        """Initialize linked list and set head."""
        self.head = None

        cur_node = None
        for val in seq or []:
            cur_node = Node(val, cur_node)
        if cur_node:
            self.head = cur_node

    def display(self):
        """Print the list as a tuple literal."""
        display_list = []
        cur_node = self.head
        while cur_node:
            display_list.append(cur_node.val)
            cur_node = cur_node.next
        return str(tuple(display_list))

    def size(self):
        """Return the size of the LinkedList as an integer."""
        cur_node = self.head
        counter = 0
        while cur_node:
            counter += 1
            cur_node = cur_node.next
        return counter

    def insert(self, val):
        """Add node to linked list and update next and previous references."""
        # condense this into 1 line
        self.head = Node(val, self.head)

    def pop(self):
        """Remove the first node from the head and return its value."""
        if not self.head:
            raise IndexError("Cannot pop from empty LinkedList.")
        popped_node = self.head
        self.head = popped_node.next
        return popped_node.val

    def search(self, search_val):
        """Return first node containg the given value or None if not found."""
        search_node = self.head
        while search_node:
            if search_node.val == search_val:
                return search_node
            search_node = search_node.next
        return None

    def remove(self, node_to_remove):
        """Remove node from list in place. Raise ValueError if not found."""
        prev_node = None
        search_node = self.head
        while search_node:
            if search_node == node_to_remove:
                if prev_node:
                    prev_node.next = search_node.next
                elif search_node.next:
                    self.head = search_node.next
                else:
                    self.head = None
                break
            prev_node = search_node
            search_node = search_node.next
        else:
            raise ValueError("Node is not in list.")
