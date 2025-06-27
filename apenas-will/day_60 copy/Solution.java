class Solution {
    public int DFS(int[][] map, boolean[][] visited, int row, int column){
        if(row >= map.length || row < 0) return 1;
        if(column >= map[0].length || column < 0) return 1;
        if(map[row][column] == 0) return 1;
        if(visited[row][column]) return 0;

        visited[row][column] = true;
        int res = 0;
        res += DFS(map, visited, row + 1, column);
        res += DFS(map, visited, row - 1, column);
        res += DFS(map, visited, row, column + 1);
        res += DFS(map, visited, row, column - 1);
        return res;
    }
    public int islandPerimeter(int[][] grid) {
        Random r = new Random();
        while(true){
            int row = r.nextInt(grid.length);
            int col = r.nextInt(grid[0].length);
            if(grid[row][col] == 1){
                boolean[][] visited = new boolean[grid.length][grid[0].length];
                return DFS(grid, visited, row, col);
            }
        }
    }
}