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
    public boolean isSameTreeRecursive(TreeNode p, TreeNode q){
        if(p == null && q == null){
            System.out.println(1);
            return true;
        }
        
        if (p == null && q != null || q == null && p != null){
            System.out.println(2);
            return false;
        }

        if(p.val != q.val) return false;
        if(!isSameTreeRecursive(p.left, q.left)) return false;
        if(!isSameTreeRecursive(p.right, q.right)) return false;

        return true;
    }
    public boolean isSameTree(TreeNode p, TreeNode q) {
        return isSameTreeRecursive(p, q);
    }
}