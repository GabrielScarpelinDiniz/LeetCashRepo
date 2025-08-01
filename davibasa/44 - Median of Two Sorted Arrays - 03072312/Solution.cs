using System;

public class Solution
{
    public double FindMedianSortedArrays(int[] nums1, int[] nums2)
    {
        // Ensure nums1 is the smaller array
        if (nums1.Length > nums2.Length)
        {
            return FindMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.Length;
        int n = nums2.Length;
        int left = 0, right = m;

        while (left <= right)
        {
            int partitionX = (left + right) / 2;
            int partitionY = (m + n + 1) / 2 - partitionX;

            // Handle edge cases
            int maxLeftX = (partitionX == 0) ? int.MinValue : nums1[partitionX - 1];
            int minRightX = (partitionX == m) ? int.MaxValue : nums1[partitionX];

            int maxLeftY = (partitionY == 0) ? int.MinValue : nums2[partitionY - 1];
            int minRightY = (partitionY == n) ? int.MaxValue : nums2[partitionY];

            if (maxLeftX <= minRightY && maxLeftY <= minRightX)
            {
                // Found the correct partition
                if ((m + n) % 2 == 0)
                {
                    return (Math.Max(maxLeftX, maxLeftY) + Math.Min(minRightX, minRightY)) / 2.0;
                }
                else
                {
                    return Math.Max(maxLeftX, maxLeftY);
                }
            }
            else if (maxLeftX > minRightY)
            {
                // Move left in nums1
                right = partitionX - 1;
            }
            else
            {
                // Move right in nums1
                left = partitionX + 1;
            }
        }

        // Should never reach here for valid input
        throw new ArgumentException("Input arrays are not sorted");
    }
}
