def isSameTree(root1, root2):
        # check if both empty
        if root1 == None and root2 == None:
            return True

        # Base case: check if any root None
        if root1 == None or root2 == None:
            return False

        if root1.val != root2.val:
            return False

        #Leap of Faith

        return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)    

class Solution(object):
    def isSubtree(self, root, subRoot):
        
        #   check the root node
        if root == None:
            return False

        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)        

    
    




