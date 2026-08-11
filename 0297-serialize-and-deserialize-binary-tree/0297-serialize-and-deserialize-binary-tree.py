# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        vals = []


        def btPreOrder(node):

            if node == None:
                vals.append("#")
                return


            vals.append( str(node.val))

            btPreOrder(node.left)
            btPreOrder(node.right) 

        btPreOrder(root)       
        return ",".join(vals)

        

    def deserialize(self, data):
        if not data:
            return None

        vals = list( data.split(","))
        index = [0]

        def build():
            if index[0] >= len(vals):
                return None

            val = vals[index[0]]

            index[0] += 1
            if val == "#":
                return None

            

            node = TreeNode(int(val))

            node.left = build()
            node.right = build()

            return node

        return build()