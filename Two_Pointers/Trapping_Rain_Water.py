"""
You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars
"""

class Solution:
    def trap(self, height: List[int]) -> int:

        # initiate pointers 
        left = 0
        right = len(height) - 1

        # establish our left and right maxes in case we find blocks underwater
        leftMax = height[left]
        rightMax = height[right]

        water_area = 0

        while left < right:
            # handle where we need to find the tallest bar on the left
            if  leftMax < rightMax:
                left+=1
                #   compare our last height on the left to our now +1 one
                leftMax = max(leftMax, height[left])
                # this finds the difference between the bars
                water_area +=  leftMax - height[left]

            else:
                # if rightMax is bigger, we can decrement from the right
                right-=1
                rightMax = max(rightMax, height[right])
                water_area += rightMax - height[right]

        return water_area 
