"""
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.
"""
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        # Sliding window: iterate over the string
        for i in range(len(s) - 2):  # Ensures that there is room for a 3-character substring
            # Get the current 3-character window
            window = s[i:i+3]
            # Check if all characters are distinct
            if len(set(window)) == 3:
                count += 1  # Increment count if the substring has 3 distinct characters
        return count
