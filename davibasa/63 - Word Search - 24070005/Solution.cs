using System;

public class Solution
{
    private int[][] directions = new int[][] {
        new int[] {0, 1}, new int[] {1, 0}, new int[] {0, -1}, new int[] {-1, 0}
    };

    public bool Exist(char[][] board, string word)
    {
        int m = board.Length, n = board[0].Length;

        // Try starting from each cell
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (board[i][j] == word[0] && DFS(board, word, i, j, 0))
                {
                    return true;
                }
            }
        }

        return false;
    }

    private bool DFS(char[][] board, string word, int row, int col, int index)
    {
        // Base case: found the complete word
        if (index == word.Length) return true;

        // Check boundaries and character match
        if (row < 0 || row >= board.Length || col < 0 || col >= board[0].Length ||
            board[row][col] != word[index])
        {
            return false;
        }

        // Mark current cell as visited
        char temp = board[row][col];
        board[row][col] = '#';

        // Explore all 4 directions
        foreach (var dir in directions)
        {
            int newRow = row + dir[0];
            int newCol = col + dir[1];

            if (DFS(board, word, newRow, newCol, index + 1))
            {
                board[row][col] = temp; // Restore before returning
                return true;
            }
        }

        // Backtrack: restore the original character
        board[row][col] = temp;
        return false;
    }
}
