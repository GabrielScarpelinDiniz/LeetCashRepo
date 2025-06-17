public class Solution
{
    public int IslandPerimeter(int[][] grid)
    {
        int rows = grid.Length;
        int cols = grid[0].Length;
        int perimeter = 0;

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (grid[i][j] == 1)
                {
                    // Verifica cada lado: se estivermos na borda ou adjacente a água, incrementa perímetro
                    if (i == 0 || grid[i - 1][j] == 0) perimeter++;
                    if (i == rows - 1 || grid[i + 1][j] == 0) perimeter++;
                    if (j == 0 || grid[i][j - 1] == 0) perimeter++;
                    if (j == cols - 1 || grid[i][j + 1] == 0) perimeter++;
                }
            }
        }

        return perimeter;
    }
}
