# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        list_result = []
        def recursive(current):
            if current == None:
                return
            if current.left != None:
                recursive(current.left)

            list_result.append(current.val)

            if current.right != None:
                recursive(current.right)



        recursive(root)
        return list_result
