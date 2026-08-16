from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        left = 0
        right = 0

        line = deque()
        maxs = []

        while right < len(nums):

            # Remove smaller numbers from back
            while line and nums[right] > nums[line[-1]]:
                line.pop()

            line.append(right)

            # Remove front if it left the window
            if line[0] < left:
                line.popleft()

            # Window has reached size k
            if right - left + 1 == k:
                maxs.append(nums[line[0]])
                left += 1

            right += 1

        return maxs

        