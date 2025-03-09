"""
You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].
"""

from collections import Counter
import heapq
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        
        # Iterate through all sliding windows of size k
        for i in range(len(nums) - k + 1):
            # Get the current window
            window = nums[i:i + k]
            
            # Count frequencies in the current window
            freq = Counter(window)
            
            # Create a list of [count, value] pairs
            c = []
            for val, count in freq.items():
                c.append([count, val])
            
            # Get the x largest elements based on [count, value]
            largest_x = []
            for i in range(x):
                # Find the largest element by frequency
                largest_element = max(c, key=lambda pair: (pair[0], pair[1]))
                c.remove(largest_element)
                largest_x.append(largest_element)
            
            # Calculate the sum of the resulting x elements
            result_sum = 0
            for count, val in largest_x:
                result_sum += count * val
            
            # Append the result for this window to the result list
            res.append(result_sum)
        
        return res
