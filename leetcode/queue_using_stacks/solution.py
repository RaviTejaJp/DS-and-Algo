from typing import Any
class Stack:
    def __init__(self) -> None:
        self.stack = []

    def isEmpty(self):
        if self.stack:
            return False
        return True
    
    def push(self, value: Any) -> None:
        self.stack.append(value)

    def pop(self) -> Any:
        if self.isEmpty():
            raise ValueError("Stack is empty")
        else:
            return self.stack.pop()

    def peek(self) -> Any:
        if self.isEmpty():
            raise ValueError("Stack is empty")
        else:
            return self.stack[-1]
    
    def __str__(self) -> str:
        return str(self.stack)


class Queue:
    def __init__(self) -> None:
        self.incoming_queue = Stack()
        self.outgoing_queue = Stack()
    
    def enqueue(self, value: int) -> None:
        self.incoming_queue.push(value)
    
    def dequeue(self) -> Any:
        if self.outgoing_queue.isEmpty():
            while not self.incoming_queue.isEmpty():
                self.outgoing_queue.push(self.incoming_queue.pop())
        if self.outgoing_queue.isEmpty():
            raise MemoryError("Queue is empty can not be dequeued")
        else:
            return self.outgoing_queue.pop()
    
    def __str__(self) -> str:
        return (f"Out going queue : {str(self.outgoing_queue)}  Incoming Queue : {str(self.incoming_queue)}")


queue = Queue()

for i in range(10):
    queue.enqueue(i)

print(queue.dequeue())

for i in range(10,20):
    queue.enqueue(i)

for i in range(10):
    print(queue.dequeue())


print(queue)