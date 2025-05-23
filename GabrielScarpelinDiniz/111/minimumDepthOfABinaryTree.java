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

    static class TreeNodeWithDepth {

        TreeNode node;
        int depth;

        TreeNodeWithDepth(TreeNode treeNode, int depth) {
            this.node = treeNode;
            this.depth = depth;
        }
    }

    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        Queue<TreeNodeWithDepth> queue = new LinkedList<>();
        queue.offer(new TreeNodeWithDepth(root, 1));
        boolean leafNode = false;
        while (!queue.isEmpty() && leafNode == false) {
            TreeNodeWithDepth treeNodeWithDepth = queue.poll();
            TreeNode current = treeNodeWithDepth.node;
            System.out.println(
                "Current:" + current.val + " depth:" + treeNodeWithDepth.depth
            );
            if (current.right == null && current.left == null) {
                return treeNodeWithDepth.depth;
            }
            if (current.right != null) {
                queue.offer(
                    new TreeNodeWithDepth(
                        current.right,
                        treeNodeWithDepth.depth + 1
                    )
                );
            }
            if (current.left != null) {
                queue.offer(
                    new TreeNodeWithDepth(
                        current.left,
                        treeNodeWithDepth.depth + 1
                    )
                );
            }
        }
        return -1;
    }
}
