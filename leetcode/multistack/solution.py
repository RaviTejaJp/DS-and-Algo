class MultiStack:
    def __init__(self, stack_size, number_of_stack):
        self.stack = [None] * stack_size * number_of_stack
        self.stack_details = [
            {
                "min_index": ((stack_size * item) - stack_size),
                "max_index": ((stack_size * item) - 1),
                "top": ((stack_size * item) - stack_size - 1),
            }
            for item in range(1, number_of_stack + 1)
        ]

    def push(self, stack_id, data):
        if self.isFull(stack_id):
            raise MemoryError(f"Stack {stack_id} is full")
        else:
            stack_details = self.stack_details[stack_id]
            stack_details["top"] = stack_details["top"] + 1
            self.stack[stack_details["top"]] = data

    def pop(self, stack_id):
        if self.isEmpty(stack_id):
            raise MemoryError(f"Stack {stack_id} is empty")
        else:
            stack_details = self.stack_details[stack_id]
            data = self.stack[stack_details["top"]]
            self.stack[stack_details["top"]] = None
            stack_details["top"] = stack_details["top"] - 1
            return data

    def peek(self, stack_id):
        stack_details = self.stack_details[stack_id]
        if self.isEmpty(stack_id):
            return f"Stack {stack_id} is empty"
        else:
            return self.stack[stack_details.top]

    def isFull(self, stack_id):
        if 0 <= stack_id < len(self.stack_details):
            stack = self.stack_details[stack_id]
            if stack["top"] == stack["max_index"]:
                return True
            else:
                return False
        else:
            raise ValueError(f"Stack {stack_id} is not recognized")

    def isEmpty(self, stack_id):
        if 0 <= stack_id <= len(self.stack_details):
            stack = self.stack_details[stack_id]
            if stack["top"] == stack["min_index"] - 1:
                return True
            else:
                return False
        else:
            raise ValueError(f"Stack {stack_id} is not recognized")

    def print_stack(self):
        print(self.stack)


stack = MultiStack(stack_size=5, number_of_stack=3)
stack.print_stack()
stack.push(0, 3)
stack.print_stack()
stack.push(1, 30)
stack.print_stack()
stack.push(2, 300)

stack.print_stack()
stack.push(2, 400)
stack.push(2, 400)
stack.push(2, 400)
stack.push(2, 400)
stack.pop(2)
stack.print_stack()
stack.push(2, 400)
stack.print_stack()
