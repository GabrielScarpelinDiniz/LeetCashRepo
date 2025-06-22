class Solution {
    public void DFS(boolean[] res, int ref, int destination, List<List<Integer>> graph, Set<Integer> visited){
        if(res[0]) return;
        visited.add(ref);

        if(ref == destination){
            res[0] = true;
            return;
        } else {
            for(int node: graph.get(ref)){
                if(!visited.contains(node)){
                    if(node == destination){
                        res[0] = true;
                        return;
                    }
                    DFS(res, node, destination, graph, visited);
                }
            }
        }
    }
    
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        List<List<Integer>> graph = new ArrayList<>();

        for(int i = 0; i < n; i++){
            graph.add(new ArrayList<>());
        }

        for(int[] edge: edges){
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        Set<Integer> visited = new HashSet<>();
        
        boolean[] res = {false};        
        DFS(res, source, destination, graph, visited);
        return res[0];
    }
}