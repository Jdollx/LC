"""
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # given array of strings 
        # reverse polish = 3+4 --- 3 4 +
        # return int that does the expression

        # initiate a stack 
        s = []
        
        # iterate through the array
        for x in tokens:
            # check if its a digit so we can push it to the stack 
            if x.lstrip('-').isdigit():
                s.append(x)
            # if its an operator, we can pop the previous stack elements
            if x == "+" or x == "-" or x == "*" or x == "/":
                # once we run into operator, pop two elements that can be used for the operations
                a = int(s.pop())  
                b = int(s.pop())    

                # append the result back to the stack so that the operation can continue
                if x == "+":
                    s.append(a+b)
                if x == "-":
                    s.append(b-a)
                if x == "*":
                    s.append(a*b)
                if x == "/":
                    s.append(b/a)
        return int(s.pop())




        