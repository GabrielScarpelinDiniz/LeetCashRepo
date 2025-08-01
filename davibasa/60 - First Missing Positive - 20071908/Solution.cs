using System;

public class Solution
{
    public int FirstMissingPositive(int[] nums)
    {
        int n = nums.Length;

        // Step 1: Replace all numbers <= 0 or > n with n+1
        for (int i = 0; i < n; i++)
        {
            if (nums[i] <= 0 || nums[i] > n)
            {
                nums[i] = n + 1;
            }
        }

        // Step 2: Use array indices to mark presence of numbers
        for (int i = 0; i < n; i++)
        {
            int num = Math.Abs(nums[i]);
            if (num <= n)
            {
                nums[num - 1] = -Math.Abs(nums[num - 1]);
            }
        }

        // Step 3: Find the first positive number (unmarked index)
        for (int i = 0; i < n; i++)
        {
            if (nums[i] > 0)
            {
                return i + 1;
            }
        }

        // If all numbers from 1 to n are present, return n+1
        return n + 1;
    }
}
