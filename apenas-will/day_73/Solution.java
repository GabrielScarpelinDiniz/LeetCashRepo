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
    public void DFS(int[] res, TreeNode root, int currVal){
        if(root == null) return;
        if(root.left == null && root.right == null){
            res[0] += (currVal * 10 + root.val);
            return;
        }

        currVal = currVal * 10 + root.val; 
        if(root.left != null) DFS(res, root.left, currVal);
        if(root.right != null) DFS(res, root.right, currVal);
    }
    public int sumNumbers(TreeNode root) {
        if(root == null) return 0;

        int[] res = new int[1];

        DFS(res, root, 0);

        return res[0];
    }
}