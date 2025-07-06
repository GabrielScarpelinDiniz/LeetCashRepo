using System;

public class Solution
{
    public void NextPermutation(int[] nums)
    {
        int n = nums.Length;

        // Step 1: Find the first decreasing element from right to left
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1])
        {
            i--;
        }

        if (i >= 0)
        {
            // Step 2: Find the element just larger than nums[i] from right
            int j = n - 1;
            while (nums[j] <= nums[i])
            {
                j--;
            }

            // Step 3: Swap nums[i] and nums[j]
            Swap(nums, i, j);
        }

        // Step 4: Reverse the suffix starting at i + 1
        Reverse(nums, i + 1);
    }

    private void Swap(int[] nums, int i, int j)
    {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private void Reverse(int[] nums, int start)
    {
        int end = nums.Length - 1;
        while (start < end)
        {
            Swap(nums, start, end);
            start++;
            end--;
        }
    }
}
