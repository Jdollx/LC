"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 """

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # give input string of distinct characters + array of strings
        # consistent = all chars in string in allowed

        # initate count
        count = 0

        # check if each word in words is in allowed
        # iterate through the words
        for word in words:
            # The all() function returns True if all items in an iterable are true, otherwise it returns False.
            # all checks if all characters in 'word' are in 'allowed'
            # for every character in the word, check if it is in 'allowed'
            if all(char in allowed for char in word):
                count += 1
        return count
        