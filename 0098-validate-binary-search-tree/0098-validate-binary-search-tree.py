class Solution(object):
    def isValidBST(self, root):
        self.prev = float('-inf')
        
        def inorder(node):
            # Base Case
            if not node:
                return True
            
            #LEFT
            if not inorder(node.left):
                return False
                
            # ROOT (The Check) we check
            if node.val <= self.prev:
                return False
            self.prev = node.val
            
            # 3. RIGHT (Written explicitly, just like you pictured it!)
            if not inorder(node.right):
                return False
                
            # If left is good, root is good, and right is good:
            return True
            
        return inorder(root)