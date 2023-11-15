"""This File consists code for SinglyLinkedList Data structures



Raises:
    TypeError: Next value must be a SinglyLinkedListNode or None not
    TypeError: Length should be a integer
    TypeError: We can append only SinglyLinkedListNode to SinglyLinkedList
    TypeError: We can concat only SinglyLinkedList
    NotImplementedError: We encountered a scenario to which code is not \
        implemented
    IndexError: Pop from empty Linked List
"""
from __future__ import annotations

import warnings
from typing import Any
from typing import Optional

__all__ = ['SinglyLinkedListNode', 'SinglyLinkedList']


class SinglyLinkedListNode:
    """Code for SinglyLinkedListNode data structure.

    Raises:
        TypeError: Next value must be a SinglyLinkedListNode or None not
    """

    __slots__ = ['_data', '_next']

    def __init__(
        self, data: Any, next: SinglyLinkedListNode | None = None,
    ) -> None:
        self.data = data
        self.next = next

    @property
    def data(self) -> None:
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        self._data = value

    @property
    def next(self) -> SinglyLinkedListNode | None:
        return self._next

    @next.setter
    def next(self, value: SinglyLinkedListNode | None) -> None:
        if isinstance(value, SinglyLinkedListNode) or value is None:
            self._next = value
        else:
            raise TypeError(
                f'Next value must be a SinglyLinkedListNode or None not '
                f'{type(value)}',
            )

    def __str__(self) -> str:
        return f'{self.__class__.__name__} Containing:[{self.data}, {self.next}]'

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: [{self.data}, {self.next}]>'

    def __eq__(self, other: object) -> bool:
        result: bool = False
        if isinstance(other, SinglyLinkedListNode):
            result = (self.next == other.next) and (self.data == other.data)
        return result

    def __ne__(self, other: object) -> bool:
        result: bool = False
        if isinstance(other, SinglyLinkedListNode):
            result = (self.next != other.next) or (self.data != other.data)
        return result


