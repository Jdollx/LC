"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # given array of ints nums
        # find subaray of len(k) that has max avg value

        # store the sum of the initial k letters
        curr_sum = max_sum = sum(nums[:k])

        # count through to end of array starting from the end of size k
        for right in range(k, len(nums)):
            # fixed window = k
            # add up all the elements in size k

            # first add new number to right
            # subtract to find the difference in indices (removes the left number)
            curr_sum += nums[right] - nums[right - k]

            # compare and update
            max_sum = max(max_sum, curr_sum)

        return max_sum / k





        