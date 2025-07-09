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
    public void DFS(TreeNode root, int[] lefts, int[] rights){
        if(root == null) return;

        if(lefts.length > 0){
            root.left = new TreeNode(lefts[lefts.length / 2]);
            DFS(root.left, Arrays.copyOfRange(lefts, 0, lefts.length / 2), Arrays.copyOfRange(lefts, lefts.length / 2 + 1, lefts.length)); 
        }

        if(rights.length > 0){
            root.right = new TreeNode(rights[rights.length / 2]);
            DFS(root.right, Arrays.copyOfRange(rights, 0, rights.length / 2), Arrays.copyOfRange(rights, rights.length / 2 + 1, rights.length)); 
        }
    }
    public TreeNode sortedArrayToBST(int[] nums) {
        TreeNode root = new TreeNode(nums[nums.length/2]);
        TreeNode current = root;
        
        DFS(root, Arrays.copyOfRange(nums, 0, nums.length / 2), Arrays.copyOfRange(nums, nums.length / 2 + 1, nums.length));

        return root;
    }
}