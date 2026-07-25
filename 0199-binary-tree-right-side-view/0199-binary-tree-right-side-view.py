# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):

        if not root:
            return []


        queue = collections.deque([root])

        
        res = []
        while queue:

            levelsize = len(queue)

            for i in range( levelsize ):

                cur = queue.popleft()
                if i == levelsize - 1:
                    res.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)        


        
        return res