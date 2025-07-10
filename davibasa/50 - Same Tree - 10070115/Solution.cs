public class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution
{
    public bool IsSameTree(TreeNode p, TreeNode q)
    {
        // Both trees are empty
        if (p == null && q == null) return true;

        // One tree is empty, the other is not
        if (p == null || q == null) return false;

        // Both nodes exist, check values and recursively check subtrees
        return p.val == q.val &&
               IsSameTree(p.left, q.left) &&
               IsSameTree(p.right, q.right);
    }
}
