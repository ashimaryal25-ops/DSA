# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(p, q):

        if p == None and q == None:
            return True
                
        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False
                
        # The Leap of Faith
        return isSameTree(p.left, q.right) and isSameTree(p.right, q.left)

class Solution(object):
    def isSymmetric(self, root):

        return isSameTree( root.left, root.right)

        

        
        