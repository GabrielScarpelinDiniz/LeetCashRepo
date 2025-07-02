using System;
using System.Collections.Generic;
using System.Text;

public class Solution
{
    public IList<string> FullJustify(string[] words, int maxWidth)
    {
        var result = new List<string>();
        int start = 0;

        while (start < words.Length)
        {
            int end = GetLineEnd(words, start, maxWidth);
            result.Add(JustifyLine(words, start, end, maxWidth));
            start = end + 1;
        }

        return result;
    }

    private int GetLineEnd(string[] words, int start, int maxWidth)
    {
        int end = start;
        int totalLength = words[start].Length;

        while (end + 1 < words.Length)
        {
            int nextLength = totalLength + 1 + words[end + 1].Length; // +1 for space
            if (nextLength > maxWidth) break;
            totalLength = nextLength;
            end++;
        }

        return end;
    }

    private string JustifyLine(string[] words, int start, int end, int maxWidth)
    {
        int wordCount = end - start + 1;

        // Last line or single word line - left justify
        if (end == words.Length - 1 || wordCount == 1)
        {
            return LeftJustify(words, start, end, maxWidth);
        }

        // Calculate spaces needed
        int totalWordsLength = 0;
        for (int i = start; i <= end; i++)
        {
            totalWordsLength += words[i].Length;
        }

        int totalSpaces = maxWidth - totalWordsLength;
        int gaps = wordCount - 1;
        int spacesPerGap = totalSpaces / gaps;
        int extraSpaces = totalSpaces % gaps;

        var sb = new StringBuilder();
        for (int i = start; i <= end; i++)
        {
            sb.Append(words[i]);
            if (i < end) // Not the last word in the line
            {
                int spacesToAdd = spacesPerGap;
                if (i - start < extraSpaces) spacesToAdd++; // Add extra space
                sb.Append(new string(' ', spacesToAdd));
            }
        }

        return sb.ToString();
    }

    private string LeftJustify(string[] words, int start, int end, int maxWidth)
    {
        var sb = new StringBuilder();
        for (int i = start; i <= end; i++)
        {
            sb.Append(words[i]);
            if (i < end) sb.Append(' ');
        }

        // Pad with spaces to reach maxWidth
        while (sb.Length < maxWidth)
        {
            sb.Append(' ');
        }

        return sb.ToString();
    }
}
