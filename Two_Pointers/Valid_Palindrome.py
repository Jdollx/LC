"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use two pointers to trace forward and backward through word
        # to see if they're equal = palindrome 

        # initiate pointers
        left = 0
        right = len(s)-1

        while left < right:
            # check if they're letters
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            # if all letters, then we can compare
            elif s[left].lower() == s[right].lower():
                # increment
                left+=1
                right-=1
            else:
            # if none of these conditions met, then return false
                return False
        return True



        