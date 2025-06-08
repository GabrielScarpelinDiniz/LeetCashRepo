class Solution {
    public int findCenter(int[][] edges) {
        int[] counts = new int[edges.length + 1];

        for(int[] edge: edges){
            counts[edge[0] - 1] ++;
            counts[edge[1] - 1] ++;
        }

        int max = 0;
        int index = 0;
        for(int i = 0; i < counts.length; i++){
            if(counts[i] > max){
                max = counts[i];
                index = i;
            }
        }

        return index + 1;
    }
}