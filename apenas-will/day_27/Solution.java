class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        if(nums.length == 0) return 0;
        int lo = -1;
        if(nums[0] == 1) lo = 0;
        
        int hi = 0;
        int max = 0;

        while(hi < nums.length){
            if(nums[hi] == 1){
                hi ++;
            } else if(nums[hi] == 0){
                if (lo < 0) max = hi;
                else if (hi - lo > max) max = hi - lo;
                hi++;
                lo = hi;
            }
        }
        
        if(hi - lo > max) max = hi - lo;
        return max;
    }
}