using System;

public class Solution
{
    public int CountHillValley(int[] nums)
    {
        int n = nums.Length;
        int count = 0;
        int i = 1;
        while (i < n - 1)
        {
            int left = i - 1;
            int right = i + 1;
            // Skip equal neighbors to the left
            while (left >= 0 && nums[left] == nums[i]) left--;
            // Skip equal neighbors to the right
            while (right < n && nums[right] == nums[i]) right++;
            if (left >= 0 && right < n)
            {
                if ((nums[i] > nums[left] && nums[i] > nums[right]) ||
                    (nums[i] < nums[left] && nums[i] < nums[right]))
                {
                    count++;
                }
            }
            i = right;
        }
        return count;
    }
}
