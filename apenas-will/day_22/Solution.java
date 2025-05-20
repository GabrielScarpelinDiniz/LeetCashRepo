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
    public int maxDepthRecursive(TreeNode root){
        if(root == null) return 0;
        if(root.left == null && root.right == null) return 1;
        
        int lDepth = 1;
        if(root.left != null) lDepth += maxDepthRecursive(root.left);
        
        int rDepth = 1;
        if(root.right != null) rDepth += maxDepthRecursive(root.right);

        return Math.max(lDepth, rDepth);
    }
    public int maxDepth(TreeNode root) {
        return maxDepthRecursive(root);
    }
}