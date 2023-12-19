#!/usr/bin/python3

"""Singly linked list"""


class Node:
    """a class Node that defines a node"""

    def __init__(self, data, next_node=None):
        """Initializing a node.

        Args:
            data (int): the data of node.
            next_node(node): next node nownode.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """set the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """set next_node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """a class SinglyLinkedList that defines a singly linked"""

    def __init__(self):
        """initializing list."""
        self.head = None

    def sorted_insert(self, value):
        """sorting the inserted node."""
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """string of the new node."""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
