class Solution {
    public void DFS(int[][] isConnected, int city, boolean[] visited){
        if(visited[city]) return;
        visited[city] = true;

        for(int i = 0; i < isConnected[city].length; i++){
            if(isConnected[city][i] == 1 && !visited[i]){
                DFS(isConnected, i, visited);
            }
        }
    }
    public int findCircleNum(int[][] isConnected) {
        boolean[] visited = new boolean[isConnected.length];
        int res = 0;
        for(int i = 0; i < isConnected.length; i++){
            if(!visited[i]){
                res++;
                DFS(isConnected, i, visited);
            }
        }
        return res;
    }
}