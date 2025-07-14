using System;
using System.Collections.Generic;

public class Solution
{
    private int m, n, total;
    private Random rand;
    private Dictionary<int, int> map;

    public Solution(int m, int n)
    {
        this.m = m;
        this.n = n;
        this.total = m * n;
        this.rand = new Random();
        this.map = new Dictionary<int, int>();
    }

    public int[] Flip()
    {
        int index = rand.Next(total);
        total--;

        // Check if this index has been remapped
        int actualIndex = map.ContainsKey(index) ? map[index] : index;

        // Remap the selected index to the last available index
        map[index] = map.ContainsKey(total) ? map[total] : total;

        return new int[] { actualIndex / n, actualIndex % n };
    }

    public void Reset()
    {
        total = m * n;
        map.Clear();
    }
}
