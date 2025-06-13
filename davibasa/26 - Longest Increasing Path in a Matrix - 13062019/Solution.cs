public class Solution {
    private int[][] directions = new int[][] {
        new int[] {0, 1}, new int[] {1, 0}, new int[] {0, -1}, new int[] {-1, 0}
    };
    
    public int LongestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.Length == 0 || matrix[0].Length == 0) {
            return 0;
        }
        
        int m = matrix.Length;
        int n = matrix[0].Length;
        int[,] memo = new int[m, n];
        int maxPath = 0;
        
        // Tenta encontrar o caminho mais longo a partir de cada célula
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                maxPath = Math.Max(maxPath, DFS(matrix, i, j, memo));
            }
        }
        
        return maxPath;
    }
    
    private int DFS(int[][] matrix, int row, int col, int[,] memo) {
        // Se já calculou este resultado, retorna da memória
        if (memo[row, col] != 0) {
            return memo[row, col];
        }
        
        int maxLength = 1; // Pelo menos a própria célula
        
        // Explora as 4 direções
        foreach (int[] direction in directions) {
            int newRow = row + direction[0];
            int newCol = col + direction[1];
            
            // Verifica se está dentro dos limites e se o valor é maior
            if (newRow >= 0 && newRow < matrix.Length && 
                newCol >= 0 && newCol < matrix[0].Length && 
                matrix[newRow][newCol] > matrix[row][col]) {
                
                maxLength = Math.Max(maxLength, 1 + DFS(matrix, newRow, newCol, memo));
            }
        }
        
        // Salva o resultado na memória
        memo[row, col] = maxLength;
        return maxLength;
    }
}
