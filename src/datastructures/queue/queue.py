from typing import Any


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