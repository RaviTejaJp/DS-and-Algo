""" This module has definition for all the nodes that were used in Linked Lists


"""
from __future__ import annotations

from typing import Any, Type
from functools import wraps

def type_check(param_name: str, expected_type: Type):
    def decorator(func):
        @wraps(func)
        def wrapper(self, node):
            if not isinstance(node, expected_type):
                raise TypeError(
                    f"The '{param_name}' parameter must be an instance of "
                    f"{expected_type.__name__}"
                    )
            return func(self, node)
        return wrapper
    return decorator

def generic_type_check(*param_check_args:tuple,**param_check_kwargs:dict):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            if param_check_args and args:
                for item, item_type in zip(args[1:], param_check_args):
                    if isinstance(item, item_type):
                        pass
                    else:
                        raise TypeError(
                            f"Expected '{param_check_args}' but got {type(item_type)}"
                            f" in positional arguments"
                            )
            for param_name, expected_type in param_check_kwargs.items():
                if param_name in kwargs:
                    param_value = kwargs[param_name]
                    if not isinstance(param_value, expected_type):
                        raise TypeError(
                            f"Error in {func.__name__}: "
                            f"The '{param_name}' parameter must be an instance"
                            f"of {expected_type.__name__}" 
                            f"got {type(param_value).__name__}"
                            )
            return func(*args,**kwargs)
        return wrapper
    return decorator



class SinglyLinkedListNode:
    """Class representing a Singly linked list Node

    Raises:
        ValueError: In setter method when you try to set next with something
                    other than SinglyLinkedListNode

    """

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



class DoublyLinkedListNode:
    """Class representing a Doubly linked list Node

    Raises:
        ValueError: In setter method when you try to set next with something
                    other than DoublyLinkedListNode

    """

    __slots__ = ['_data', '_next', "_prev"]

    def __init__(
        self,
        data: Any,
        next: DoublyLinkedListNode | None = None,
        prev: DoublyLinkedListNode | None = None
    ) -> None:
        self._data = data
        self._next = next
        self._prev = prev


    @property
    def prev(self) -> DoublyLinkedListNode | None:
        return self._prev

    @prev.setter
    def prev(self, value: Any) -> None:
        if isinstance(value, DoublyLinkedListNode) or value is None:
            self._prev = value
        else:
            raise ValueError(
                f'Next must be a {self.__class__.__name__} or None',
            )

    @property
    def data(self) -> None:
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        self._data = value

    @property
    def next(self) -> DoublyLinkedListNode | None:
        return self._next

    @next.setter
    def next(self, value: Any) -> None:
        if isinstance(value, DoublyLinkedListNode) or value is None:
            self._next = value
        else:
            raise ValueError(
                f'Next must be a {self.__class__.__name__} or None',
            )

    def __str__(self) -> str:
        return f'{self.__class__.__name__} [{self.prev}, {self.data}, {self.next}]'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if isinstance(other, DoublyLinkedListNode):
            return bool(
                (self.data == other.data) and (self.next is other.next) and 
                (self.prev is other.prev)
            )
        return False

    def __ne__(self, other: object) -> bool:
        if isinstance(other, DoublyLinkedListNode):
            return bool(
                (self.data != other.data) 
                or not (self.next is other.next) 
                or not (self.prev is other.prev)
            )
        return True
