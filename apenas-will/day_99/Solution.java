class Solution {
    public boolean canJump(int[] nums) {
        boolean[] canBeReached = new boolean[nums.length];
        canBeReached[0] = true;

        for(int i = 0; i < nums.length; i++){
            for(int j = 0; j < nums[i] + 1; j++){
                if(!canBeReached[i]) {
                    return false;
                } 
                
                if(i + j < nums.length){
                    canBeReached[i + j] = true;
                }
            }
        }

        return canBeReached[nums.length - 1];
    }
}