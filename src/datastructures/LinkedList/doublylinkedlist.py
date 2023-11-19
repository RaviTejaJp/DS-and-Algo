# mypy: disable-error-code="misc"
"""Module that handles the implementation of Doubly Linked List

"""
from __future__ import annotations

import warnings
from typing import Any, Optional

from .nodes import DoublyLinkedListNode, generic_type_check

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
    
    @generic_type_check(DoublyLinkedListNode,
                        node=DoublyLinkedListNode)
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


    @generic_type_check(DoublyLinkedListNode,
                        node=DoublyLinkedListNode)
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

    @generic_type_check(DoublyLinkedListNode,int,
                        node=DoublyLinkedListNode,index=int)
    def insert_node(self, node: DoublyLinkedList, index: int) -> None:
        index = self._handle_negative_index(index=index)
        if index == 0:
            self.prepend_node(node=node)
        elif index == self.length:
            self.append_node(node=node)
        else:
            current_pos = 0
            current = self.head
            while current_pos < index:
                current_pos += 1
                current = current.next
            
            node.prev = current.prev
            node.next = current
            
            current.prev = node
            node.prev.next = node
            self.length += 1

    def traverse(self, reverse: bool= False) -> None:
        if not reverse:
            current = self.head
            while current:
                print(f"{current.data}",end=" -> ")
                current = current.next
            print('Done')
        else:
            current = self.tail
            while current:
                print(f"{current.data}",end=" -> ")
                current = current.prev
            print('Done')
    
    def search(self, data: Any) -> bool:
        found: bool = False
        current = self.head
        while current:
            if current.data == data:
                found = True
                break
            current = current.next
        return found

    def delete(self, data: Any) -> None:
        current = self.head
        while current:
            if current.data == data:
                if self.head is self.tail:
                    self.head = None
                    self.tail = None
                elif current.prev is None:
                    self.head = current.next
                    self.head.prev = None
                    current.next = None
                elif current.next is None:
                    self.tail = current.prev
                    self.tail.next = None
                    current.prev = None
                else:
                    current.next.prev = current.prev
                    current.prev.next = current.next
                    current.prev = None
                    current.next = None
                self.length -= 1
                break
            current = current.next



    def append(self, value: Any) -> None:
        if isinstance(value,DoublyLinkedListNode):
            self.append_node(node=value)
        else:
            self.append_node(node=DoublyLinkedListNode(value))
    
    def prepend(self, value: Any) -> None:
        if isinstance(value,DoublyLinkedListNode):
            self.prepend_node(node= value)
        else:
            self.prepend_node(node= DoublyLinkedListNode(value))
    
    def insert(self, value: Any, index: int) -> None:
        if isinstance(value,DoublyLinkedListNode):
            self.insert_node(node=value, index=index)
        else:
            self.insert_node(node=DoublyLinkedListNode(value), index=index)
    
    def clear(self) -> None:
        current = self.head
        while current:
            current.prev = None
            current = current.next
        self.head = None
        self.tail = None
        self.tail = 0
    
    @generic_type_check(int,
                        index=int)
    def _handle_negative_index(self, index:int) -> int:
        if index < 0:
            index = max(0, index + self.length)
        if index > self.length:
            index = self.length
        return index
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next