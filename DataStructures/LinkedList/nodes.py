from __future__ import annotations

from typing import Any


class SinglyLinkedListNode:

    __slots__ = ['_data', '_next']

    def __init__(
        self,
        data: Any,
        next: SinglyLinkedListNode | None = None,
    ) -> None:
        self._data = data
        self._next = next

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
    def next(self, value: Any) -> None:
        if isinstance(value, SinglyLinkedListNode) or value is None:
            self._next = value
        else:
            raise ValueError(
                f'Next must be a {self.__class__.__name__} or None',
            )

    def __str__(self) -> str:
        return f'{self.__class__.__name__} [{self.data}, {self.next}]'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SinglyLinkedListNode):
            return bool(
                (self.data == other.data) and (self.next is other.next),
            )
        return False

    def __ne__(self, other: object) -> bool:
        if isinstance(other, SinglyLinkedListNode):
            return bool(
                (self.data != other.data) or not (self.next is other.next),
            )
        return True
