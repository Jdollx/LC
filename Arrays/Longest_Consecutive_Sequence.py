"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if nums is empty, return 0
        if not nums:
            return 0
        
        # create a set to store numbers for O(1) lookup
        # don't care about taking duplciates into consideration
        nums_set = set(nums)
        # stores our longest streak
        result_count = 0

        # iterate through the numbers
        for num in nums_set:
            # only start a new sequence if num-1 is not in the set 
            # initiates a new sequence
            if num - 1 not in nums_set:
                current_num = num
                count = 1

                # expand the sequence to the right
                while current_num + 1 in nums_set:
                    # because we're looking for exactly num + 1, we can just add
                    current_num += 1
                    # increment the current count streak as we go
                    count += 1

                # once we finish a streak, we compare our longest streak and current 
                result_count = max(result_count, count)

        return result_count
