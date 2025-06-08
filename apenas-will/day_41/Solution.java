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
    public void backtracking(List<String> res, String path, TreeNode root){
        if(root.left == null && root.right == null){
            res.add(path);
            return;
        }

        if(root.left != null) backtracking(res, path + "->" + Integer.toString(root.left.val), root.left);
        if(root.right != null) backtracking(res, path + "->" + Integer.toString(root.right.val), root.right);
    }

    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        backtracking(res, Integer.toString(root.val), root);
        return res;
    }
}