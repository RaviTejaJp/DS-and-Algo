class MultiStack:
    def __init__(self, stack_size, number_of_stack):
        self.stack = [None]*stack_size*number_of_stack
        self.stack_details = [{"min_index":((stack_size*item)-stack_size), "max_index":((stack_size*item)-1), "top":((stack_size*item)-stack_size-1)} for item in range(1,number_stack+1)]
    def push(self,stack_id,data):
        stack_details = self.stack_details[stack_id]
        if stack_details.top == stack_details.max:
            return f"Stack {stack_id} is full"
        else:
            self.top = self.top + 1
            self.stack[self.top] = data
    def pop(self,stack_id):
        stack_details = self.stack_details[stack_id]
        if stack_details.top == stack_details.min-1:
            return f"Stack {stack_id} is empty"
        else:
            data = self.stack[self.top]
            self.stack[self.top] = None
            self.top = self.top - 1
            return data

    def peek(self,stack_id):
        stack_details = self.stack_details[stack_id]
        if stack_details.top == stack_details.min-1:
            return f"Stack {stack_id} is empty"
        else:
            return self.stack[stack_details.top]