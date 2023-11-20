# mypy: disable-error-code="misc"
"""Module that handles the implementation of Doubly Linked List

"""
from __future__ import annotations

import warnings
from typing import Any, Optional

from .nodes import DoublyLinkedListNode, generic_type_check

__all__ = ['1circularDoublySinglyLinkedList']



class CircularDoublyLinkedList:
    
    __slots__ = ["_head","_tail","_length"]
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    @property
    def head(self) -> CircularDoublyLinkedList | None:
        return self._head

    @property
    def tail(self) -> CircularDoublyLinkedList | None:
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

    @generic_type_check(DoublyLinkedListNode, 
                        node=DoublyLinkedListNode)
    def append_node(self, node: DoublyLinkedListNode) -> None:
        if self.head is None:
            node.next = None
            node.prev = None
            self.head = node
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            node.prev = self.tail
            node.next = self.head
            self.tail.next = node
            self.head.prev = node
            self.tail = node
        self.length += 1
    
    @generic_type_check(DoublyLinkedListNode,
                        node=DoublyLinkedListNode)
    def prepend_node(self, node: DoublyLinkedListNode) -> None:
        if self.head is None:
            node.next = None
            node.prev = None
            self.head = node
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            node.next = self.head
            node.prev = self.tail
            self.head.prev = node
            self.tail.next = node
            self.head = node
        self.length += 1
    
    @generic_type_check(DoublyLinkedListNode,int, 
                        node=DoublyLinkedListNode,
                        index=int)
    def insert_node(self, node: DoublyLinkedListNode, index: int) -> None:
        index = self._handle_negative_index(index)
        if index == 0:
            self.prepend_node(node=node)
        elif index == self.length:
            self.append_node(node=node)
        else:
            current = self.head
            current_pos = 0
            while current and current_pos < index:
                current_pos += 1
                current = current.next
            node.next = current
            node.prev = current.prev
            current.prev.next = node
            current.prev = node
            self.length += 1
    
    def traverse(self, reverse: bool = False) -> None:
        if reverse:
            current = self.tail
            while current:
                print(f"{current.data}", end= " -> ")
                current = current.prev
                if current is self.tail:
                    print("Done")
                    break
        else:
            current = self.head
            while current:
                print(f"{current.data}", end = " ->")
                current = current.next
                if current is self.head:
                    print("Done")
                    break
    
    def delete(self, data: Any):
        current = self.head
        while current:
            if current.data == data:
                if current is self.head:
                    if self.head is self.tail:
                        self.head = None
                        self.tail = None
                    else:
                        self.head = self.head.next
                        self.head.prev = self.tail
                        self.tail.next = self.head
                elif current is self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else:
                    current.prev.next, current.next.prev = (current.next, 
                                                            current.prev)
                current.prev = current.next = None
                self.length -= 1
                break
            current = current.next
            if current is self.head:
                break
    
    
    
    def search(self, data: Any) -> bool:
        found: bool = False
        current = self.head
        while current:
            if current.data == data:
                found = True
                break
            current = current.next
            if current is self.head:
                break
        return found
    
    def insert(self, data: DoublyLinkedListNode, index: int):
        if isinstance(data, DoublyLinkedListNode):
            self.insert_node(data,index)
        else:
            self.insert_node(DoublyLinkedListNode(data),index)
    
    def append(self, data: Any) -> None:
        if isinstance(data, DoublyLinkedListNode):
            self.append_node(data)
        else:
            self.append_node(DoublyLinkedListNode(data=data))
        
    def prepend(self, data: Any) -> None:
        if isinstance(data, DoublyLinkedListNode):
            self.prepend_node(node=data)
        else:
            self.prepend_node(DoublyLinkedListNode(data=data))
    
    
    def to_list(self):
        return list(self)
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
            if current is self.head:
                break
    
    @generic_type_check(int,
                        index=int)
    def _handle_negative_index(self, index:int) -> int:
        if index < 0:
            index = max(0, index + self.length)
        if index > self.length:
            index = self.length
        return index
