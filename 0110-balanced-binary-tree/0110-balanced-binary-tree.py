# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        
        def dfs(roo):

            if roo == None:
                return [0, True]

            left = dfs( roo.left)
            right = dfs(roo.right)

            check = False
            if left[1] and right[1] and abs(left[0] - right[0]) <= 1:
                check = True   

            return (max(left[0], right[0]) + 1, check)

        res =  dfs(root)
        return res[1]
