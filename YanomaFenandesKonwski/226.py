class Solution(object):
    def invertTree(self, root):
        if root:
            a = root.left
            b = root.right
            root.left = b
            root.right = a
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root