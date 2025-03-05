"""
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.
"""
class MinStack:

    def __init__(self):
        # Main stack to store the values
        self.stack = []
        # Min stack to store the minimum values
        self.min_stack = []

    def push(self, val: int) -> None:
        # Add the value to the main stack
        self.stack.append(val)
        # Add the new value to the min_stack if it's the new minimum
        # check if empty or if the value being added is <= top of min stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop from both the main stack and the min stack if the value is the current min
        if self.stack:
            popped_val = self.stack.pop()
            
            if popped_val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        if self.stack:
            return self.stack[-1]
        return None  # Or raise an error if stack is empty

    def getMin(self) -> int:
        # Return the minimum element, which is the top of the min stack
        if self.min_stack:
            return self.min_stack[-1]
        return None  # Or raise an error if stack is empty
