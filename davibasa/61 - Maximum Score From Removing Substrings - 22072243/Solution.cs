using System;
using System.Collections.Generic;

public class Solution
{
    public int MaximumGain(string s, int x, int y)
    {
        // Remove the higher value substring first
        if (x >= y)
        {
            return RemoveSubstring(s, "ab", x) + RemoveSubstring(s, "ba", y);
        }
        else
        {
            return RemoveSubstring(s, "ba", y) + RemoveSubstring(s, "ab", x);
        }
    }

    private int RemoveSubstring(string s, string target, int points)
    {
        var stack = new Stack<char>();
        int score = 0;

        foreach (char c in s)
        {
            if (stack.Count > 0 && stack.Peek() == target[0] && c == target[1])
            {
                stack.Pop(); // Remove the first character of target
                score += points;
            }
            else
            {
                stack.Push(c);
            }
        }

        // Update s with remaining characters
        var remaining = new char[stack.Count];
        for (int i = stack.Count - 1; i >= 0; i--)
        {
            remaining[i] = stack.Pop();
        }
        s = new string(remaining);

        return score;
    }
}
