# mypy: disable-error-code="misc"
"""Module that handles the implementation of Doubly Linked List

"""
from __future__ import annotations

import warnings
from typing import Any

from .nodes import DoublyLinkedListNode, type_check

__all__ = ['DoublySinglyLinkedList']



class DoublyLinkedList:
    
    __slots__ = ["_head","_tail","_length"]
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    @property
    def head(self) -> DoublyLinkedList | None:
        return self._head

    @property
    def tail(self) -> DoublyLinkedList | None:
        return self._tail

    @property
    def length(self) -> int:
        return self._length

    # Setters
    @head.setter    # type: ignore[no-redef, attr-defined]
    def head(self, value: object) -> None:
        if isinstance(value, DoublyLinkedListNode) or value is None:
            self._head = value
        else:
            raise TypeError(
                f'Next value must be a DoublyLinkedListNode or None not'
                f'{type(value)}',
            )

    @tail.setter    # type: ignore[no-redef, attr-defined]
    def tail(self, value: object) -> None:
        if isinstance(value, DoublyLinkedListNode) or value is None:
            self._tail = value
        else:
            raise TypeError(
                f'Next value must be a DoublyLinkedListNode or None not'
                f'{type(value)}',
            )

    @length.setter  # type: ignore[no-redef, attr-defined]
    def length(self, value: int) -> None:
        if isinstance(value, int):
            self._length = value
        else:
            raise TypeError(f'Length should be a integer not {type(value)}')
    
    
    def to_list(self):
        return list(self)
    
    @type_check('node', DoublyLinkedListNode)
    def append_node(self, node: DoublyLinkedListNode) -> None:
        if self.head is None:
            node.prev = None
            node.next = None
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            node.next = None
        self.length += 1


    @type_check('node',DoublyLinkedListNode)
    def prepend_node(self, node: DoublyLinkedListNode) -> None:
        if self.head is None:
            node.prev = None
            node.next = None
            self.head = node
            self.tail = node
        else:
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    
    def append(self, value: Any) -> None:
        if isinstance(value,DoublyLinkedListNode):
            self.append_node(value)
        else:
            self.append_node(DoublyLinkedListNode(value))
    
    def prepend(self, value: Any) -> None:
        if isinstance(value,DoublyLinkedListNode):
            self.prepend_node(value)
        else:
            self.prepend_node(DoublyLinkedListNode(value))
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next