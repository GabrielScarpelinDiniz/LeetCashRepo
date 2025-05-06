
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node):
            if not node:
                return None
            if node.val == val:
                return node
            return search(node.right if node.val < val else node.left)
        
        return search(root)
```

### Binary Search Tree (BST) Recap
This solution uses recursion to traverse the tree:
- If the current node is `None`, return `None`.
- If the current node's value matches the target `val`, return the node.
- Otherwise, recursively search the right subtree if the current node's value is less than `val`, or the left subtree if it's greater.

Simple and efficient! On to the next challenge! Good Luck Losers!
