"""
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
"""

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # four operations, one variable x 
        # x = 0 a start
        # input array of strings that contain operations
        # return x after operations

        # initialize x
        x = 0

        # iterate through the array
        for operation in operations:
            if "X++" in operation or "++X" in operation:
                x += 1
            if "X--" in operation or "--X" in operation:
                x -= 1

        return x




        