"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # given array of words
        # return words on one row of keyboard

        # use sets cause dupes dont matter
        keyboard_rows = {
            1: set("qwertyuiop"),
            2: set("asdfghjkl"),
            3: set("zxcvbnm")
        }

        result = []

        for word in words:
            # handle case sensitivity
            lower = set(word.lower())
            # iterate over 
            for row in keyboard_rows.values():
                # checks if all the letters are in the set (each given row)
                if lower.issubset(row): 
                    # if so, add the word
                    result.append(word)
                    break

        return result

        
