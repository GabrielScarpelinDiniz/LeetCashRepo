# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert(current):
    if current == None:
        return
    aux = current.left
    current.left = current.right
    current.right = aux
    invert(current.left)
    invert(current.right)
class Solution:
    def invertTree(self, root):
        head = root
        invert(head)
        return head
