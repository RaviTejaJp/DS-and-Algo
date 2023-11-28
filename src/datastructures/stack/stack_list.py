from __future__ import annotations

from typing import Any
from typing import List


class StackList:
    def __init__(self, length: int = 10) -> None:
        self.stack = []
        self.top = -1
        self.length = length

    def push(self, data: Any) -> None:
        if self.top <= self.length - 1:
            self.stack.append(data)
            self.top += 1
            print(f'{data} is successfully pushed to stack')
        else:
            raise MemoryError('Stack is full')

    def pop(self) -> Any:
        popped_element: Any = None
        if self.top <= -1:
            raise IndexError('Stack is empty')
        else:
            self.top -= 1
            popped_element = self.stack.pop()
            print(f'{popped_element} is successfully popped from stack')
        return popped_element

    def peek(self) -> Any:
        peeked_element: Any = None
        if self.top <= -1:
            raise IndexError('Stack is empty')
        else:
            peeked_element = self.stack[-1]
        return peeked_element

    def isEmpty(self) -> bool:
        if self.top == -1:
            return True
        return False

    def deleteStack(self) -> None:
        self.stack = []
        self.length = None
        self.top -= 1

    def __len__(self) -> int:
        return self.top + 1

    def __repr__(self) -> str:
        return str(list(self.stack))

    def __str__(self) -> str:
        stack_str: str = 'Top : '
        for x in range(len(self.stack) - 1, -1, -1):
            stack_str = stack_str + f' {self.stack[x]} ->'
        stack_str += ' Done'
        return f'Stack : {stack_str}'

    def __iter__(self) -> str:
        for item in range(len(self.stack) - 1, -1, -1):
            yield self.stack[item]

    def isFull(self) -> bool:
        if self.length == self.top + 1:
            return True
        return False
