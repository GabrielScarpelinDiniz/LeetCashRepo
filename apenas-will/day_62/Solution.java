class Solution {
    public int DFS(int[][] map, boolean[][] visited, int row, int col){
        if(row >= map.length || row < 0) return 0;
        if(col >= map[0].length || col < 0) return 0;
        if(map[row][col] == 0) return 0;
        if(visited[row][col]) return 0;

        visited[row][col] = true;

        int size = 1;

        size += DFS(map, visited, row + 1, col);
        size += DFS(map, visited, row - 1, col);
        size += DFS(map, visited, row, col + 1);
        size += DFS(map, visited, row, col - 1);

        return size;
    }
    public int maxAreaOfIsland(int[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int max = 0;

        for(int row = 0; row < grid.length; row++){
            for(int col = 0; col < grid[0].length; col ++){
                if(grid[row][col] == 1 && !visited[row][col]){
                    int temp = DFS(grid, visited, row, col);
                    if(temp >= max) max = temp;
                }
            }
        }

        return max;
    }
}