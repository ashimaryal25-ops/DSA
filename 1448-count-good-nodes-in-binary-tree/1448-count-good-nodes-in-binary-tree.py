# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def goodNodes(self, root):
        self.count = 0
        def dfs(node, maxim):
            
            if not node:
                return 

            if maxim <=  node.val:
                self.count += 1

            maxim = max(maxim, node.val)

            dfs(node.right, maxim)
            dfs(node.left, maxim)
            
        
        dfs(root, float('-inf'))
        return self.count



        