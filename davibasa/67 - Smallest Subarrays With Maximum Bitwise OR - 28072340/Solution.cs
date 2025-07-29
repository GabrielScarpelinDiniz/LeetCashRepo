using System;
using System.Collections.Generic;

public class Solution
{
    public int[] SmallestSubarrays(int[] nums)
    {
        int n = nums.Length;
        int[] result = new int[n];
        
        // For each starting position
        for (int i = 0; i < n; i++)
        {
            int maxOr = 0;
            int currentOr = 0;
            
            // Find maximum OR possible starting from i
            for (int j = i; j < n; j++)
            {
                currentOr |= nums[j];
                maxOr = Math.Max(maxOr, currentOr);
            }
            
            // Find shortest subarray starting from i with maximum OR
            currentOr = 0;
            for (int j = i; j < n; j++)
            {
                currentOr |= nums[j];
                if (currentOr == maxOr)
                {
                    result[i] = j - i + 1;
                    break;
                }
            }
        }
        
        return result;
    }
}
