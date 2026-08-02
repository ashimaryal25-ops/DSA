class Solution(object):
    def permute(self, nums):
        
        res = []

        stack = []

        used = set()

        def dfs():
            
            if len(stack) == len(nums):

                res.append(list(stack))
                return

            for n in nums:  

                if n in used:
                    continue
                    
                stack.append(n)
                used.add(n)

                dfs()

                stack.pop()
                used.remove(n)
        dfs()
        return res        



                
