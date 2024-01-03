from __future__ import annotations
from typing import Any, Type


class Queue:
    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self, item: int) -> None:
        self.queue.append(item)
    
    def dequeue(self) -> Any:
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            element: Any = self.queue.pop(0)
            return element
    
    def peek(self) -> Any:
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            return self.queue[0]
    
    def deleteQueue(self) -> None:
        self.queue = []
    
    def isEmpty(self) -> bool:
        if self.queue:
            return False
        else:
            return True

    def to_list(self) -> list:
        return list(self)

    def __str__(self) -> str:
        return ''.join(item for item in self.queue)
    
    def __iter__(self) -> list:
        for item in self.queue:
            yield item


class CircularQueue:
    def __init__(self, capacity:int) -> None:
        self.circular_queue = [None]*capacity
        self.end = -1
        self.start = -1
        self.capacity = capacity
    
    def isEmpty(self) -> bool:
        if self.start == -1:
            return True
        return False
    
    def peek(self) -> Any:
        if self.isEmpty():
            raise ValueError("CircularQueue is empty")
        else:
            return self.circular_queue[self.start]
    
    def delete(self) -> None:
        self.end = self.start = -1
        self.circular_queue = [None]*self.capacity
    
    def isFull(self) -> bool:
        if (self.end+1)% self.capacity == self.start:
            return True
        return False
    
    def enqueue(self, element: Any) -> None:
        if self.isFull():
            raise ValueError('CircularQueue is full')  
        elif self.isEmpty():
            self.start = self.end = 0
            self.circular_queue[self.end] = element
        else:
            self.end = (self.end + 1)% self.capacity
            self.circular_queue[self.end] = element
    
    def dequeue(self) -> Any:
        if self.isEmpty():
            raise ValueError("Circular Queue is empty")
        elif self.start == self.end:
            element = self.circular_queue[self.start]
            self.circular_queue[self.start] = None
            self.start = self.end = -1
            return element
        else:
            element = self.circular_queue[self.start]
            self.circular_queue[self.start] = None
            self.start = (self.start + 1)% self.capacity
    
    def __iter__(self):
        if self.end >= self.start:
            temp = self.start
            while temp <= self.end:
                yield self.circular_queue[temp]
                temp = temp + 1
        else:
            temp = self.start
            while temp < self.capacity:
                yield self.circular_queue[temp]
                temp = temp + 1
            temp = 0
            while temp <= self.end:
                yield self.circular_queue[temp]
                temp = temp + 1

class LinkedListNode:
    def __init__(self,data:Any, next: LinkedListNode | None =None) -> None:
        self._data = data
        self._next = next
    
    @property
    def data(self)-> Any:
        return self._data
    
    @data.setter
    def data(self, data: Any) -> None:
        self._data = data
    
    @property
    def next(self) -> LinkedListNode | None:
        return self._next
    
    @next.setter
    def next(self, value: LinkedListNode | None) -> None:
        if isinstance(value, LinkedListNode) or value is None:
            self._next = value
        else:
            return f"Value must be of type {self.__class__.__name__} not of {type(value)}"

class LinkedList:
    def __init__(self)-> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.data
            temp = temp.next

    def append(self,data:Any)-> None:
        temp = LinkedListNode(data=data)
        if self.head:
            self.tail.next = temp
            self.tail = temp
        else:
            self.head = temp
            self.tail = temp
    
    def pop_first(self)-> LinkedListNode:
        try:
            if self.head:
                temp = self.head
                self.head = self.head.next
                if self.head is None:
                    self.tail = None
            else:
                raise ValueError("Can not pop from empty Linked List")
        except Exception as e:
            return None
        finally:
            return temp.data

class LLQueue:
    def __init__(self):
        self.llq = LinkedList()
    
    def enqueue(self,data):
        self.llq.append(data)
    
    def dequeue(self) -> Any:
        return self.llq.pop_first()
    
    def peek(self) -> Any:
        if self.llq.head:
            return self.llq.head.data
        else:
            return "Empty Queue"
    
    def isEmpty(self) -> bool:
        if self.llq.head:
            return False
        return True

    def delete(self)-> None:
        self.llq.head = None
        self.llq.tail = None

    def to_list(self) -> list:
        return list(self.llq)
    
    def __iter__(self):
        return iter(self.llq)
