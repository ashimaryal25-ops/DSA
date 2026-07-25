class Solution(object):
    def diameterOfBinaryTree(self, root):
        # Keep a tracker for the max diameter found so far
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            self.res = max(self.res, left_height + right_height)

            return 1 + max( left_height , right_height)

        dfs(root)    
        return self.res 