"""
You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use two pointers to go through each bar
        left = 0
        right = len(heights) - 1

        # initiate a current area that will keep track of each pointer movement
        current_area = 0
        # initiate a max area that can be used to compare current to max to find optimal area
        max_area = 0

        # start pointers
        while left < right:
            # need to calculate the area each time we use the pointer
            # need to find the height difference between the two bars

            # length = right index minus left index
            l =  right - left
            # width = min height of the two bars
            w = min(heights[left], heights[right])

            # calculate the current area
            current_area = l * w 

            # need to update the max if current_area > max_area
            if current_area > max_area:
                max_area = current_area
            
            # otherwise, we can move our pointers
            # want to move our pointers so that we move to a taller bar
            # compare our left to right heights
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1

        return max_area
