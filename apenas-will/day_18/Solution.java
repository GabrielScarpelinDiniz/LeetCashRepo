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
    List<Integer> ans = new ArrayList<>();

    public void preorderRecursive(TreeNode root){
        if(root != null) {
            ans.add(root.val);
            if(root.left != null) preorderRecursive(root.left);
            if(root.right != null) preorderRecursive(root.right);
        }  
    }

    public List<Integer> preorderTraversal(TreeNode root) {
        preorderRecursive(root);
        return ans;
    }
}