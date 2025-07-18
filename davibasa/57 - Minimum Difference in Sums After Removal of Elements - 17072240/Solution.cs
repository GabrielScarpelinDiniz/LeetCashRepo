using System;
using System.Collections.Generic;

public class Solution
{
    public long MinimumDifference(int[] nums)
    {
        int n = nums.Length / 3;

        // Arrays to store minimum sums for first n elements and maximum sums for last n elements
        long[] minFirstSum = new long[n + 1];
        long[] maxSecondSum = new long[n + 1];

        // Priority queues (max heap for first part, min heap for second part)
        var maxHeap = new PriorityQueue<int, int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
        var minHeap = new PriorityQueue<int, int>();

        // Calculate minimum sum for first n elements from left to right
        long sum = 0;
        for (int i = 0; i < n; i++)
        {
            sum += nums[i];
            maxHeap.Enqueue(nums[i], nums[i]);
        }
        minFirstSum[0] = sum;

        for (int i = n; i < 2 * n; i++)
        {
            sum += nums[i];
            maxHeap.Enqueue(nums[i], nums[i]);
            sum -= maxHeap.Dequeue();
            minFirstSum[i - n + 1] = sum;
        }

        // Calculate maximum sum for last n elements from right to left
        sum = 0;
        for (int i = 3 * n - 1; i >= 2 * n; i--)
        {
            sum += nums[i];
            minHeap.Enqueue(nums[i], nums[i]);
        }
        maxSecondSum[n] = sum;

        for (int i = 2 * n - 1; i >= n; i--)
        {
            sum += nums[i];
            minHeap.Enqueue(nums[i], nums[i]);
            sum -= minHeap.Dequeue();
            maxSecondSum[i - n] = sum;
        }

        // Find minimum difference
        long minDiff = long.MaxValue;
        for (int i = 0; i <= n; i++)
        {
            minDiff = Math.Min(minDiff, minFirstSum[i] - maxSecondSum[i]);
        }

        return minDiff;
    }
}
