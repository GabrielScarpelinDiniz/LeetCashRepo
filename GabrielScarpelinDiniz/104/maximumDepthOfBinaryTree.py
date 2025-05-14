# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(current, level):
    leftLevel = level
    rightLevel = level
    if current.right != None:
        rightLevel = dfs(current.right, level + 1)
    if current.left != None:
        leftLevel = dfs(current.left, level + 1)

    return max(rightLevel, leftLevel)

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0

        return dfs(root, 1)
