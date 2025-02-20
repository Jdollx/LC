"""
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
"""

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # circular array len(n)
        # k with if statements 

        n = len(code)  # Define n to avoid errors
        result = []
        
        # k > 0 take sum of next k numbers
        # from index i, we take the sum of the next 3 numbers
        if k > 0:

            # iterate through each index and take the sum for each 3 forwards
            for i in range(len(code)):

                # initiate sum for next 3 numbers
                sum = 0

                # then for each int in code, iterate through the next 3 numbers (not including current)
                for j in range(1, 1 + k):

                    sum += code[(i + j) % n]  # accounts for the circular array
                result.append(sum)  # append the sum

        # k < 0 take sum of previous k numbers
        if k < 0:
            for i in range(len(code)):
                sum = 0

                for j in range(1, -k + 1):
                    sum += code[(i - j) % n]  # accounts for the circular array
                result.append(sum)  # append the sum

        # k == 0, replace ith number with 0
        if k == 0:
            # can return the length of the array filled with 0s
            return [0] * len(code)
        
        return result  # return the result after processing all cases
