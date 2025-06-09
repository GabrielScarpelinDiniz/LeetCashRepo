class Solution {
    public int findJudge(int n, int[][] trust) {
        int[][] trustCounts = new int[n][2];

        for(int[] t: trust){
            trustCounts[t[0] - 1][0] ++;
            trustCounts[t[1] - 1][1] ++;
        }

        for(int i = 0; i < n; i++){
            if(trustCounts[i][0] == 0 && trustCounts[i][1] == n - 1){
                return i + 1;
            }
        }

        return -1;
    }
}