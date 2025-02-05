"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers will allow for O(1) - no additional space
        # keep in mind 1-indexed so need to return +1 to L and R

        # initiate our pointers
        left = 0
        right = len(numbers) - 1

        # iterate through and make sure they don't overlap
        while left < right:

            # initiate sum for easier comparisons
            sum = numbers[left] + numbers[right]
            # if they don't equal each other, check if they equal target
            if sum == target:
                # return the indices
                return [left+1, right+1]
                # if sum too much, decrease right
            elif sum > target:
                right-=1
            else:
                left+=1

        # return empty if nothing
        return []

        

