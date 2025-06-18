class Solution {
    public int tribonacci(int n) {
     int[] memo = new int[n + 1];

     for(int i = 0; i < n + 1; i++){
        if(i == 0){
            memo[i] = 0;
        } else if (i <= 2){
            memo[i] = 1;
        } else {
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3];
        }
     }
     return memo[n];   
    }
}