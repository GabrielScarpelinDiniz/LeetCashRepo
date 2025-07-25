class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] maxAt = new int[nums.length];

        int res = 0;
        for(int i = 0; i < nums.length; i++){
            maxAt[i] = 1;
            int max = 1;
            for(int j = 0; j < i; j++){
                if(nums[j] < nums[i]) {
                    if(max < maxAt[j] + 1) max = maxAt[j] + 1;
                }
            }
            maxAt[i] = max;
            res = max > res? max: res;
        }

        return res;
    }
}