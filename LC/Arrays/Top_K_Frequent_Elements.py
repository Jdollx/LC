"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k = how many of the most frequent occurring numbers should be returned

        # establish hashmap to hold number and frequency
        # use default dic so everything is added already
        map = defaultdict(int)

        # because default dic, the number is already added to map
        # so then we can just increment if more than 1 number occurs
        for number in nums:
            map[number] += 1

        # now we need to iterate through map to find the k occurring numbers
        # we build another array to hold frequency, number
        frequency = []
        for num, freq in map.items():
            # adding frequency and number to the array
            frequency.append([freq, num])

        # now we can sort (can't sort dict)
        # sort by frequency in descending order
        # lists frequency first and then number
        frequency.sort(reverse=True)

        # make array for the answer
        answer = []
        for i in range(k):  # take the first k elements from the sorted list
            answer.append(frequency[i][1])  # Append the number - numbers stored as (freq, number)

        return answer