public class Solution
{
    public int MinCostToMoveChips(int[] position)
    {
        int even = 0, odd = 0;
        foreach (int p in position)
        {
            if (p % 2 == 0)
                even++;
            else
                odd++;
        }
        return Math.Min(even, odd);
    }
}
