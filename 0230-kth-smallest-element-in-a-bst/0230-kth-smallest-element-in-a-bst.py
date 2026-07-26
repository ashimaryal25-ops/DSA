# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        
        self.count = 0
        self.res  = None

        def traverse( node ):

            if node == None or self.res is not None:
                return 

            traverse(node.left)
            self.count += 1

            if self.count == k:
                self.res = node.val
                return

            traverse(node.right)

        traverse(root)
        return self.res