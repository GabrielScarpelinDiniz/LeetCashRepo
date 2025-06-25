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
    public boolean DFS(int sum, TreeNode root, int target){
        if(sum == target && (root.left == null && root.right == null)){
            return true;
        }

        if(root.left != null){
            if (DFS(sum + root.left.val, root.left, target)) return true;
        }
        
        if(root.right != null){
            if (DFS(sum + root.right.val, root.right, target)) return true;
        }

        return false;
    }
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null) return false;
        return DFS(root.val, root, targetSum);
    }
}