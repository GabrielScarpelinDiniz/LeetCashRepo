# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_recursive(previous_node, start_idx, end_idx, arr, is_to_left):
    if start_idx > end_idx:
        return
    middle = (start_idx + end_idx) // 2

    if is_to_left == True:
        previous_node.left = TreeNode(arr[middle], None, None)
        construct_recursive(previous_node.left, start_idx, middle - 1, arr, True)
        construct_recursive(previous_node.left,middle + 1, end_idx, arr, False)
    else:
        previous_node.right = TreeNode(arr[middle], None, None)
        construct_recursive(previous_node.right, start_idx, middle - 1, arr, True)
        construct_recursive(previous_node.right,middle + 1, end_idx, arr, False)


class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        middle = (len(nums) - 1) // 2
        root = TreeNode(nums[middle], None, None)
        construct_recursive(root, 0, middle - 1, nums, True)
        construct_recursive(root, middle + 1, len(nums) - 1, nums, False)

        return root
