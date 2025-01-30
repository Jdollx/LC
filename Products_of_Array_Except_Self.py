"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n time without using the division operation?
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # handling brute force where we'll iterate through the array
        # twice for every number, multiplying those except for the nums[i]
        # will result in On^2

        # we need to iterate over indices
        n = len(nums)

        # initiate an array to hold the answer; same length as input array
        res = [0] * n

        for i in range(n):
            product = 1
            for j in range(n):
                # exclude nums[i]
                if i != j:
                    product *= nums[j]
            # store each new product in result
            res[i] = product

        return res
