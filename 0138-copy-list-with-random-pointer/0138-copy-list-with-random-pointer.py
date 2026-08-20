"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        
        dummyCopy = Node(0)

        origCur = head

        nodeMap = {}

        nodeMap[None] = None

        copyCur = dummyCopy
        while origCur != None:

            copyCur.next = Node(origCur.val)

            copyCur = copyCur.next

            nodeMap[origCur] = copyCur

            origCur = origCur.next

        copyCur.next = None


        #now connecting random pointers

        copyCur = dummyCopy.next
        origCur = head
        while origCur != None:

            copyCur.random = nodeMap[origCur.random]

            copyCur = copyCur.next

            origCur = origCur.next


        return dummyCopy.next

        