/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int ans = 0;
    public int diameterRecursive(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return 1;

        int n = 0;
        int leftHi = 0;
        if (root.left != null) {
            leftHi = diameterRecursive(root.left) + 1;
            n ++;
        }

        int rightHi = 0;
        if (root.right != null) {
            rightHi = diameterRecursive(root.right) + 1;
            n ++;
        }
        
        if (leftHi + rightHi - n >= ans) ans = leftHi + rightHi - n;
        

        return Math.max(leftHi, rightHi);
    }

    public int diameterOfBinaryTree(TreeNode root) {
        diameterRecursive(root);
        return ans;
    }
}