using System;
using System.Collections.Generic;

public class Solution
{
    public int MaximizeSubarrays(int n, int[][] conflictingPairs)
    {
        int maxSubarrays = 0;

        // Try removing each conflicting pair one by one
        for (int removeIndex = 0; removeIndex < conflictingPairs.Length; removeIndex++)
        {
            var remainingPairs = new List<int[]>();

            // Create list of remaining pairs after removing one
            for (int i = 0; i < conflictingPairs.Length; i++)
            {
                if (i != removeIndex)
                {
                    remainingPairs.Add(conflictingPairs[i]);
                }
            }

            // Count valid subarrays with remaining pairs
            int validSubarrays = CountValidSubarrays(n, remainingPairs);
            maxSubarrays = Math.Max(maxSubarrays, validSubarrays);
        }

        return maxSubarrays;
    }

    private int CountValidSubarrays(int n, List<int[]> conflictingPairs)
    {
        int count = 0;

        // Check all possible subarrays
        for (int start = 1; start <= n; start++)
        {
            for (int end = start; end <= n; end++)
            {
                if (IsValidSubarray(start, end, conflictingPairs))
                {
                    count++;
                }
            }
        }

        return count;
    }

    private bool IsValidSubarray(int start, int end, List<int[]> conflictingPairs)
    {
        // Check if any conflicting pair appears together in this subarray
        foreach (var pair in conflictingPairs)
        {
            int a = pair[0], b = pair[1];

            // If both elements of a conflicting pair are in the subarray, it's invalid
            if (a >= start && a <= end && b >= start && b <= end)
            {
                return false;
            }
        }

        return true;
    }
}
