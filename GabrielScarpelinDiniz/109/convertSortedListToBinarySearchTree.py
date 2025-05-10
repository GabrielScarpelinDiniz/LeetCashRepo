# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recursiveGeneratedHeightedBalancedTree(treeNode, startIdx, endIdx, arr, isToLeft):
    if startIdx == endIdx:
        if isToLeft == True:
            treeNode.left = TreeNode(arr[startIdx], None, None)
        else:
            treeNode.right = TreeNode(arr[startIdx], None, None)
        return

    if startIdx > endIdx:
        return

    middle = ((startIdx + endIdx) // 2)

    if isToLeft == True:
        treeNode.left = TreeNode(arr[middle], None, None)
        recursiveGeneratedHeightedBalancedTree(treeNode.left, startIdx, middle - 1, arr, True)
        recursiveGeneratedHeightedBalancedTree(treeNode.left, middle + 1, endIdx, arr, False)
    else:
        treeNode.right = TreeNode(arr[middle], None, None)
        recursiveGeneratedHeightedBalancedTree(treeNode.right, startIdx, middle - 1, arr, True)
        recursiveGeneratedHeightedBalancedTree(treeNode.right, middle + 1, endIdx, arr, False)

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        arr = []
        current = head
        while current != None:
            arr.append(current.val)
            current = current.next

        if len(arr) == 0:
            return None
        middle = len(arr) // 2
        root = TreeNode(arr[len(arr) // 2], None, None)
        recursiveGeneratedHeightedBalancedTree(root, 0, middle - 1, arr, True)
        recursiveGeneratedHeightedBalancedTree(root, middle + 1, len(arr) - 1, arr, False)

        return root
