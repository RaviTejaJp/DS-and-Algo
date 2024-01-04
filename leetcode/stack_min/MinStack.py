class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self,stack_value):
        if not self.stack:
            min_stack_value = stack_value
        else:	
            min_stack_value = min(self.stack[-1],stack_value)
        self.stack.append(stack_value)
        self.min_stack.append(min_stack_value)

    def pop(self):
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()
        else:
            raise ValueError("Stack is empty can not pop")

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            raise ValueError("Stack is empty can not peek")

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            raise ValueError("Stack is empty can not get minimum value of stack")

    def print_stack(self):
        print(f"Stack : {self.stack}")
        print(f"Min Stack : {self.min_stack}")

stack = MinStack()
stack.push(6)
stack.push(7)
stack.push(3)
stack.push(0)
stack.push(-1)
stack.push(10)

stack.print_stack()

stack.pop()
stack.pop()

stack.print_stack()



