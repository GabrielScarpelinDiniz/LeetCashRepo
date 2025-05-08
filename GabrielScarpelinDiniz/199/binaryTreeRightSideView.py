# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(current, depth, maxDepth, output):
    if current == None:
        return None
    print("Val: "+str(current.val)+" Depth: "+str(depth)+" MaxDepth: "+str(maxDepth))
    if depth > maxDepth['val']:
        maxDepth['val'] = depth
        output.append(current.val)
    dfs(current.right, depth + 1, maxDepth, output)
    dfs(current.left, depth + 1, maxDepth,output)

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None:
            return []
        output = []
        maxDepth = dict(val=-1)
        dfs(root, 0, maxDepth, output)
        return output
