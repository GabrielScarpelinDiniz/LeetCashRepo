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
    public boolean evaluateTreeRecursive(TreeNode root){
        if(root == null || root.val == 0) return false;
        if(root.val == 1) return true;
        
        boolean left = evaluateTreeRecursive(root.left);
        boolean right = evaluateTreeRecursive(root.right);

        if(root.val == 2){
            if(!(left | right)) {
                return false;
            }
        } else {
            if(!(left & right)) {
                return false;
            }
        }

        return true;
    }
    public boolean evaluateTree(TreeNode root) {
        return evaluateTreeRecursive(root);
    }
}