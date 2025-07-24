using System;
using System.Collections.Generic;

public class Solution
{
    public int MinimumScore(int[] nums, int[][] edges)
    {
        int n = nums.Length;
        var graph = new List<int>[n];

        // Build adjacency list
        for (int i = 0; i < n; i++)
        {
            graph[i] = new List<int>();
        }

        foreach (var edge in edges)
        {
            graph[edge[0]].Add(edge[1]);
            graph[edge[1]].Add(edge[0]);
        }

        // Calculate subtree XOR for each node
        var subtreeXor = new int[n];
        var visited = new bool[n];

        int totalXor = CalculateSubtreeXor(0, -1, graph, nums, subtreeXor);

        int minScore = int.MaxValue;

        // Try removing each pair of edges
        for (int i = 0; i < edges.Length; i++)
        {
            for (int j = i + 1; j < edges.Length; j++)
            {
                var edge1 = edges[i];
                var edge2 = edges[j];

                // Calculate XOR values for the three components
                var xorValues = CalculateComponentXors(edge1, edge2, graph, nums, subtreeXor, totalXor);

                if (xorValues != null)
                {
                    Array.Sort(xorValues);
                    int score = xorValues[2] - xorValues[0];
                    minScore = Math.Min(minScore, score);
                }
            }
        }

        return minScore;
    }

    private int CalculateSubtreeXor(int node, int parent, List<int>[] graph, int[] nums, int[] subtreeXor)
    {
        int xor = nums[node];

        foreach (int neighbor in graph[node])
        {
            if (neighbor != parent)
            {
                xor ^= CalculateSubtreeXor(neighbor, node, graph, nums, subtreeXor);
            }
        }

        subtreeXor[node] = xor;
        return xor;
    }

    private int[] CalculateComponentXors(int[] edge1, int[] edge2, List<int>[] graph, int[] nums, int[] subtreeXor, int totalXor)
    {
        // Find which nodes are roots of subtrees after removing edges
        var components = new List<int>();

        // Try different configurations of edge removals
        var visited = new bool[graph.Length];

        // Simulate edge removal by DFS without crossing removed edges
        for (int start = 0; start < graph.Length; start++)
        {
            if (!visited[start])
            {
                int componentXor = 0;
                var stack = new Stack<int>();
                stack.Push(start);

                while (stack.Count > 0)
                {
                    int node = stack.Pop();
                    if (visited[node]) continue;

                    visited[node] = true;
                    componentXor ^= nums[node];

                    foreach (int neighbor in graph[node])
                    {
                        if (!visited[neighbor] && !IsRemovedEdge(node, neighbor, edge1, edge2))
                        {
                            stack.Push(neighbor);
                        }
                    }
                }

                components.Add(componentXor);
            }
        }

        return components.Count == 3 ? components.ToArray() : null;
    }

    private bool IsRemovedEdge(int u, int v, int[] edge1, int[] edge2)
    {
        return (u == edge1[0] && v == edge1[1]) || (u == edge1[1] && v == edge1[0]) ||
               (u == edge2[0] && v == edge2[1]) || (u == edge2[1] && v == edge2[0]);
    }
}
