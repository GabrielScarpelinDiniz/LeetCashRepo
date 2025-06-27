using System;
using System.Collections.Generic;

public class Solution
{
    public string RemoveKdigits(string num, int k)
    {
        if (k >= num.Length) return "0";

        Stack<char> stack = new Stack<char>();

        foreach (char digit in num)
        {
            while (stack.Count > 0 && k > 0 && stack.Peek() > digit)
            {
                stack.Pop();
                k--;
            }
            stack.Push(digit);
        }

        // Remove remaining digits if k > 0
        while (k > 0 && stack.Count > 0)
        {
            stack.Pop();
            k--;
        }

        // Build the result
        char[] result = stack.ToArray();
        Array.Reverse(result);
        string finalResult = new string(result).TrimStart('0');

        return finalResult.Length > 0 ? finalResult : "0";
    }
}
