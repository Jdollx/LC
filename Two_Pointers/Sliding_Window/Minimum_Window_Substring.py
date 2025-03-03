"""
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # given string s and t
        # return shortest substring of s
        # where every char in t (including dupes)
        # is present in the sub
        # if no sub, return ""

        if len(s) < len(t):
            return ""

        res = ""

        t_dict = defaultdict(int)
        s_dict = defaultdict(int)
        # this will increment with every match our s to t makes
        matched = 0

        # need to count the freq of char in t
        for letter in t:
            t_dict[letter] += 1

        # use pointers to shrink and expand the window
        left = 0
        right = 0

        # move right until all the characters in t_dict found
        while right < len(s):
            # check if expansion (next char) of window in t dict
            if s[right] in t_dict:
                # if in dict, then we want to add it to s_dict to keep track
                # of occurences in the current window
                s_dict[s[right]] += 1

                # need to determine if what is in the window is a valid substring
                # this checks that frequencies are the same 
                if s_dict[s[right]] == t_dict[s[right]]:
                    matched += 1

            # use another loop to shrink the window
            # since our right is handled so that we have through the end of t,
            # we need to revisit the left side
            while left <= right and matched == len(t_dict):
                # if the current window is valid, check if it's the smallest one
                if not res or (right - left + 1) < len(res):
                    # extract and add the substring to res
                    res = s[left:right + 1]

                # now try to shrink the window from the left
                if s[left] in t_dict:
                    s_dict[s[left]] -= 1
                    # if we have fewer characters than required in the window, stop shrinking
                    if s_dict[s[left]] < t_dict[s[left]]:
                        matched -= 1

                # move left pointer to shrink the window
                left += 1

            # expand the window by moving right pointer
            right += 1

        return res
