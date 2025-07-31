class Solution {
    public int uniquePaths(int m, int n) {
        int[][] numPaths = new int[m][n];

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(i == 0){
                    numPaths[i][j] = 1;
                } else if(j == 0){
                    numPaths[i][j] = 1;
                } else {
                    numPaths[i][j] = numPaths[i][j - 1] + numPaths[i - 1][j];
                }
            }
        }

        return numPaths[m - 1][n - 1];
    }
}