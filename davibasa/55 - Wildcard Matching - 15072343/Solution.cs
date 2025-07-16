using System;

public class Solution
{
    public bool IsMatch(string s, string p)
    {
        int sLen = s.Length, pLen = p.Length;
        int sIndex = 0, pIndex = 0;
        int starIndex = -1, match = 0;

        while (sIndex < sLen)
        {
            // If characters match or pattern has '?', advance both pointers
            if (pIndex < pLen && (p[pIndex] == '?' || s[sIndex] == p[pIndex]))
            {
                sIndex++;
                pIndex++;
            }
            // If pattern has '*', record positions and advance pattern pointer
            else if (pIndex < pLen && p[pIndex] == '*')
            {
                starIndex = pIndex;
                match = sIndex;
                pIndex++;
            }
            // If no match and we have seen '*' before, backtrack
            else if (starIndex >= 0)
            {
                pIndex = starIndex + 1;
                match++;
                sIndex = match;
            }
            // No match and no '*' to backtrack
            else
            {
                return false;
            }
        }

        // Skip any remaining '*' in pattern
        while (pIndex < pLen && p[pIndex] == '*')
        {
            pIndex++;
        }

        // Pattern should be fully consumed
        return pIndex == pLen;
    }
}
