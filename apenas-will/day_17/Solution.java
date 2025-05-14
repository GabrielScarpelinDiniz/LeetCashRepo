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
    List<Integer> ordering = new ArrayList<>();
    
    public void inOrderChecking(TreeNode root){        
        if(root.left != null) inOrderChecking(root.left);
        ordering.add(root.val);
        if(root.right != null) inOrderChecking(root.right);
    }

    public boolean isValidBST(TreeNode root) {
        inOrderChecking(root);
        for(int i = 0; i < ordering.size() - 1; i++){
            if(ordering.get(i) >= ordering.get(i + 1)){
                return false;
            }
        }

        return true;
    }
}