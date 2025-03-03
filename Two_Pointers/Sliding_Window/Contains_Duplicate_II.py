"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # given int array nums and int k
        # true if nums equal each other and their absolute difference of indices <= k

        # sliding window of size k
        window = set()

        for i in range(len(nums)):
            # since we're looking for where they equal each other, we can use set

            # check if num already in set
            if nums[i] in window:
                return True # this means its a duplicate
                # we don't need to check the second clause because we'll never let the window get that big

            # if not, add
            window.add(nums[i])

            # if our set gets bigger than k, remove the oldest element 
            if len(window) > k:
                window.remove(nums[i - k]) 

        return False




        