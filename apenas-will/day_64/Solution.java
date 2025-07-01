class Solution {
    public void DFS(int[][] image, int row, int col, int def, int color, boolean[][] visited){
        if(row < 0 || row >= image.length) return;
        if(col < 0 || col >= image[0].length) return;
        if(visited[row][col]) return;
        if(image[row][col] != def) return;

        image[row][col] = color;
        visited[row][col] = true;

        DFS(image, row + 1, col, def, color, visited);
        DFS(image, row - 1, col, def, color, visited);
        DFS(image, row, col + 1, def, color, visited);
        DFS(image, row, col - 1, def, color, visited);
    }
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        boolean[][] visited = new boolean[image.length][image[0].length];
        DFS(image, sr, sc, image[sr][sc], color, visited);
        return image;
    }
}