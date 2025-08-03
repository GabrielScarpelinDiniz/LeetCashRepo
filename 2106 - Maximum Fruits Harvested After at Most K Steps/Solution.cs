using System;
using System.Collections.Generic;

public class Solution
{
    public int MaxFruits(int[][] fruits, int startPos, int k)
    {
        int n = fruits.Length;
        int[] prefixSum = new int[n + 1];

        for (int i = 0; i < n; i++)
        {
            prefixSum[i + 1] = prefixSum[i] + fruits[i][1];
        }

        int maxFruits = 0;

        for (int i = 0; i < n; i++)
        {
            int left = Math.Max(0, startPos - k);
            int right = Math.Min(n - 1, startPos + k);

            int totalFruits = prefixSum[right + 1] - prefixSum[left];
            maxFruits = Math.Max(maxFruits, totalFruits);
        }

        return maxFruits;
    }
}
