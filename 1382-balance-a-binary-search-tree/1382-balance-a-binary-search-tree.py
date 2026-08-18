# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
            sorted = []
        #sort using in order traversal
            def inOrder(node):

                if not node:
                    return


                inOrder(node.left)
                cur = node.val

                sorted.append(cur)

                inOrder(node.right)  

            inOrder(root)

            def dfs(left, right):

                
                if left > right:
                    return None

                mid = ( left + right ) // 2

                cur = TreeNode(sorted[mid])

                cur.left = dfs(left, mid - 1)

                cur.right = dfs(mid + 1, right)

                

                return cur

            return dfs( 0, len(sorted) - 1 )    