class SinglyLinkedList:
    """_summary_

    Raises:
        TypeError: Next value must be a SinglyLinkedListNode or None not
        TypeError: Length should be a integer
        TypeError: We can append only SinglyLinkedListNode to SinglyLinkedList
        TypeError: We can concat only SinglyLinkedList
        NotImplementedError: We encountered a scenario to which code is not \
            implemented
        IndexError: Pop from empty Linked List
    """

    __slots__ = ['_head', '_tail', '_length']

    def __init__(
        self,
        head: SinglyLinkedListNode | None = None,
        tail: SinglyLinkedListNode | None = None,
        length: int = 0,
    ) -> None:
        self.head = head
        self.tail = tail
        self.length = length

    # Getters
    @property
    def head(self) -> SinglyLinkedListNode | None:
        return self._head

    @property
    def tail(self) -> SinglyLinkedListNode | None:
        return self._tail

    @property
    def length(self) -> int:
        return self._length

    # Setters
    @head.setter
    def head(self, value: SinglyLinkedListNode | None) -> None:
        if isinstance(value, SinglyLinkedListNode) or value is None:
            self._head = value
        else:
            raise TypeError(
                f'Next value must be a SinglyLinkedListNode or None not'
                f'{type(value)}',
            )

    @tail.setter
    def tail(self, value: SinglyLinkedListNode | None) -> None:
        if isinstance(value, SinglyLinkedListNode) or value is None:
            self._tail = value
        else:
            raise TypeError(
                f'Next value must be a SinglyLinkedListNode or None not'
                f'{type(value)}',
            )

    @length.setter
    def length(self, value: int) -> None:
        if isinstance(value, int):
            self._length = value
        else:
            raise TypeError(f'Length should be a integer not {type(value)}')

    def append_node(self, node: SinglyLinkedListNode) -> None:
        if isinstance(node, SinglyLinkedListNode):
            if node.next is not None:
                warnings.warn(
                    'Given node next is pointing to some other object'
                    ' for safe appending we are removing that pointer',
                )
                node.next = None
            if self.tail and self.head:
                self.tail.next = node
                self.tail = node
            else:
                self.head = node
                self.tail = node
            self.length += 1
        else:
            raise TypeError(
                f'We can append only SinglyLinkedListNode to SinglyLinkedList'
                f'but we got {type(node)}',
            )

    def prepend_node(self, node: SinglyLinkedListNode) -> None:
        if isinstance(node, SinglyLinkedListNode):
            if node.next is not None:
                warnings.warn(
                    'Given node next is pointing to some other object'
                    ' for safe prepending we are removing that pointer',
                )
                node.next = None
            if self.tail and self.head:
                node.next = self.head
                self.head = node
            else:
                self.head = node
                self.tail = node
            self.length += 1
        else:
            raise TypeError(
                f'We can prepend only SinglyLinkedListNode to SinglyLinkedList'
                f'but we got {type(node)}',
            )

    def insert_node(self, node: SinglyLinkedListNode, index: int) -> None:
        if isinstance(node, SinglyLinkedListNode) and isinstance(index, int):
            if node.next is not None:
                warnings.warn(
                    'Given node next is pointing to some other object'
                    ' for safe prepending we are removing that pointer',
                )
                node.next = None

            # Handling Negative index for insertion
            if index < 0:
                index = self.length + index
                # Note:
                # params : [1] , -3
                # index = 1 + (-3)  => -2
                # if the index is still negative that means we need to prepend
            if index >= self.length:
                self.append_node(node)
            elif index <= 0:
                self.prepend_node(node)
            elif 0 < index < self.length:
                current = self.head
                current_pos = 0
                while current_pos < index - 1:
                    current = current.next
                    current_pos += 1
                node.next = current.next
                current.next = node
                self.length += 1
            else:
                raise NotImplementedError(
                    'We encountered a scenario to which code is not implemented',
                )
        else:
            raise TypeError(
                f'We can prepend only SinglyLinkedListNode to SinglyLinkedList'
                f'but we got {type(node)}',
            )

    def search_node(self, node: SinglyLinkedListNode, match_next: bool = True) -> bool:
        return_value = False
        if isinstance(node, SinglyLinkedListNode):
            current = self.head
            while current is not None:
                if match_next:
                    if current == node:
                        return_value = True
                        break
                else:
                    if current.data == node.data:
                        return_value = True
                        break
                current = current.next
        return return_value

    def search(self, data: Any) -> bool:
        return_value = False
        if isinstance(data, SinglyLinkedListNode):
            return_value = self.search_node(node=data, match_next=False)
        else:
            current = self.head
            while current is not None:
                if current.data == data:
                    return_value = True
                    break
                current = current.next
        return return_value

    def append(self, data: Any) -> None:
        node = SinglyLinkedListNode(data)
        self.append_node(node=node)

    def prepend(self, data: Any) -> None:
        node = SinglyLinkedListNode(data)
        self.prepend_node(node=node)

    def insert(self, data: Any, index: int) -> None:
        node = SinglyLinkedListNode(data)
        self.insert_node(node=node, index=index)

    # TODO: Implementation not complete yet
    def remove(self, data: Any) -> None:
        pass

    def pop(self) -> SinglyLinkedListNode:
        popped_node = None
        if self.head:
            if self.head is self.tail:
                popped_node = self.head
                self.head = None
                self.tail = None
            else:
                current = self.head

                while current.next != self.tail:
                    current = current.next

                popped_node = current.next
                current.next = None
                self.tail = current

            self.length -= 1
        else:
            raise IndexError('Pop from empty Linked List')
        return popped_node

    def pop(self, index: int) -> SinglyLinkedListNode:
        index = self._handle_negative_index(index)
        popped_node = None

        if index == self.length:
            popped_node = self.pop()
        else:
            if index == 0:
                popped_node = self.head
                self.head = self.head.next
                popped_node.next = None
            else:
                current_node = self.head
                current_pos = 0
                while index < current_pos:
                    current_node = current_node.next
                    current_pos += 1
                popped_node = current_node.next
                current_node.next = popped_node.next
                popped_node.next = None
            self.length -= 1
        return popped_node

    def to_list(self) -> list:
        return list(self)

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def reverse(self):
        if self.head is self.tail:
            pass
        else:
            first_node = self.head
            second_node = first_node.next
            third_node = second_node.next

            while third_node is not None:
                second_node.next = first_node

                first_node = second_node
                second_node = third_node
                third_node = second_node.next

            second_node.next = first_node
            self.head, self.tail = self.tail, self.head

            self.tail.next = None

    def _handle_negative_index(self, index: int) -> int:
        # Condition to handle neg index < length
        # (smaller negative index than length)
        # this will make sure that we pop the first element incase of
        # negative index less than -1*length
        if index < 0:
            index = max(self.length + index, 0)
        if index > self.length:
            index = min(self.length, index)
        return index

    def __str__(self) -> str:
        str_repr = ''
        current_node = self.head
        while current_node is not None:
            str_repr += str(current_node.data) + ' -> '
            current_node = current_node.next
        str_repr += 'Done'
        return f'{self.__class__.__name__}: [{str_repr}]'

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return self.length

    def __bool__(self) -> bool:
        return self.head or self.tail or self.length

    def __contains__(self, node: SinglyLinkedListNode) -> bool:
        return self.search(node) or self.search_node(node)

    def __eq__(self, other) -> bool:
        result: bool = False
        if isinstance(other, SinglyLinkedList):
            current = self.head
            other_current = other.head

            while current is not None and other_current is not None:
                if current != other_current:
                    return False
                current = current.next
                other_current = other_current.next

            if current is None and other_current is None:
                result = True

        return result

    def __nq__(self, other) -> bool:
        return not self.__eq__(other)

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __getitem__(self, index: int) -> Any:
        index = self._handle_negative_index(index)
        current = self.head
        while index != 0:
            current = current.next
            index -= 1
        return current.data

    def __setitem__(self, index: int, data: Any) -> None:
        index = self._handle_negative_index(index)
        current = self.head
        while index != 0:
            current = current.next
            index -= 1
        current.data = data

    def __delitem__(self, index: int) -> None:
        index = self._handle_negative_index(index=index)
        self.pop(index=index)

    def __iadd__(self, other: SinglyLinkedList | None) -> None:
        if isinstance(other, SinglyLinkedList):
            self.tail.next = other.head
            self.tail = other.tail
            self.length += other.length
        else:
            raise TypeError(
                f'We can concat only SinglyLinkedList but got {type(other)}',
            )

    def __add__(self, other: SinglyLinkedList | None) -> SinglyLinkedList:
        result = SinglyLinkedList()
        if isinstance(other, SinglyLinkedList):
            current = self.head
            while current is not None:
                result.append(current.data)
                current = current.next

            current = other.head
            while current is not None:
                result.append(current.data)
                current = current.next
        else:
            raise TypeError(
                f'We can concat only SinglyLinkedList but got {type(other)}',
            )
        return result
