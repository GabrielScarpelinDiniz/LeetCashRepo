class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] res = new int[numCourses];
        List<List<Integer>> adjList = new ArrayList<>();
        for(int i = 0; i < numCourses; i++){
            adjList.add(new ArrayList<>());
        }

        int[] inDegree = new int[numCourses];
        for(int[] edge : prerequisites){
            adjList.get(edge[1]).add(edge[0]);
            inDegree[edge[0]] ++;
        }

        int i = 0;
        Queue<Integer> nextToAdd = new ArrayDeque<>();
        for(int j = 0; j < inDegree.length; j++){
            if (inDegree[j] == 0) nextToAdd.add(j);
        }

        while(!nextToAdd.isEmpty()){
            int prereq = nextToAdd.remove();

            res[i] = prereq;
            i++;

            for(int j : adjList.get(prereq)){
                inDegree[j] --;
                if(inDegree[j] == 0) nextToAdd.add(j);
            }
        }

        if(i < numCourses - 1) return new int[0];

        return res;
    }
}