using System;
using System.Collections.Generic;

public class WordFilter
{
    private Dictionary<string, int> map;

    public WordFilter(string[] words)
    {
        map = new Dictionary<string, int>();

        for (int index = 0; index < words.Length; index++)
        {
            string word = words[index];
            int len = word.Length;

            // Generate all possible prefix#suffix combinations
            for (int i = 0; i <= len; i++)
            {
                for (int j = 0; j <= len; j++)
                {
                    string prefix = word.Substring(0, i);
                    string suffix = word.Substring(len - j);
                    string key = prefix + "#" + suffix;
                    map[key] = index; // This will overwrite with the largest index
                }
            }
        }
    }

    public int F(string pref, string suff)
    {
        string key = pref + "#" + suff;
        return map.ContainsKey(key) ? map[key] : -1;
    }
}
