"""
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # result list to store all valid combinations
        res = []

        # helper function to generate parentheses using backtracking
        def backtrack(s: str, open_count: int, close_count: int):
            # Base case: if the string length is 2*n (valid parentheses string)
            # if n = 3, then we have 3 open and 3 closed = 2*3 = 6
            if len(s) == 2 * n:
                # this is a valid parentheses 
                res.append(s)
                return
            
            # If we can add an open parenthesis '('
            # if we have more open 
            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)

            # If we can add a close parenthesis ')'
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)

        # Start the backtracking with an empty string and counts for open and close parentheses
        backtrack('', 0, 0)
        
        return res








        