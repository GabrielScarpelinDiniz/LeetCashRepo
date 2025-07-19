using System;
using System.Collections.Generic;

public class Solution
{
    public IList<string> RemoveSubfolders(string[] folder)
    {
        Array.Sort(folder, StringComparer.Ordinal);
        var result = new List<string>();
        string prev = "";

        foreach (var f in folder)
        {
            // Se prev está vazia ou f não é subpasta de prev, adiciona ao resultado
            if (prev == "" || !f.StartsWith(prev + "/"))
            {
                result.Add(f);
                prev = f;
            }
        }

        return result;
    }
}
