from typing import Any

class StackNode:
    def __init__(self, data: Any, prev: 'StackNode' = None) -> None:
        self.data = data
        self.prev = prev


class Stack:
    def __init__(self, length: int = 10) -> None:
        self.top = -1
        self.length = length
        self.head = None

    def push_node(self, node: 'StackNode'):
        if self.top + 1 >= self.length:
            raise MemoryError("Stack is full")
        else:
            if isinstance(node, StackNode):
                node.prev = self.head
                self.head = node
                self.top += 1
            else:
                raise TypeError(
                    "Stack only Accept StackNode but {type(node)} is given"
                    )
    
    def pop_node(self) -> StackNode:
        if self.top <= -1:
            raise IndexError("Stack is empty")
        else:
            node = self.head
            self.head = self.head.prev
            node.prev = None
            self.tail -= 1
    
    def peak(self) -> Any:
        if self.top <= -1:
            raise IndexError("Stack is empty")
        else:
            return self.head.data
    
    def isEmpty(self):
        return bool(self.length == -1)
    
    def isFull(self) -> bool:
        return bool(self.length == self.top+1)
    
    def delete(self) -> None:
        self.head = None
        self.length = None
        self.top = -1