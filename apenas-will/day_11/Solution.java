class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int sl = 0;
        int fa = 0;

        while(fa < prices.length){
            if(prices[fa] - prices[sl] >= max){
                max = prices[fa] - prices[sl];
            }
            if(prices[fa] < prices[sl]){
                sl = fa;
            }
            fa++;
        }
        
        return max;
    }
}