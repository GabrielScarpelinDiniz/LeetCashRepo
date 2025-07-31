class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int[][] uniquePathsTo = new int[obstacleGrid.length][obstacleGrid[0].length];

        for(int i = 0; i < obstacleGrid.length; i++){
            for(int j = 0; j < obstacleGrid[0].length; j++){
                if(i == 0){
                    if(obstacleGrid[i][j] == 0){
                        uniquePathsTo[i][j] = 1;
                    } 
                    if(j - 1 >= 0 && uniquePathsTo[i][j-1] < 1){
                        uniquePathsTo[i][j] = 0;
                    }
                } else if(j == 0){
                    if(obstacleGrid[i][j] == 0){
                        uniquePathsTo[i][j] = 1;
                    }
                    if(i - 1 >= 0 && uniquePathsTo[i - 1][j] == 0){
                        uniquePathsTo[i][j] = 0;
                    }
                } else {
                    if(obstacleGrid[i][j] == 0){
                        uniquePathsTo[i][j] = uniquePathsTo[i][j - 1] + uniquePathsTo[i - 1][j];
                    }
                }
            }
        }

        return uniquePathsTo[obstacleGrid.length - 1][obstacleGrid[0].length - 1];
        
    }
}