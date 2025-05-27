using System;

public class Solution
{
    public string ReverseStr(string s, int k)
    {
        char[] arr = s.ToCharArray();
        for (int i = 0; i < arr.Length; i += 2 * k)
        {
            int left = i;
            int right = Math.Min(i + k - 1, arr.Length - 1);
            while (left < right)
            {
                char temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
                right--;
            }
        }
        return new string(arr);
    }
}