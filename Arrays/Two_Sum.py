"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given array of ints and a target int
        # return index i and j where the numbers = target and i!=j

        # iterate through the input array and add complement to map
        # values are the index and the nums[i]
        map = {}
        for i, num in enumerate(nums):
            complement = target - num
            
            # if the complement in the map, then we have our answer
            if complement in map:
                # this accesses the stored index of that number
                return [map[complement], i]

            # if complement not in map, then we need to sore the index in the map
            map[num] = i

        return []



