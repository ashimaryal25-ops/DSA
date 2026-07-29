class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        
        def dfs(node, p, q):
            if not node:
                return None

            if node == p or node == q:
                return node

            right = dfs(node.right, p, q)    

            left =  dfs(node.left, p, q)

            if right and left :
                return node

            if right:
                return right

            if left:
                return left


            return None

        return dfs( root, p, q )    






        