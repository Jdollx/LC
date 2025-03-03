"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
"""
class Solution:
    def findLHS(self, nums: List[int]) -> int:

        # harmonious array = difference between max and min = 1
        # max - min = 1
        # given int array nums, return longest substring of harmonious array
        # need to keep track of the max and min
        # outputing length of array
        # dynamic window

        if not nums:
            return 0
                
        freq = {}
        # add all nums to dict
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
                
            # initiate count
        max_length = 0
        for key in freq:
            # uses key + 1 as key
            if key + 1 in freq:
                # if it's in dict, then take the frequency of each 
                current_length = freq[key] + freq[key + 1]
                # compare to previous iterations
                max_length = max(max_length, current_length)
            
        return max_length








        
