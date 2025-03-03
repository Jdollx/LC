"""
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # given two strings
        # true if  s2 contains permutation of s1 else false

        # handle edge case where s1 longer than s2
        if len(s1) > len(s2):
            return False

        # use a sliding window to check each part of the two strings
        # thought to use sorting, but costly, so we can use frequency count

        # initiate freq_count
        s1_count = {}
        s2_count = {}

        # add all characters to s1
        for s in s1:
            s1_count[s] = s1_count.get(s, 0) + 1

        # initialize the first window in s2 with the same length as s1
        for i in range(len(s1)):
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1

        # the first check: if frequencies match for the first window
        if s1_count == s2_count:
            return True

        # the for loop allows us to start at the end of len(s1) and through to the end of len(s2)
        # check if the frequencies of chars in s2 window = freq of chars in s1
        for i in range(len(s1), len(s2)):
            # accesses s2 at i and adds s2 freq
            # go one at a time (increase right here, then decrease left below)
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1

            # handle moving the window
            # remove the left number
            # update in the dict
            left_char = s2[i - len(s1)]
            s2_count[left_char] -= 1

            # check the freq of that removed letter in the map
            if s2_count[left_char] == 0:
                # delete it so that it doesn't count towards the next window
                del s2_count[left_char]

            # check if current window's freq matches s1's freq
            if s1_count == s2_count:
                return True

        return False
