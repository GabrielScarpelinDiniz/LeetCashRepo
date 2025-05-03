class Solution {
    
    int Fibonacci(int n){
        if(n <= 1) return 1;

        int[] processed = new int[n + 1];
        processed[0] = 1;
        processed[1] = 1;
        

        for(int i = 0; i <= n; i++){
            if(processed[i] == 0){
                processed[i] = processed[i-1] + processed[i-2];
            }
        }

        return processed[n];

    }
    public int climbStairs(int n) {
        return Fibonacci(n);
    }
}
