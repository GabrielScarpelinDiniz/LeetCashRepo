class Solution {
    public int jump(int[] nums) {
        if(nums.length == 2) return 1;
        int[] jumpsToReach = new int[nums.length];
        
        for(int i = 1; i < nums.length; i ++){
            jumpsToReach[i] = Integer.MAX_VALUE;
        }

        for(int i = 0; i < nums.length - 1; i++){
            for(int j = 0; j < nums[i]; j++){
                if(i + j + 1 < nums.length){
                    jumpsToReach[i + j + 1] = Math.min(jumpsToReach[i + j + 1], jumpsToReach[i] + 1);
                }
            }
        }

        return jumpsToReach[nums.length - 1];
    }
}