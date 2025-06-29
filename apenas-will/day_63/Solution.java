class Solution {
    public void DFS(char[][] map, int row, int col){
        if(row >= map.length || row < 0) return;
        if(col >= map[0].length || col < 0) return;
        if(map[row][col] == '0') return;

        map[row][col] = '0';
        DFS(map, row + 1, col);
        DFS(map, row - 1, col);
        DFS(map, row, col + 1);
        DFS(map, row, col - 1);
    }

    public int numIslands(char[][] grid) {
        int numIslands = 0;

        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == '1'){
                    numIslands ++;
                    DFS(grid, i, j);
                }
            }
        }

        return numIslands;
    }
}