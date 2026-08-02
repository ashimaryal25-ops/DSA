class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        stack = []

        def dfs(start_index):
            res.append(list(stack))

            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i - 1]:
                    continue

                stack.append(nums[i])
                dfs(i + 1)
                stack.pop()

        dfs(0)
        return res
        