using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public IList<IList<string>> DeleteDuplicateFolder(IList<IList<string>> paths)
    {
        var trie = new TrieNode();

        // Build trie from all paths
        foreach (var path in paths)
        {
            var current = trie;
            foreach (var folder in path)
            {
                if (!current.Children.ContainsKey(folder))
                {
                    current.Children[folder] = new TrieNode();
                }
                current = current.Children[folder];
            }
        }

        // Generate signatures for each subtree
        var signatureToNodes = new Dictionary<string, List<TrieNode>>();
        GenerateSignatures(trie, signatureToNodes);

        // Mark duplicate nodes for deletion
        foreach (var entry in signatureToNodes)
        {
            if (entry.Value.Count > 1 && entry.Key != "")
            {
                foreach (var node in entry.Value)
                {
                    node.ToDelete = true;
                }
            }
        }

        // Collect remaining paths
        var result = new List<IList<string>>();
        CollectPaths(trie, new List<string>(), result);

        return result;
    }

    private string GenerateSignatures(TrieNode node, Dictionary<string, List<TrieNode>> signatureToNodes)
    {
        var childSignatures = new List<string>();

        foreach (var child in node.Children)
        {
            var childSignature = GenerateSignatures(child.Value, signatureToNodes);
            if (!child.Value.ToDelete)
            {
                childSignatures.Add($"({child.Key}{childSignature})");
            }
        }

        childSignatures.Sort();
        var signature = string.Join("", childSignatures);

        if (!signatureToNodes.ContainsKey(signature))
        {
            signatureToNodes[signature] = new List<TrieNode>();
        }
        signatureToNodes[signature].Add(node);

        return signature;
    }

    private void CollectPaths(TrieNode node, List<string> currentPath, IList<IList<string>> result)
    {
        if (currentPath.Count > 0 && !node.ToDelete)
        {
            result.Add(new List<string>(currentPath));
        }

        foreach (var child in node.Children)
        {
            if (!child.Value.ToDelete)
            {
                currentPath.Add(child.Key);
                CollectPaths(child.Value, currentPath, result);
                currentPath.RemoveAt(currentPath.Count - 1);
            }
        }
    }
}

public class TrieNode
{
    public Dictionary<string, TrieNode> Children { get; set; }
    public bool ToDelete { get; set; }

    public TrieNode()
    {
        Children = new Dictionary<string, TrieNode>();
        ToDelete = false;
    }
}
