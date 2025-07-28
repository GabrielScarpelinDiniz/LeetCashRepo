class Solution {
    public void backtracking(int[] res, int max, int[] nums, int total, int start){
        if(total == max){
            res[0] ++;
        }

        for(int i = start; i < nums.length; i++){
            if((total | nums[i])<= max){
                backtracking(res, max, nums, total | nums[i], i + 1);
            }
        }
    }

    public int countMaxOrSubsets(int[] nums) {
        int[] res = new int[1];
        int max = 0;
        
        for(int i : nums){
            max |= i;
        }

        backtracking(res, max, nums, 0, 0);
        
        return res[0];   
    }
}