# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def maxElement(root):
    queue = []
    if root.right != None:
        queue.append(root.right)
    elif root.left != None:
        queue.append(root.left)

    current = root
    maxNode = root
    while len(queue) > 0:
        element = queue.pop()
        if current.val < element.val:
            maxNode = element

        if root.left != None:
            queue.append(root.left)
        if root.right != None:
            queue.append(root.right)

        current = element


    return maxNode

def minElement(root):
    queue = []
    queue.append(root)
    current = root
    minNode = root
    while len(queue) > 0:
        element = queue.pop()
        if current.val > element.val:
            minNode = element

        if current.left != None:
            queue.append(current.left)
        if current.right != None:
            queue.append(current.right)

        current = element

    return minNode

def verifySubtree(root):
    if root == None:
        return True

    valid = True
    if root.right != None:
        valid = valid & root.right.val > root.val
    if root.left != None:
        valid = valid & root.left.val < root.val

    return valid & verifySubtree(root.right) & verifySubtree(root.left)

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        maxLeftChild = maxElement(root.left)
        minRightChild = minElement(root.right)

        if maxLeftChild.val >= root.val and maxLeftChild != root:
            return False

        if minRightChild.val <= root.val and minRightChild != root:
            return False

        # verifying each subtree
        return verifySubtree(root)

def isValidBST(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    if root.right == None and root.left == None:
        return True

    maxLeftChild = None
    minRightChild = None
    if root.left != None:
        maxLeftChild = maxElement(root.left)
    if root.right != None:
        minRightChild = minElement(root.right)

    if maxLeftChild != None and maxLeftChild.val >= root.val and maxLeftChild != root:
        return False

    if minRightChild != None and minRightChild.val <= root.val and minRightChild != root:
        return False

    # verifying each subtree
    return verifySubtree(root)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

print(isValidBST(root))
