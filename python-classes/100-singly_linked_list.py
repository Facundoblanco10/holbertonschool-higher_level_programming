#!/usr/bin/python3
"""Module"""


class Node():
    """Node class"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) != Node and value:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """Singly linked list class"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        aux = self.__head
        while value > aux.data:
            prev = aux
            if aux.next_node:
                aux = aux.next_node
            else:
                aux.next_node = new_node
                return
        prev.next_node = new_node
        new_node.next_node = aux

    def __str__(self):
        st = ''
        if self.__head is None:
            return
        while self.__head.next_node:
            st += str(self.__head.data) + '\n'
            self.__head = self.__head.next_node
        st += str(self.__head.data)
        return (st)
