class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # can use a set because it doesn't allow duplicates
        # initiate set
        num_set = set()

        # iterate through the array and check if in set, otherwise false
        for num in nums:
            if num in num_set:
                return True

            else:
                # since it's not in the set, that means it's first occurence
                num_set.add(num)
        return False