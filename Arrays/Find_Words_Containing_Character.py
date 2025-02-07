"""
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.
"""


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # 0-indexed array strings and char x
        # return array of indices of where x is in strings


        # initiate result array
        result = []

        # iterate through the words in array
        # enumerate to access the indices of the words
        for i, word in enumerate(words):
            # don't need to iterate through each letter - python specific
            if x in word:
                # need to append the index of the word
                result.append(i)

        return result
        