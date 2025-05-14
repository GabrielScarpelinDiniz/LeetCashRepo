# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        resultado = []
        def odernar(node):
            
            if node is None:
                return
            odernar(node.left)
            odernar(node.right)
            resultado.append(node.val)
            
        odernar(root)
        return resultado