# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        resultado = []

        def preOrder(node):
            if node is None:
                return
            resultado.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        return resultado
        