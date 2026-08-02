class Solution(object):
    def subsets(self, nums):
        res = [[]]
        def dfs(start_index, current_form):

            for i in range(start_index, len(nums)):

                current_form.append( nums[i] )
                res.append(list(current_form))
                dfs( i+1, current_form)
                current_form.pop()
        dfs(0, []) 
        return res       
