# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root):
            if root == None:
                return
            if root.val == val:
                return root
            if root.val<val:
                return search(root.right)
            if root.val>val:
                return search(root.left)
        
        find_root = search(root)
        return find_root

            


