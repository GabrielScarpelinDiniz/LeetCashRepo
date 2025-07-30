using System;

public class Solution
{
    public int LongestSubarray(int[] nums)
    {
        int max = 0;
        foreach (var num in nums)
            max = Math.Max(max, num);

        int longest = 0, current = 0;
        foreach (var num in nums)
        {
            if (num == max)
                current++;
            else
                current = 0;
            longest = Math.Max(longest, current);
        }
        return longest;
    }
}
