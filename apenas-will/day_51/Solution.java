class Solution {
    public int fib(int n) {
       int[] fibs = new int[n + 1];

       for(int i = 0; i < n + 1; i ++){
        if (i == 0){
            fibs[i] = 0;
        } else if(i <= 2){
            fibs[i] = 1;
        } else {
            fibs[i] = fibs[i-1] + fibs[i-2];
        }
       }

       return fibs[n];
    }
}