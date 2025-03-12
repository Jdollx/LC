"""
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
"""
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # given array of int temps
        # temp[i] = temp on ith day
        # return result [] where result[i] = number of days 
        # until a warmer temperature appears after the ith day
        # if no warmer day, set to 0

        # initiate stack 
        s = []

        # initiate result array with x times 0s to handle else clause
        res = [0] * len(temperatures)

        # iterate through the temps
        # need indices so we can keep track of difference
        # the stack will only contain indices
        for i, temp in enumerate(temperatures):
            # add to the stack if not empty and if current temp > top of stack
            while s and temp > temperatures[s[-1]]:
                # if the temp (i, temp) is greater than the top of the stack, we need to pop
                # this means we found a higher temp
                last_hottest = s.pop()

                # calculate the difference in indices
                # current index - index of the next hottest day
                count = i - last_hottest
                res[last_hottest] = count

            # Push the current index onto the stack
            s.append(i)

        return res
