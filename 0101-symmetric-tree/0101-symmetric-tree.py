# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isMirrorTree(p, q):

        if p == None and q == None:
            return True
                
        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False
                
        # The Leap of Faith
        return isMirrorTree(p.left, q.right) and isMirrorTree(p.right, q.left)

class Solution(object):
    def isSymmetric(self, root):

        return isMirrorTree( root.left, root.right)

        

        
        