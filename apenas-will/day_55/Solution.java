class Solution {
    static boolean cycleInPath(List<List<Integer>> dGraph, int node, Set<Integer> visited, Set<Integer> recStack){
        if(recStack.contains(node)) return true;
        if(visited.contains(node)) return false;
        
        visited.add(node);
        recStack.add(node);
        
        for(int neighbour = 0; neighbour < dGraph.get(node).size(); neighbour++){
            if(cycleInPath(dGraph, dGraph.get(node).get(neighbour), visited, recStack))return true;
        }

        recStack.remove(node);
        return false;
    }

    static boolean hasCycle(List<List<Integer>> graph){
        Set<Integer> visited = new HashSet<>();
        Set<Integer> recStack = new HashSet<>();
        for(int ref = 0; ref < graph.size(); ref++){
            if(cycleInPath(graph, ref, visited, recStack)) return true;
        }

        return false;
    }
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();

        for(int i = 0; i < numCourses; i++){
            graph.add(new ArrayList<>());
        }

        for(int i = 0; i < prerequisites.length; i++){
            graph.get(prerequisites[i][1]).add(prerequisites[i][0]);
        }

        return !hasCycle(graph);
    }
}