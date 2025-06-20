public class Solution
{
    public int LongestPalindrome(string s)
    {
        var freq = new Dictionary<char, int>();
        foreach (char c in s)
        {
            if (!freq.ContainsKey(c))
                freq[c] = 0;
            freq[c]++;
        }

        int length = 0;
        bool hasOdd = false;
        foreach (var count in freq.Values)
        {
            length += (count / 2) * 2;
            if (count % 2 == 1)
                hasOdd = true;
        }

        if (hasOdd)
            length += 1;

        return length;
    }
}
