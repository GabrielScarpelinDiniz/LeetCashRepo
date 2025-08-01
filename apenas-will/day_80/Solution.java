class Solution {
    public void rotate(int[][] matrix) {
        // First transpose
        for(int i = 0; i < matrix.length; i ++){
            for(int j = i; j < matrix[0].length; j ++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // Invert in x axis
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length / 2; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][matrix.length - j - 1];
                matrix[i][matrix.length - j - 1] = temp;
            }
        }
    }
}