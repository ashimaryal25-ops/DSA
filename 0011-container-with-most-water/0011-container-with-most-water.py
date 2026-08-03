class Solution(object):
    def maxArea(self, height):
        
        left = 0

        right = len(height) - 1

        curMax = 0
        while left < right:

            
            curWaterHold = (right - left) * min( height[left], height[right])

            curMax = max( curWaterHold, curMax)

            if height[right] < height[left]:
                right = right - 1
            else:
                left = left + 1


        return curMax        





