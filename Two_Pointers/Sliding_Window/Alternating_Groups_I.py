"""
There is a circle of red and blue tiles. You are given an array of integers colors. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color from its left and right tiles) is called an alternating group.

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.
"""

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:

        # alternating group = 3 tiles that alternate colors (0 1 0 or 1 0 1)
        # circular array

        n = len(colors)
        count = 0

        # handle if array empty
        if n == 0:
            return 0

        # brute force
        for i in range(1, n-1):

            if colors[i] != colors[i-1] and colors[i] != colors[i+1]:
                count += 1

        if colors[0] != colors[1] and colors [0] != colors[-1]:
            count += 1

        if colors[-2] != colors[-1] and colors [-1] != colors[0]:
            count += 1


        return count