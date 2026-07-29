# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        self.i = 0
        
        def build(min, max):
            
            if self.i == len(preorder):
                return None


            cur_val = preorder[self.i]

            if cur_val < min or cur_val > max:
                return None

            root = TreeNode(cur_val)

            self.i += 1
            root.left = build(min, cur_val)
            
            root.right = build(cur_val, max)

            return root
        return build(float('-inf'), float('inf'))    
   



        