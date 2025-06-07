# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def preOrder(current, listNode):
            if current == None:
                return

            listNode.append(current.val)
            if current.left != None:
                preOrder(current.left, listNode)
            if current.right != None:
                preOrder(current.right, listNode)
        result = list()
        preOrder(root, result)
        return result
