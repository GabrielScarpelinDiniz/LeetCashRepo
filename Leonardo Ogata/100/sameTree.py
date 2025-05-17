# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    

    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        arrp = []
        arrq = []

        preOrder(p, arrp)
        preOrder(q, arrq)

        print(arrp)
        print(arrq)

        return arrp == arrq

def preOrder(node, arr):
    if node is None:
        arr.append(None)
        return
    arr.append(node.val)
    preOrder(node.left, arr)
    preOrder(node.right, arr)
        