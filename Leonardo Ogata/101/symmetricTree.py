# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        rightArray = []
        leftArray = []

        self.preOrderMirror(root.right, rightArray)
        self.preOrder(root.left, leftArray)

        return rightArray == leftArray

    def preOrder(self, node, arr):
        if(node == None):
            arr.append(None)
            return
        
        arr.append(node.val)
        self.preOrder(node.left, arr)
        self.preOrder(node.right, arr)

    def preOrderMirror(self, node, arr):
        if(node == None):
            arr.append(None)
            return
        
        arr.append(node.val)
        self.preOrderMirror(node.right, arr)
        self.preOrderMirror(node.left, arr)
        