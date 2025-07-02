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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if(root == null) return new ArrayList<>();

        List<List<Integer>> ans = new ArrayList<>();
        Queue<TreeNode> queue = new ArrayDeque<>();
        
        TreeNode sep = new TreeNode();
        queue.add(root);
        queue.add(sep);
        
        ans.add(new ArrayList<>());
        
        while(!queue.isEmpty()){
            TreeNode current = queue.remove();

            if(current == sep){
                if(!queue.isEmpty()){
                    ans.add(new ArrayList<>());
                    queue.add(sep);
                }
            } else {
                ans.get(ans.size() - 1).add(current.val);
                if(current.left != null) queue.add(current.left);
                if(current.right != null) queue.add(current.right);
            }
        }

        return ans;
    }
}