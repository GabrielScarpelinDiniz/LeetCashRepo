using System;
using System.Collections.Generic;

public class Solution
{
    public int SubarrayBitwiseORs(int[] arr)
    {
        HashSet<int> result = new HashSet<int>();
        HashSet<int> current = new HashSet<int>();

        foreach (int num in arr)
        {
            HashSet<int> next = new HashSet<int>();
            next.Add(num);

            foreach (int prev in current)
            {
                next.Add(prev | num);
            }

            foreach (int val in next)
            {
                result.Add(val);
            }

            current = next;
        }

        return result.Count;
    }
}
