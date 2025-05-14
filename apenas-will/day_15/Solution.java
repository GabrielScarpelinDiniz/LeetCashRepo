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
    public List<Integer> inOrderRecursive(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        
        if(root == null) return res;
        
        if(root.left != null) res.addAll(inOrderRecursive(root.left));
        
        res.add(root.val);
        
        if(root.right != null) res.addAll(inOrderRecursive(root.right));

        return res;
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        return inOrderRecursive(root);
    }
}