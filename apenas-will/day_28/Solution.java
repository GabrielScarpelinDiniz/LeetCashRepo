/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
}
*/

class Solution {
    List<Integer> solution = new ArrayList<>();

    public void postorderRecursive(Node root) {
        if (root != null) {
            if (root.children != null) {
                for (Node n : root.children) {
                    postorderRecursive(n);
                }
            }
            solution.add(root.val);
        }
    }

    public List<Integer> postorder(Node root) {
        postorderRecursive(root);
        return solution;
    }
}