class Solution {
    public void sortColors(int[] nums) {
        int[] count = new int[3];
        for(int n : nums){
            count[n] ++;
        }

        for(int i = 0; i < nums.length; i++){
            int element = -1;
            if(count[0] > 0) {
                element = 0;
                count[0] --;
            } else if (count[1] > 0){ 
                element = 1;
                count[1] --;
            } else {
                element = 2;
                count[2] --;
            }

            nums[i] = element;
        }
    }
}