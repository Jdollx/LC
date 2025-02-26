"""
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.
"""

import heapq
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # given array of nums and int k
        # sliding window = k size that starts at left of nums
        # window slides right until at end
        # return list that contains max element for each step

        if not nums or k == 0:
            return []

        # make a heap that takes the max value and index for each window
        h = []
        heapq.heapify(h)

        # result to store the max elements for each window
        result = []

        # since the window (fixed) is sliding by itself, we just need to handle k elements
        for i in range(len(nums)):
            # add the current element and its index to the heap (invert value to use min heap as max heap)
            # The heap stores pairs of (neg_value, index)
            heapq.heappush(h, (-nums[i], i))

            # make sure the heap only contains elements within the sliding window
            while h[0][1] <= i - k:
                heapq.heappop(h)

            # once we have processed at least k elements, get the max (which is the root of the heap)
            if i >= k - 1:
                result.append(-h[0][0])  # negate again to get the original value

        return result
