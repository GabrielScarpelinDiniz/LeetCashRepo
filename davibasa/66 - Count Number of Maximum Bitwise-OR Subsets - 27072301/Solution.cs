using System;

public class Solution
{
    private int maxOr = 0;
    private int count = 0;

    public int CountMaxOrSubsets(int[] nums)
    {
        maxOr = 0;
        count = 0;
        foreach (int num in nums) maxOr |= num;
        Dfs(nums, 0, 0);
        return count;
    }

    private void Dfs(int[] nums, int index, int currentOr)
    {
        if (index == nums.Length)
        {
            if (currentOr == maxOr && currentOr != 0) count++;
            return;
        }
        // Include nums[index]
        Dfs(nums, index + 1, currentOr | nums[index]);
        // Exclude nums[index]
        Dfs(nums, index + 1, currentOr);
    }
}
