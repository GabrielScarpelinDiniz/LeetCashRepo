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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if(root == null) return res;

        res.add(new ArrayList<>());

        TreeNode sep = new TreeNode();
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);
        queue.add(sep);

        while(!queue.isEmpty()){
            TreeNode current = queue.remove();
            
            if(current == sep){
                if(!queue.isEmpty()){
                    res.add(new ArrayList<>());
                    queue.add(sep);
                }
            } else {
                res.get(res.size() - 1).add(current.val);
                if(current.left != null) queue.add(current.left);
                if(current.right != null) queue.add(current.right);
            }
        }

        Collections.reverse(res);
        return res;
    }
}
