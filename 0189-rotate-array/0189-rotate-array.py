class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)

        # remove full rotation cycles
        k %= n

        # reverse whole array
        nums.reverse()

        # reverse first k elements
        nums[:k] = reversed(nums[:k])

        # reverse the rest
        nums[k:] = reversed(nums[k:])
        