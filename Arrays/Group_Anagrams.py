"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # could sort - expensive
        # could make map of value:occurence = 26 possible slots for abc

        #initiate a default dic to add to map if not present
        map = defaultdict(list)

        # iterate through the array
        for word in strs:
            # initiate count of how many times letter appears in word
            count = [0] * 26
            # iterate through each letter in word
            for letter in word:
                # ord returns unicode of letter
                # use ord of a to get the relative position to the current letter
                # this allows for each letter to be mapped to a positional value
                # ex: a = 0, b = 1
                # count is increased for that positional index 
                # could just store a-z and increment their values, but space
                count[ord(letter) - ord('a')] += 1
            # need to convert to tuple because lists are mutable and tuples are not
            # associates counts with their words
            map[tuple(count)].append(word)
        return list(map.values())


            

            

