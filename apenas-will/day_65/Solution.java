class Solution {
    public boolean isBorder(int[][] grid, int row, int col, int original, int color, boolean[][] visited){
        if(row < 0 || row >= grid.length) return true;
        if(col < 0 || col >= grid[0].length) return true;
        if(visited[row][col]) return false;    
        if(grid[row][col] != original) return true;

        visited[row][col] = true;

        boolean res = false;
        res = res | isBorder(grid, row + 1, col, original, color, visited);
        res = res | isBorder(grid, row - 1, col, original, color, visited);
        res = res | isBorder(grid, row, col + 1, original, color, visited);
        res = res | isBorder(grid, row, col - 1, original, color, visited);

        if(res) grid[row][col] = color;

        return false;
    }
    
    public int[][] colorBorder(int[][] grid, int row, int col, int color) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        isBorder(grid, row, col, grid[row][col], color, visited);
        return grid;
    }
}