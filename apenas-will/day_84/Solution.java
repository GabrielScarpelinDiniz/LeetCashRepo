class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length == 1) return 1;
        int k = 1;
        int lo = 0;
        int hi = 0;

        while(hi < nums.length){
            if(nums[lo] != nums[hi]){
                k++;
                lo ++;
                nums[lo] = nums[hi];
            } else {
                hi ++;
            }   
        }
        
        return k;
    }
}