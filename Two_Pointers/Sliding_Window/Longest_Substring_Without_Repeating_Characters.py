class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # given string s
        # find length of longest substring w/o duplicate chars

        # initiate set to hold the chars
        chars = set()
        left = 0

        # initiate count for substring count
        max_count = 0

        # iterate through loop and keep track of idex
        for right in range(len(s)):
            # check each char to see if in set (duplicate)
            while s[right] in chars:
                # slide our window to the right (shrink)
                chars.remove(s[left])
                left += 1
                # (expand)
            chars.add(s[right])
            # calculate the size of our window with indices
            max_count = max(max_count, right-left + 1)

        return max_count


        