class Solution {
    public void moveZeroes(int[] nums) {
        int real = 0;

        for(int i = 0; i < nums.length; i++){
            if(nums[i] != 0){
                nums[real] = nums[i];
                real ++;
            }
        }

        for(int z = real; z < nums.length; z ++){
            nums[z] = 0;
        }
    }
}