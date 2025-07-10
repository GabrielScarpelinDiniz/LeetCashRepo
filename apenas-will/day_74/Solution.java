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
    public void DFS(String[] res, TreeNode root, List<Integer> currVal){
        if(root == null) return;
        
        if(root.left == null && root.right == null){
            StringBuilder s = new StringBuilder();
            for(int i = currVal.size() -1; i >= 0 ; i--){
                s.append((char) ('a' + currVal.get(i)));
            }

            res[0] = s.toString().compareTo(res[0]) < 0? s.toString(): res[0];
            return;
        }


        if(root.left != null){
            currVal.add(root.left.val);
            DFS(res, root.left, currVal);
            currVal.remove(currVal.size() - 1);
        }

        if(root.right != null) {
            currVal.add(root.right.val);
            DFS(res, root.right, currVal);
            currVal.remove(currVal.size() - 1);
        }
    }

    public String smallestFromLeaf(TreeNode root) {
        if(root == null) return new String();
        String[] res = new String[1];
        res[0] = "{";
        List<Integer> temp = new ArrayList<>();
        temp.add(root.val);

        DFS(res, root, temp);

        return res[0];
    }
}