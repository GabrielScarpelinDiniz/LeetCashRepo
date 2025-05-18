using System.Linq;

public class Solution
{
    public int ClimbStairs(int n)
    {
        Dictionary<int, int> memo = new Dictionary<int, int>();
        return ClimbStairsRecursive(n, memo);
    }

    private int ClimbStairsRecursive(int n, Dictionary<int, int> memo)
    {
        if (n == 0 || n == 1)
            return 1;

        if (memo.ContainsKey(n))
            return memo[n];

        int result = ClimbStairsRecursive(n - 1, memo) + ClimbStairsRecursive(n - 2, memo);
        memo[n] = result;
        return result;
    }
}