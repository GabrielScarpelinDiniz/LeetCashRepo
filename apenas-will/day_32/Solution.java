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
    public void invertRecursive(TreeNode root){
        if(root != null){
            if(root.left != null) invertRecursive(root.left);
            if(root.right != null) invertRecursive(root.right);
            TreeNode temp = root.left;
            root.left = root.right;
            root.right = temp;
        }
    }
    public TreeNode invertTree(TreeNode root) {
        invertRecursive(root);
        return root;
    }
}