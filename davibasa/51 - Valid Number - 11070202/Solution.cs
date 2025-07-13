using System;

public class Solution
{
    public bool IsNumber(string s)
    {
        bool seenDigit = false;
        bool seenExponent = false;
        bool seenDot = false;

        for (int i = 0; i < s.Length; i++)
        {
            char c = s[i];

            if (char.IsDigit(c))
            {
                seenDigit = true;
            }
            else if (c == '+' || c == '-')
            {
                // Sign can only be at the beginning or right after 'e'/'E'
                if (i != 0 && s[i - 1] != 'e' && s[i - 1] != 'E')
                {
                    return false;
                }
            }
            else if (c == '.')
            {
                // Dot cannot appear after exponent or if we've seen a dot before
                if (seenExponent || seenDot)
                {
                    return false;
                }
                seenDot = true;
            }
            else if (c == 'e' || c == 'E')
            {
                // Exponent cannot appear if we haven't seen digits or if we've seen exponent before
                if (seenExponent || !seenDigit)
                {
                    return false;
                }
                seenExponent = true;
                seenDigit = false; // Reset to check for digits after exponent
            }
            else
            {
                // Invalid character
                return false;
            }
        }

        return seenDigit;
    }
}
