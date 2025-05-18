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

    public void postorderRecursive(TreeNode root){
        if(root != null) {
            if(root.left != null) postorderRecursive(root.left);
            if(root.right != null) postorderRecursive(root.right);
            ans.add(root.val);
        }  
    }

    public List<Integer> postorderTraversal(TreeNode root) {
        postorderRecursive(root);
        return ans;
    }
}