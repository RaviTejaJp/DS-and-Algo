from typing import Any
class Stack:
    def __init__(self, capacity: int) -> None:
        self.stack = [None] * capacity
        self.top = -1
        self.capacity = capacity
    
    def isFull(self):
        if self.top == self.capacity - 1:
            return True
        return False
    
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    
    def push(self, value: Any) -> None:
        if self.isFull():
            raise ValueError("Stack is full")
        else:
            self.top = self.top + 1
            self.stack[self.top] = value

    def pop(self) -> Any:
        if self.isEmpty():
            raise ValueError("Stack is empty")
        else:
            pop_value = self.stack[self.top]
            self.stack[self.top] = None
            self.top = self.top - 1
            return pop_value

    def peek(self) -> Any:
        if self.isEmpty():
            raise ValueError("Stack is empty")
        else:
            return self.stack[self.top]
    
    def __str__(self) -> str:
        return str(self.stack)



class SetOfStack:
    def __init__(self, stack_capacity: int) -> None:
        self.stack_set = []
        self.stack_capacity = stack_capacity
    
    def push(self, value: Any) -> None:
        stack = None
        if self.stack_set:
            stack = self.stack_set[-1]
            if stack.isFull():
                stack = Stack(capacity=self.stack_capacity)
                self.stack_set.append(stack)
        else:
            stack = Stack(capacity=self.stack_capacity)
            self.stack_set.append(stack)
        stack.push(value=value)

    def pop(self):
        stack = None
        if self.stack_set:
            stack = self.stack_set[-1]
            if stack.isEmpty():
                self.stack_set.pop()
                stack = self.stack_set[-1]
        else:
            raise MemoryError("Stack set is empty")
        pop_value = stack.pop()
        return pop_value

    def popAt(self, stack_id):
        stack = None
        if self.stack_set and len(self.stack_set) >= stack_id:
            stack = self.stack_set[stack_id]
            if stack.isEmpty():
                self.stack_set.pop()
                stack = self.stack_set[-1]
        else:
            raise MemoryError("Stack set is empty")
        pop_value = stack.pop()
        return pop_value

    def __str__(self):
        result = ""
        for item in self.stack_set:
            result += item.__str__()
        return result


StackSet = SetOfStack(stack_capacity=5)
print(StackSet)
for i in range(15):
    StackSet.push(i)

print(StackSet.popAt(1))
print(StackSet)

