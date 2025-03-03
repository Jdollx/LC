"""
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # num of replacements = len(str) - freq of most common char

        # initiate pointer at start to check first char
        left = 0

        # hashmap to count occurences of each char
        count = {}

        # result = longest substring to create
        res = 0

        # count of most frequent char in any window
        # doesn't need to be updated because our result is only
        # increased with max_freq (length of window - max_freq >= k)
        max_freq = 0

        # right goes through to end of s
        for right in range(len(s)):
            # Update the frequency of the current character
            count[s[right]] = 1 + count.get(s[right], 0)
            # Update the max frequency of any character in the window
            max_freq = max(max_freq, count[s[right]])

            # Calculate the window size
            window_size = right - left + 1

            # If the number of replacements exceeds k, shrink the window
            while window_size - max_freq > k:
                count[s[left]] -= 1
                left += 1
                window_size = right - left + 1  # Recalculate window size

            # Update the result with the maximum window size found
            res = max(res, window_size)

        return res
